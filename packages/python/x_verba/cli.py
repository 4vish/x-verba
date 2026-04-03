"""
X-Verba CLI entry point — v0.2.0
Find the governance gaps in your AI code before your users do.
"""
import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

BANNER = """
 ██╗  ██╗      ██╗   ██╗███████╗██████╗ ██████╗  █████╗
 ╚██╗██╔╝      ██║   ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
  ╚███╔╝ █████╗██║   ██║█████╗  ██████╔╝██████╔╝███████║
  ██╔██╗ ╚════╝╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██╗██╔══██║
 ██╔╝ ██╗       ╚████╔╝ ███████╗██║  ██║██████╔╝██║  ██║
 ╚═╝  ╚═╝        ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝

 Governance Infrastructure for the AI Era
 by Super Semantics — supersemantics.org
"""


@click.group()
@click.version_option(version="0.2.0", prog_name="x-verba")
def main():
    """
    X-Verba — Find the governance gaps in your AI code before your users do.

    AI writes code. AI runs code. X-Verba governs it.

    Five modes:

    \b
      scan      Scan any repo → governance contract + test case matrix
      qa        [coming v0.2] Check code against schema → regression report
      forensics [coming v0.2] Reverse engineer failures → DC decomposition
      prompt    [coming v0.2] Generate governed prompt for AI coding tools
      compile   [coming v0.2] Compile approved schema → executable bundle
    """
    pass


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="yaml",
    help="Output format. yaml = governance contract, json = machine-readable, md = human report",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file path. Default: .verba/governance.[format]",
)
@click.option(
    "--identity-key", "-k",
    type=str,
    default=None,
    help="Identity Key for this system. Scopes governance events across the full lifecycle.",
)
@click.option(
    "--context-profile", "-p",
    type=click.Choice(["ai-app", "system-utility", "general"], case_sensitive=False),
    default="ai-app",
    help=(
        "Context profile. "
        "ai-app = AI-adjacent only (default). "
        "system-utility = suppress file op false positives. "
        "general = scan everything (legacy)."
    ),
)
@click.option(
    "--strict-ai-only",
    is_flag=True,
    default=False,
    help="Exit code 1 if no AI integrations found. Use in CI on repos that must use AI.",
)
@click.option(
    "--no-test-matrix",
    is_flag=True,
    default=False,
    help="Skip generating the test case matrix. Governance contract only.",
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    default=False,
    help="Show detailed scan progress and skipped files.",
)
def scan(path, output_format, output, identity_key, context_profile, strict_ai_only, no_test_matrix, verbose):
    """
    Scan any repo and generate a governance contract + test case matrix.

    PATH is the directory to scan. Defaults to current directory.

    What this does:

    \b
      1. Reads your code — finds every AI call, irreversible action,
         and existing constraint (AST-based for Python, regex for JS/TS)
      2. Maps findings to the VERBA governance taxonomy
      3. Identifies governance gaps: missing Pre-Nodes, ungated irreversible
         actions, missing Human Gates, informal Invariants
      4. Generates governance.yaml — the VERBA contract you fill in to
         define what your system must and must never do
      5. Generates test_case_matrix.yaml — structured test stubs for every
         node, invariant, threshold, and terminal state

    Context profiles control what gets flagged:

    \b
      ai-app        — only flag issues in AI-integrated files (default)
      system-utility — suppress file op false positives for tools/compilers
      general        — flag everything, like v0.1 (may produce false positives)

    Examples:

    \b
      x-verba scan .
      x-verba scan ./my-repo --format json
      x-verba scan ./my-repo --context-profile system-utility
      x-verba scan ./my-repo --strict-ai-only
      x-verba scan ./my-repo --identity-key my-system-v1.0
    """
    from x_verba.scanner.engine import ScanEngine
    from x_verba.output.writer import OutputWriter
    from x_verba.output.test_matrix import TestMatrixWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Scan", style="bold"),
        subtitle=f"Governance contract generation  |  profile: {context_profile}",
        border_style="dim",
    ))
    console.print()

    engine = ScanEngine(verbose=verbose, context_profile=context_profile)
    results = engine.scan(path, identity_key=identity_key)

    # --strict-ai-only: exit 1 if no AI found
    if strict_ai_only and results.get("summary", {}).get("ai_integrations_detected", 0) == 0:
        console.print(
            "[bold red]--strict-ai-only: No AI integrations detected. "
            "Expected AI usage in this repo.[/bold red]"
        )
        raise SystemExit(1)

    writer = OutputWriter(results, output_format)
    output_path = writer.write(output)

    matrix_path = None
    if not no_test_matrix:
        matrix_writer = TestMatrixWriter(results)
        from pathlib import Path as _Path
        matrix_out = str(_Path(output_path).parent / "test_case_matrix.yaml")
        matrix_path = matrix_writer.write(matrix_out)

    _print_terminal_summary(results, output_path, matrix_path)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--schema", "-s",
    type=click.Path(exists=True),
    required=True,
    help="Path to the approved governance schema (YAML or JSON)",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the regression report",
)
@click.option(
    "--fail-on-critical",
    is_flag=True,
    default=True,
    help="Exit with non-zero status if critical governance regressions found (default: true)",
)
def qa(path, schema, output_format, fail_on_critical):
    """
    [coming v0.2] Check code against an approved governance schema.

    Compares your codebase against the governance contract defined in SCHEMA.
    Flags every place where the code has drifted from the contract.

    Designed to run in CI/CD pipelines on every commit.

    Examples:

    \b
      x-verba qa . --schema .verba/governance.yaml
      x-verba qa . --schema .verba/governance.yaml --format json
    """
    from x_verba.scanner.qa_engine import QAEngine
    from x_verba.output.writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba QA", style="bold"),
        subtitle="Governance regression check",
        border_style="dim",
    ))
    console.print()

    engine = QAEngine()
    results = engine.check(path, schema)

    if results.get("status") == "not_implemented":
        return

    writer = OutputWriter(results, output_format)
    output_path = writer.write(None)
    _print_qa_summary(results, output_path)

    if fail_on_critical and results.get("has_critical_regressions"):
        raise SystemExit(1)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--identity-key", "-k",
    type=str,
    default=None,
    help="Identity Key to trace across the full governance chain",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the forensic report",
)
def forensics(path, identity_key, output_format):
    """
    [coming v0.2] Reverse engineer governance failures — DC decomposition.

    Examples:

    \b
      x-verba forensics ./legacy-repo
      x-verba forensics ./repo --identity-key my-system-v1.0
    """
    from x_verba.scanner.forensics_engine import ForensicsEngine
    from x_verba.output.writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Forensics", style="bold"),
        subtitle="Reverse engineering governance failures",
        border_style="dim",
    ))
    console.print()

    engine = ForensicsEngine()
    results = engine.analyse(path, identity_key=identity_key)

    if results.get("status") == "not_implemented":
        return

    writer = OutputWriter(results, output_format)
    output_path = writer.write(None)
    _print_forensics_summary(results, output_path)


@main.command()
@click.option(
    "--description", "-d",
    type=str,
    default=None,
    help="Plain language description of what you want to build",
)
@click.option(
    "--from-repo",
    type=click.Path(exists=True),
    default=None,
    help="Infer governance requirements from an existing partial codebase",
)
@click.option(
    "--domain",
    type=click.Choice([
        "healthcare", "finance", "legal", "infrastructure",
        "education", "ecommerce", "general",
    ], case_sensitive=False),
    default="general",
    help="Domain context for governance requirement inference",
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["txt", "md", "json"], case_sensitive=False),
    default="md",
    help="Output format for the governed prompt",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file. Default: .verba/governed-prompt.[format]",
)
def prompt(description, from_repo, domain, output_format, output):
    """
    [coming v0.2] Generate a governance-informed prompt for AI coding tools.

    Examples:

    \b
      x-verba prompt -d "patient triage API using GPT-4" --domain healthcare
      x-verba prompt --from-repo ./partial-codebase --domain finance
    """
    from x_verba.scanner.prompt_engine import PromptEngine

    console.print()
    console.print(Panel(
        Text("X-Verba Prompt", style="bold"),
        subtitle="Generating governance-informed prompt",
        border_style="dim",
    ))
    console.print()

    if not description and not from_repo:
        console.print("[red]Error:[/red] Provide either --description or --from-repo")
        raise SystemExit(1)

    engine = PromptEngine()
    results = engine.generate(
        description=description,
        from_repo=from_repo,
        domain=domain,
    )


@main.command()
@click.argument("schema", type=click.Path(exists=True))
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output path for compiled bundle. Default: .verba/bundle.vsl",
)
@click.option(
    "--validate-only",
    is_flag=True,
    default=False,
    help="Validate the schema without compiling",
)
def compile(schema, output, validate_only):
    """
    [coming v0.2] Compile an approved governance schema into an executable bundle.

    Examples:

    \b
      x-verba compile .verba/governance.yaml
      x-verba compile .verba/governance.yaml --validate-only
    """
    from x_verba.scanner.compile_engine import CompileEngine

    console.print()
    console.print(Panel(
        Text("X-Verba Compile", style="bold"),
        subtitle="Compiling governance schema to executable bundle",
        border_style="dim",
    ))
    console.print()

    engine = CompileEngine()

    if validate_only:
        results = engine.validate(schema)
        _print_validation_summary(results)
    else:
        results = engine.compile(schema, output)
        _print_compile_summary(results)


# ── Terminal output helpers ───────────────────────────────────────────────────

def _print_terminal_summary(results, output_path, matrix_path=None):
    """Print clean terminal summary of scan results."""
    console.print()

    stats = results.get("summary", {})
    critical = stats.get("critical", 0)
    high = stats.get("high", 0)
    medium = stats.get("medium", 0)
    coverage = stats.get("governance_coverage", "N/A")
    gamma = stats.get("structural_gamma")
    files = stats.get("files_scanned", 0)
    ai_count = stats.get("ai_integrations_detected", 0)
    profile = stats.get("context_profile", "ai-app")

    # No AI integrations case
    if stats.get("governance_status") == "NO_AI_INTEGRATIONS":
        console.print(f"[dim]Files scanned:[/dim] {files}")
        console.print(f"[dim]Context profile:[/dim] {profile}")
        console.print()
        console.print("[yellow]No AI integrations detected.[/yellow]")
        console.print(f"[dim]{stats.get('note', '')}[/dim]")
        console.print()
        return

    gamma_str = str(gamma) if gamma is not None else "N/A"
    console.print(f"[dim]Files scanned:[/dim]          {files}")
    console.print(f"[dim]AI integrations:[/dim]        {ai_count}")
    console.print(f"[dim]Context profile:[/dim]        {profile}")
    console.print(
        f"[dim]Governance coverage:[/dim]   {coverage}"
    )
    console.print(
        f"[dim]Structural Gamma proxy:[/dim] {gamma_str} "
        f"[dim](threshold: 0.9)[/dim]"
    )
    console.print()

    if critical > 0:
        console.print(
            f"[bold red]CRITICAL: {critical}[/bold red]  "
            f"[yellow]HIGH: {high}[/yellow]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )
    elif high > 0:
        console.print(
            f"[green]No critical findings[/green]  "
            f"[yellow]HIGH: {high}[/yellow]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )
    else:
        console.print(
            f"[green]No critical or high findings[/green]  "
            f"[dim]MEDIUM: {medium}[/dim]"
        )

    console.print()

    findings = results.get("critical_findings", [])[:3]
    if findings:
        console.print("[bold]Top findings:[/bold]")
        for f in findings:
            console.print(f"  [red]✗[/red]  {f.get('location', 'unknown')}")
            console.print(f"     {f.get('plain_english', '')}")
            dc = f.get("dc_candidate", "")
            if dc:
                console.print(f"     [dim]→ {dc}[/dim]")
            console.print()

    console.print(f"[dim]Governance contract:[/dim] {output_path}")
    if matrix_path:
        console.print(f"[dim]Test case matrix:  [/dim] {matrix_path}")
    console.print()
    console.print("[dim]Next steps:[/dim]")
    console.print("[dim]  1. Fill in the null fields in governance.yaml[/dim]")
    console.print("[dim]  2. Complete test stubs in test_case_matrix.yaml[/dim]")
    console.print("[dim]  3. Add x-verba qa to your CI/CD pipeline (coming v0.2)[/dim]")
    console.print()


def _print_qa_summary(results, output_path):
    """Print QA regression summary."""
    regressions = results.get("regressions", [])
    critical = [r for r in regressions if r.get("severity") == "critical"]
    high = [r for r in regressions if r.get("severity") == "high"]

    if not regressions:
        console.print("[green]Governance check passed.[/green]")
        console.print("[dim]No governance regressions detected.[/dim]")
    else:
        console.print(
            f"[bold red]Governance regressions detected: {len(regressions)}[/bold red]"
        )
        console.print(
            f"[red]Critical: {len(critical)}[/red]  "
            f"[yellow]High: {len(high)}[/yellow]"
        )
        console.print()
        for r in critical[:3]:
            console.print(f"  [red]✗[/red]  {r.get('location', 'unknown')}")
            console.print(f"     {r.get('description', '')}")
            console.print()

    console.print(f"[dim]Full report:[/dim] {output_path}")
    console.print()


def _print_forensics_summary(results, output_path):
    """Print forensics decomposition summary."""
    dc_classes = results.get("dc_classes_detected", [])
    gamma = results.get("structural_gamma", {})

    console.print(f"[dim]Drift Classes detected:[/dim] {len(dc_classes)}")
    console.print(
        f"[dim]Structural Gamma proxy:[/dim] "
        f"{gamma.get('proxy_value', 'N/A')}"
    )
    console.print()

    if dc_classes:
        console.print("[bold]DC decomposition:[/bold]")
        for dc in dc_classes[:5]:
            console.print(
                f"  {dc.get('code', '')}  {dc.get('name', '')}  "
                f"[dim]Tier {dc.get('tier', '?')}[/dim]"
            )
            console.print(f"     {dc.get('plain_english', '')[:80]}")
            so = dc.get("primary_so", "")
            if so:
                console.print(f"     [dim]→ Recommended: {so}[/dim]")
            console.print()

    console.print(f"[dim]Full forensic report:[/dim] {output_path}")
    console.print()


def _print_validation_summary(results):
    valid = results.get("valid", False)
    issues = results.get("issues", [])

    if valid:
        console.print("[green]Schema validation passed.[/green]")
        console.print("[dim]Schema is complete and ready to compile.[/dim]")
    else:
        console.print(
            f"[bold red]Schema validation failed: {len(issues)} issues[/bold red]"
        )
        for issue in issues[:5]:
            console.print(f"  [red]✗[/red]  {issue}")
    console.print()


def _print_compile_summary(results):
    success = results.get("success", False)
    output_path = results.get("output_path", "")
    version = results.get("version_hash", "")

    if success:
        console.print("[green]Compilation successful.[/green]")
        console.print(f"[dim]Bundle:[/dim] {output_path}")
        console.print(f"[dim]Version:[/dim] {version}")
        console.print("\n[dim]Deploy this bundle with the VERBA Runtime.[/dim]")
        console.print("[dim]The Priming Engine will load it and begin monitoring.[/dim]")
    else:
        console.print("[bold red]Compilation failed.[/bold red]")
        for error in results.get("errors", [])[:5]:
            console.print(f"  [red]✗[/red]  {error}")
    console.print()


if __name__ == "__main__":
    main()

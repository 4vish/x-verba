"""
X-Verba CLI entry point.
Find the governance gaps in your code before your users do.
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
 by Super Semantics — https://supersemantic.ai
"""

@click.group()
@click.version_option(version="0.1.0", prog_name="x-verba")
def main():
    """
    X-Verba — Find the governance gaps in your code before your users do.

    AI writes code. AI runs code. X-Verba governs it.

    Five modes:

    \b
      scan      Scan any repo → governance report + template
      qa        Check code against schema → regression report
      forensics Reverse engineer failures → DC decomposition
      prompt    Generate governed prompt for AI coding tools
      compile   Compile approved schema → executable bundle
    """
    pass


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="yaml",
    help="Output format. yaml = governance template, json = machine-readable, md = human report"
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file path. Default: .verba/governance.[format]"
)
@click.option(
    "--identity-key", "-k",
    type=str,
    default=None,
    help="Identity Key for this system. Scopes governance events across the full lifecycle."
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    default=False,
    help="Show detailed scan progress"
)
def scan(path, output_format, output, identity_key, verbose):
    """
    Scan any repo and generate a governance report.

    PATH is the directory to scan. Defaults to current directory.

    What this does:

    \b
      1. Reads your code structure — actions, integration points,
         data flows, state transitions
      2. Maps detected patterns to the VERBA governance taxonomy
      3. Identifies unprotected decision points and governance gaps
      4. Generates a pre-filled governance template with plain-language
         explanations of every finding

    The output is a governance scaffold you fill in to define what your
    system must and must never do. Every field is explained inline.
    Domain knowledge stays with you — X-Verba provides the structure.

    Examples:

    \b
      x-verba scan .
      x-verba scan ./my-repo --format json
      x-verba scan ./my-repo --output ./governance.yaml
      x-verba scan ./my-repo --identity-key my-system-v1.0
    """
    from x_verba.scanner.engine import ScanEngine
    from x_verba.output.writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Scan", style="bold"),
        subtitle="Find the governance gaps in your code before your users do",
        border_style="dim"
    ))
    console.print()

    engine = ScanEngine(verbose=verbose)
    results = engine.scan(path, identity_key=identity_key)

    writer = OutputWriter(results, output_format)
    output_path = writer.write(output)

    _print_terminal_summary(results, output_path)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option(
    "--schema", "-s",
    type=click.Path(exists=True),
    required=True,
    help="Path to the approved governance schema (YAML or JSON)"
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the regression report"
)
@click.option(
    "--fail-on-critical",
    is_flag=True,
    default=True,
    help="Exit with non-zero status if critical governance regressions found (default: true)"
)
def qa(path, schema, output_format, fail_on_critical):
    """
    Check code against an approved governance schema.

    Compares your codebase against the governance contract defined in SCHEMA.
    Flags every place where the code has drifted from the contract.

    Designed to run in CI/CD pipelines on every commit. Governance
    regressions are caught before they ship.

    What this checks:

    \b
      - New unprotected decision points not in the schema
      - Pre-Nodes defined in schema but missing from code
      - Invariants that exist in schema but are bypassed in code
      - New AI integrations added since schema was last approved

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
        border_style="dim"
    ))
    console.print()

    engine = QAEngine()
    results = engine.check(path, schema)

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
    help="Identity Key to trace across the full governance chain"
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["yaml", "json", "md"], case_sensitive=False),
    default="md",
    help="Output format for the forensic report"
)
def forensics(path, identity_key, output_format):
    """
    Reverse engineer governance failures — DC decomposition.

    Scans any codebase — legacy, undocumented, inherited, or post-failure —
    and produces a structural diagnostic.

    What this produces:

    \b
      - Drift Class decomposition of detected failure modes
      - Pre-Node gap map showing where governance was absent
      - Structural Gamma proxy — governed vs ungoverned estimate
      - Stabilisation Operator recommendations with contraindications
      - Remediation roadmap

    If an Identity Key is provided, traces the complete governance chain:
    what was specified → what was generated → what was tested → what
    was released → what the runtime recorded.

    The Knight Capital example:

    \b
      x-verba forensics ./knight-capital-reconstruction
      → DC-E14 Substrate Contamination detected
      → Pre-Node gap: activation_conflict_check missing
      → One VSL Eligibility Condition would have prevented $440M loss

    Examples:

    \b
      x-verba forensics ./legacy-repo
      x-verba forensics ./repo --identity-key my-system-v1.0
      x-verba forensics ./repo --format md --output forensics-report.md
    """
    from x_verba.scanner.forensics_engine import ForensicsEngine
    from x_verba.output.writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Forensics", style="bold"),
        subtitle="Reverse engineering governance failures",
        border_style="dim"
    ))
    console.print()

    engine = ForensicsEngine()
    results = engine.analyse(path, identity_key=identity_key)

    writer = OutputWriter(results, output_format)
    output_path = writer.write(None)

    _print_forensics_summary(results, output_path)


@main.command()
@click.option(
    "--description", "-d",
    type=str,
    default=None,
    help="Plain language description of what you want to build"
)
@click.option(
    "--from-repo",
    type=click.Path(exists=True),
    default=None,
    help="Infer governance requirements from an existing partial codebase"
)
@click.option(
    "--domain",
    type=click.Choice([
        "healthcare", "finance", "legal", "infrastructure",
        "education", "ecommerce", "general"
    ], case_sensitive=False),
    default="general",
    help="Domain context for governance requirement inference"
)
@click.option(
    "--format", "output_format",
    type=click.Choice(["txt", "md", "json"], case_sensitive=False),
    default="md",
    help="Output format for the governed prompt"
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output file. Default: .verba/governed-prompt.[format]"
)
def prompt(description, from_repo, domain, output_format, output):
    """
    Generate a governance-informed prompt for AI coding tools.

    Tell AI coding tools what the code must never do — before they write
    a single line. The generated prompt embeds VERBA governance requirements
    directly into the code generation request.

    Feed the output to Claude, Copilot, Cursor, or any AI coding assistant.
    The generated code will have governance structure baked in from the
    first line.

    What this maintains across the full lifecycle:

    \b
      What was fed    → the governed prompt (declared intent)
      What was received → the generated code (actual output)
      What was tested → x-verba scan validates it
      What was released → verba compile locks it

    The same Identity Key and governance vocabulary runs through all four.
    Forensics can trace back to the first word of the first prompt.

    Examples:

    \b
      x-verba prompt -d "patient triage API using GPT-4" --domain healthcare
      x-verba prompt --from-repo ./partial-codebase --domain finance
      x-verba prompt -d "document analysis tool" -o my-governed-prompt.md
    """
    from x_verba.scanner.prompt_engine import PromptEngine
    from x_verba.output.writer import OutputWriter

    console.print()
    console.print(Panel(
        Text("X-Verba Prompt", style="bold"),
        subtitle="Generating governance-informed prompt",
        border_style="dim"
    ))
    console.print()

    if not description and not from_repo:
        console.print(
            "[red]Error:[/red] Provide either --description or --from-repo"
        )
        raise SystemExit(1)

    engine = PromptEngine()
    results = engine.generate(
        description=description,
        from_repo=from_repo,
        domain=domain
    )

    writer = OutputWriter(results, output_format)
    output_path = writer.write(output)

    console.print(f"\n[green]Governed prompt written to:[/green] {output_path}")
    console.print(
        "\nFeed this to Claude, Copilot, Cursor, or any AI coding tool."
    )
    console.print(
        "Then run [bold]x-verba scan[/bold] to validate what was generated.\n"
    )


@main.command()
@click.argument("schema", type=click.Path(exists=True))
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Output path for compiled bundle. Default: .verba/bundle.vsl"
)
@click.option(
    "--validate-only",
    is_flag=True,
    default=False,
    help="Validate the schema without compiling"
)
def compile(schema, output, validate_only):
    """
    Compile an approved governance schema into an executable bundle.

    Reads the approved YAML or JSON schema and produces a machine-executable
    invariant bundle that the VERBA Runtime loads and enforces.

    What this produces:

    \b
      - Compiled invariant bundle (.vsl) for the VERBA Runtime
      - Schema validation report
      - Completeness check — flags missing fields, unresolved gaps
      - Version hash — links this bundle to the schema that produced it

    Think of this as your governance build step — like tsc for TypeScript
    or terraform plan for infrastructure. It validates before anything
    goes live.

    Examples:

    \b
      x-verba compile .verba/governance.yaml
      x-verba compile .verba/governance.yaml --validate-only
      x-verba compile .verba/governance.yaml -o .verba/bundle.vsl
    """
    from x_verba.scanner.compile_engine import CompileEngine

    console.print()
    console.print(Panel(
        Text("X-Verba Compile", style="bold"),
        subtitle="Compiling governance schema to executable bundle",
        border_style="dim"
    ))
    console.print()

    engine = CompileEngine()

    if validate_only:
        results = engine.validate(schema)
        _print_validation_summary(results)
    else:
        results = engine.compile(schema, output)
        _print_compile_summary(results)


def _print_terminal_summary(results, output_path):
    """Print clean terminal summary of scan results."""
    from rich.table import Table

    console.print()

    stats = results.get("summary", {})
    critical = stats.get("critical", 0)
    high = stats.get("high", 0)
    medium = stats.get("medium", 0)
    coverage = stats.get("governance_coverage", "0%")
    gamma = stats.get("structural_gamma", "N/A")
    files = stats.get("files_scanned", 0)

    console.print(f"[dim]Files scanned:[/dim] {files}")
    console.print(f"[dim]Governance coverage:[/dim] {coverage}")
    console.print(
        f"[dim]Structural Gamma proxy:[/dim] {gamma} "
        f"[dim](threshold: 1.0)[/dim]"
    )
    console.print()

    if critical > 0:
        console.print(
            f"[bold red]CRITICAL findings: {critical}[/bold red]  "
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
            console.print(
                f"  [red]✗[/red]  {f.get('location', 'unknown')}"
            )
            console.print(
                f"     {f.get('plain_english', '')}"
            )
            dc = f.get("dc_candidate", "")
            if dc:
                console.print(f"     [dim]→ {dc}[/dim]")
            console.print()

    console.print(f"[dim]Full report:[/dim] {output_path}")
    console.print(
        "[dim]Next step:[/dim] Fill in the policy fields in the report"
    )
    console.print(
        "[dim]         [/dim] then open in Verba Studio for "
        "AI-assisted authoring"
    )
    console.print()


def _print_qa_summary(results, output_path):
    """Print QA regression summary."""
    regressions = results.get("regressions", [])
    critical = [r for r in regressions if r.get("severity") == "critical"]
    high = [r for r in regressions if r.get("severity") == "high"]

    if not regressions:
        console.print("[green]Governance check passed.[/green]")
        console.print(
            "[dim]No governance regressions detected.[/dim]"
        )
    else:
        console.print(
            f"[bold red]Governance regressions detected: "
            f"{len(regressions)}[/bold red]"
        )
        console.print(
            f"[red]Critical: {len(critical)}[/red]  "
            f"[yellow]High: {len(high)}[/yellow]"
        )
        console.print()
        for r in critical[:3]:
            console.print(
                f"  [red]✗[/red]  {r.get('location', 'unknown')}"
            )
            console.print(f"     {r.get('description', '')}")
            console.print()

    console.print(f"[dim]Full report:[/dim] {output_path}")
    console.print()


def _print_forensics_summary(results, output_path):
    """Print forensics decomposition summary."""
    dc_classes = results.get("dc_classes_detected", [])
    gamma = results.get("structural_gamma", {})

    console.print(
        f"[dim]Drift Classes detected:[/dim] {len(dc_classes)}"
    )
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
            console.print(
                f"     {dc.get('plain_english', '')[:80]}"
            )
            so = dc.get("primary_so", "")
            if so:
                console.print(
                    f"     [dim]→ Recommended: {so}[/dim]"
                )
            console.print()

    console.print(f"[dim]Full forensic report:[/dim] {output_path}")
    console.print()


def _print_validation_summary(results):
    """Print schema validation summary."""
    valid = results.get("valid", False)
    issues = results.get("issues", [])

    if valid:
        console.print(
            "[green]Schema validation passed.[/green]"
        )
        console.print(
            "[dim]Schema is complete and ready to compile.[/dim]"
        )
    else:
        console.print(
            f"[bold red]Schema validation failed: "
            f"{len(issues)} issues[/bold red]"
        )
        for issue in issues[:5]:
            console.print(f"  [red]✗[/red]  {issue}")
    console.print()


def _print_compile_summary(results):
    """Print compile summary."""
    success = results.get("success", False)
    output_path = results.get("output_path", "")
    version = results.get("version_hash", "")

    if success:
        console.print("[green]Compilation successful.[/green]")
        console.print(f"[dim]Bundle:[/dim] {output_path}")
        console.print(f"[dim]Version:[/dim] {version}")
        console.print(
            "\n[dim]Deploy this bundle with the VERBA Runtime.[/dim]"
        )
        console.print(
            "[dim]The Priming Engine will load it and begin "
            "monitoring.[/dim]"
        )
    else:
        console.print("[bold red]Compilation failed.[/bold red]")
        for error in results.get("errors", [])[:5]:
            console.print(f"  [red]✗[/red]  {error}")
    console.print()


if __name__ == "__main__":
    main()

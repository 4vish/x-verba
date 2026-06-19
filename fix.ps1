$replacements = @(
    ("x_verba\cli.py", "from engine import ScanEngine, OutputFormatter", "from .engine import ScanEngine, OutputFormatter"),
    ("x_verba\cli.py", "from writer import OutputWriter", "from .writer import OutputWriter"),
    ("x_verba\cli.py", "from baseline import BaselineStore", "from .baseline import BaselineStore"),
    ("x_verba\baseline.py", "from engine import OutputFormatter", "from .engine import OutputFormatter"),
    ("x_verba\engine.py", "from models import (", "from .models import ("),
    ("x_verba\engine.py", "from graph import pagerank", "from .graph import pagerank"),
    ("x_verba\qa_engine.py", "from models import DeltaDirection", "from .models import DeltaDirection"),
    ("x_verba\writer.py", "from engine import OutputFormatter", "from .engine import OutputFormatter"),
    ("x_verba\writer.py", "from qa_engine import", "from .qa_engine import"),
    ("x_verba\graph\pagerank.py", "from models import DecisionGraph", "from ..models import DecisionGraph"),
    ("x_verba\graph\critical_path.py", "from models import DecisionGraph", "from ..models import DecisionGraph"),
    ("x_verba\graph\propagation.py", "from models import DecisionGraph", "from ..models import DecisionGraph")
)
foreach ($r in $replacements) { 
    $content = Get-Content $r[0] -Raw
    $content = $content -replace [regex]::Escape($r[1]), $r[2]
    Set-Content $r[0] $content
    Write-Host "? $($r[0])"
}
$toml = Get-Content "pyproject.toml" -Raw
$toml = $toml -replace 'packages = \["x_verba"\]', 'packages = ["x_verba", "x_verba.graph", "x_verba.tests"]'
Set-Content "pyproject.toml" $toml
Write-Host "? pyproject.toml"
@"
from setuptools import setup, find_packages

setup(
    packages=find_packages(),
)
"@ | Set-Content "setup.py"
Write-Host "? setup.py created"

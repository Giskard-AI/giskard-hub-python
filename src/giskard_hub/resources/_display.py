"""Rich-based display helpers for evaluation and scan metrics."""

import math
from typing import Optional, TypedDict

from rich.table import Table
from rich.console import Console

from ..types.scan import Severity, ScanProbeResult, ScanProbeAttempt
from ..types.common import TaskState
from ..types.evaluation import Evaluation

__all__ = [
    "print_evaluation_metrics_table",
    "build_scan_probe_data",
    "print_scan_metrics_table",
]


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SUCCESS_RATE_THRESHOLD_HIGH = 0.8
SUCCESS_RATE_THRESHOLD_MEDIUM = 0.5

_SEVERITY_COLORS = {
    Severity.CRITICAL: "red",
    Severity.MAJOR: "orange",
    Severity.MINOR: "yellow",
}


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------


class ProbeData(TypedDict):
    category: str
    probe_name: str
    status: Optional[TaskState]
    severity: Optional[Severity]
    num_issues: Optional[int]
    num_attacks: Optional[int]


# ---------------------------------------------------------------------------
# Evaluation display
# ---------------------------------------------------------------------------


def print_evaluation_metrics_table(entity: Evaluation) -> None:
    """Print evaluation metrics (name, success rate, details) to the console."""
    console = Console()
    table = Table(
        "Metric",
        "Result",
        "Details",
        title=f"Evaluation Run [bold cyan]{entity.name}[/bold cyan]",
    )
    for metric in entity.metrics:
        success_rate = metric.success_rate
        if success_rate is None or math.isnan(success_rate):
            continue
        if success_rate > SUCCESS_RATE_THRESHOLD_HIGH:
            color = "green"
        elif success_rate > SUCCESS_RATE_THRESHOLD_MEDIUM:
            color = "yellow"
        else:
            color = "red"
        total = metric.total or 0
        passed = metric.passed or 0
        failed = metric.failed or 0
        errored = metric.errored or 0
        skipped = total - passed - failed - errored
        table.add_row(
            f"[bold]{metric.name.capitalize()}[/bold]",
            f"[{color}]{success_rate * 100:.2f}%[/{color}]",
            f"[bright_black]{passed} passed, {failed} failed, {errored} errored, {skipped} not executed[/bright_black]",
        )
    console.print(table)


# ---------------------------------------------------------------------------
# Scan display
# ---------------------------------------------------------------------------


def build_scan_probe_data(
    category_map: dict[str, str],
    probe_results: list[ScanProbeResult],
    attempts_by_probe_id: dict[str, list[ScanProbeAttempt]],
) -> list[ProbeData]:
    """Build sorted probe data for scan metrics display."""
    probe_data: list[ProbeData] = []
    for probe in probe_results:
        category_name = category_map.get(probe.category, probe.category)
        probe_name = probe.name
        if probe_name.endswith(" Probe"):
            probe_name = probe_name.removesuffix("Probe").strip()
        if probe.status.state != "finished":
            probe_data.append(
                {
                    "category": category_name,
                    "probe_name": probe_name,
                    "status": probe.status.state,
                    "severity": None,
                    "num_issues": None,
                    "num_attacks": None,
                }
            )
        else:
            attempts = attempts_by_probe_id.get(probe.id, [])
            num_attacks = len(attempts)
            num_issues = sum(1 for attempt in attempts if attempt.severity > Severity.SAFE)
            max_severity = max((attempt.severity for attempt in attempts), default=Severity.SAFE)
            probe_data.append(
                {
                    "category": category_name,
                    "probe_name": probe_name,
                    "status": None,
                    "severity": max_severity,
                    "num_issues": num_issues,
                    "num_attacks": num_attacks,
                }
            )
    probe_data.sort(
        key=lambda x: (
            x["category"],
            -(x["severity"] if x["severity"] is not None else -1),
            x["probe_name"],
        )
    )
    return probe_data


def print_scan_metrics_table(probe_data: list[ProbeData], entity_id: str) -> None:
    """Print scan probe metrics table to the console."""
    console = Console()
    table = Table(
        "Category",
        "Probe Name",
        "Severity",
        "Results",
        title=f"Scan Result [bold cyan]{entity_id}[/bold cyan]",
    )
    for data in probe_data:
        if data["status"] is not None:
            status_str = str(data["status"]).upper()
            status_color = "bright_black"
            severity_text = f"[{status_color}]{status_str}[/{status_color}]"
            results_text = str(data["status"]).capitalize()
            table.add_row(
                data["category"],
                data["probe_name"],
                severity_text,
                results_text,
            )
        else:
            severity_val = data["severity"]
            color: str = _SEVERITY_COLORS.get(severity_val, "green") if severity_val is not None else "green"
            num_issues = data["num_issues"]
            num_attacks = data["num_attacks"]
            severity_label = Severity(severity_val).name if severity_val is not None else "—"
            if num_issues == 0:
                issues_text = "[bold]No issues found[/bold]"
            elif num_issues == 1:
                issues_text = "[bold]1 issue[/bold]"
            else:
                issues_text = f"[bold]{num_issues} issues[/bold]"
            attacks_text = "1 attack" if num_attacks == 1 else f"{num_attacks} attacks"
            results_text = f"{issues_text} / {attacks_text}"
            table.add_row(
                data["category"],
                data["probe_name"],
                f"[{color}]{severity_label}[/{color}]",
                results_text,
            )
    console.print(table)

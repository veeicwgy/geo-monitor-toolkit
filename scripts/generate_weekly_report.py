#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

LABELS = {
    "mention_rate": "Mention Rate",
    "positive_mention_rate": "Positive Mention Rate",
    "capability_accuracy": "Capability Accuracy",
    "ecosystem_accuracy": "Ecosystem Accuracy",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    summary = json.loads(Path(args.summary).read_text(encoding="utf-8"))
    metrics = summary.get("metrics", {})
    by_model = summary.get("by_model", [])
    repair_candidates = summary.get("repair_candidates", [])

    lines = [
        f"# GEO Weekly Report — {summary.get('project', 'Unknown')}",
        "",
        f"- Run ID: `{summary.get('run_id', 'unknown')}`",
        f"- Created At: `{summary.get('created_at', 'unknown')}`",
        f"- Record Count: `{summary.get('record_count', 0)}`",
        "",
        "## Four-Metric Snapshot",
        "",
        "| Metric | Score |",
        "|---|---:|",
    ]
    for key, label in LABELS.items():
        lines.append(f"| {label} | {metrics.get(key, 0):.2f} |")

    lines.extend([
        "",
        "## By Model",
        "",
        "| Model | Mention | Positive | Capability | Ecosystem |",
        "|---|---:|---:|---:|---:|",
    ])
    for row in by_model:
        lines.append(
            f"| {row.get('model_id', 'unknown')} | {row.get('mention_rate', 0):.2f} | {row.get('positive_mention_rate', 0):.2f} | {row.get('capability_accuracy', 0):.2f} | {row.get('ecosystem_accuracy', 0):.2f} |"
        )

    lines.extend([
        "",
        "## Repair Candidates",
        "",
    ])
    if repair_candidates:
        lines.extend([
            "| Query | Model | Repair Type |",
            "|---|---|---|",
        ])
        for item in repair_candidates:
            lines.append(f"| {item.get('query_id', 'unknown')} | {item.get('model_id', 'unknown')} | {item.get('repair_type', 'none')} |")
    else:
        lines.append("No repair candidates were flagged in this run.")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ok", "output": args.output}, ensure_ascii=False))


if __name__ == "__main__":
    main()

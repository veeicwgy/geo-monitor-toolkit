#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path

METRICS = ["mention_score", "sentiment_score", "capability_score", "ecosystem_score"]
OUTPUT_MAP = {
    "mention_score": "mention_rate",
    "sentiment_score": "positive_mention_rate",
    "capability_score": "capability_accuracy",
    "ecosystem_score": "ecosystem_accuracy",
}


def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def pct(values):
    values = [v for v in values if v is not None]
    return round(sum(values) / len(values) * 100, 2) if values else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output-dir", required=True)
    args = ap.parse_args()

    rows = load_jsonl(args.input)
    if not rows:
        raise SystemExit("Input annotation file is empty.")

    by_model = defaultdict(list)
    repair_candidates = []
    for row in rows:
        by_model[row.get("model_id", "unknown")].append(row)
        if row.get("needs_repair"):
            repair_candidates.append(
                {
                    "query_id": row.get("query_id"),
                    "model_id": row.get("model_id"),
                    "repair_type": row.get("repair_type", "unspecified"),
                }
            )

    model_rows = []
    for model_id, items in by_model.items():
        metric_row = {"model_id": model_id}
        for src, dst in OUTPUT_MAP.items():
            metric_row[dst] = pct([r.get(src) for r in items])
        model_rows.append(metric_row)

    summary = {
        "run_id": Path(args.output_dir).name,
        "created_at": rows[0].get("captured_at"),
        "project": rows[0].get("project", "Unknown"),
        "record_count": len(rows),
        "metrics": {
            dst: round(sum(row[dst] for row in model_rows) / len(model_rows), 2) for dst in OUTPUT_MAP.values()
        },
        "by_model": sorted(model_rows, key=lambda x: x["model_id"]),
        "repair_candidates": repair_candidates,
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": "ok", "summary": str(out_dir / 'summary.json')}, ensure_ascii=False))


if __name__ == "__main__":
    main()

"""Evidence behind the Tayseer SAR 40M recommendation.

Reproduces every number in the deck from the course dataset (tayseer_services.csv),
using the same adoption formula as the Tableau dashboard:
    SUM([Digital Adoption Pct] / 100 * [Unique Users]) / SUM([Unique Users]) * 100

Usage:
    python analysis/analyze.py path/to/tayseer_services.csv
Writes analysis/regional_gap_dec2025.csv and prints a JSON summary.
Standard library only (no pandas needed).
"""
import csv
import json
import os
import sys
from collections import defaultdict

TARGET = 65.0
LATEST, PREV_YEAR = "2025-12-01", "2024-12-01"
NUMERIC = ("transactions", "unique_users", "digital_adoption_pct", "csat",
           "avg_completion_min", "first_time_resolution_pct", "cost_per_txn_sar", "sla_breach_pct")


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in NUMERIC:
            r[k] = float(r[k])
    return rows


def adoption(rs):
    users = sum(r["unique_users"] for r in rs)
    return sum(r["digital_adoption_pct"] / 100 * r["unique_users"] for r in rs) / users * 100


def wavg(rs, field):
    w = sum(r["transactions"] for r in rs)
    return sum(r[field] * r["transactions"] for r in rs) / w


def group(rs, key):
    g = defaultdict(list)
    for r in rs:
        g[r[key]].append(r)
    return g


def main(path):
    rows = load(path)
    by_month = group(rows, "month")
    national = {m: adoption(v) for m, v in sorted(by_month.items())}
    cur, prev = by_month[LATEST], by_month[PREV_YEAR]
    reg_cur, reg_prev = group(cur, "region"), group(prev, "region")

    regions = []
    for name, rs in reg_cur.items():
        a, a_prev = adoption(rs), adoption(reg_prev[name])
        users = sum(r["unique_users"] for r in rs)
        txns = sum(r["transactions"] for r in rs)
        assisted = sum(r["transactions"] for r in rs if r["channel"] in ("Branch", "Call Center"))
        gap = TARGET - a
        regions.append({
            "region": name,
            "adoption_dec2025": round(a, 2),
            "adoption_dec2024": round(a_prev, 2),
            "change_pts_per_year": round(a - a_prev, 2),
            "gap_to_65_pts": round(max(gap, 0), 2),
            "unique_users_dec2025": int(users),
            "users_to_reach_65": int(round(max(gap, 0) / 100 * users)),
            "months_to_65_at_current_pace": round(gap / (a - a_prev) * 12, 1) if gap > 0 else 0,
            "assisted_txn_share_pct": round(assisted / txns * 100, 1),
        })
    regions.sort(key=lambda r: r["adoption_dec2025"])
    gap_total = sum(r["users_to_reach_65"] for r in regions)
    for r in regions:
        r["share_of_remaining_gap_pct"] = round(r["users_to_reach_65"] / gap_total * 100, 1)

    out_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "regional_gap_dec2025.csv")
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(regions[0].keys()))
        w.writeheader()
        w.writerows(regions)

    y2025 = [r for r in rows if r["month"].startswith("2025")]
    channels = {c: {"cost_per_txn_sar": round(wavg(v, "cost_per_txn_sar"), 2), "csat": round(wavg(v, "csat"), 2)}
                for c, v in group(y2025, "channel").items()}
    below = [r for r in regions if r["gap_to_65_pts"] > 0]
    priority = below[:4]
    summary = {
        "national_dec2025": round(national[LATEST], 2),
        "national_dec2024": round(national[PREV_YEAR], 2),
        "first_month_at_or_above_65": next(m for m, v in national.items() if v >= TARGET),
        "regions_below_65": [r["region"] for r in below],
        "priority_four": [r["region"] for r in priority],
        "priority_four_share_of_gap_pct": round(sum(r["share_of_remaining_gap_pct"] for r in priority), 1),
        "channels_2025": channels,
    }
    print(json.dumps(summary, indent=2))
    print(f"\nWrote {out_csv}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])

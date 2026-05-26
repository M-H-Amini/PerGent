import csv
from pathlib import Path

import numpy as np
from scipy.stats import wilcoxon, rankdata


def read_orders(obs_path):
    methods = []
    l_order = []
    with obs_path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row.get("Method"):
                continue
            method = row["Method"].strip()
            l_val = row["LLM"].strip()
            if method not in methods:
                methods.append(method)
            if l_val != "Average" and l_val not in l_order:
                l_order.append(l_val)
    return methods, l_order


def read_observations(obs_path):
    rows = []
    with obs_path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def a12(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    n1 = len(x)
    n2 = len(y)
    ranks = rankdata(np.concatenate([x, y]))
    r1 = ranks[:n1].sum()
    u1 = r1 - n1 * (n1 + 1) / 2
    return u1 / (n1 * n2)


def effect_label(a):
    d = abs(a - 0.5)
    if d < 0.06:
        return "N"
    if d < 0.14:
        return "S"
    if d < 0.21:
        return "M"
    return "L"


def main():
    obs_path = Path("measurements.csv")
    out_path = Path("stat.csv")

    methods, l_order = read_orders(obs_path)
    rows = read_observations(obs_path)

    p_order = [f"P{i}" for i in range(1, 11)]
    p_index = {p: i for i, p in enumerate(p_order)}
    l_index = {l: i for i, l in enumerate(l_order)}

    # Sort to ensure consistent pairing
    rows_sorted = sorted(
        rows,
        key=lambda r: (
            r["Method"],
            l_index[r["LLM"]],
            p_index[r["Persona"]],
        ),
    )

    metrics = ["Distinctness", "Full Preservation", "Partial Preservation"]
    comparisons = ["OneShot", "OneShot+Res", "PerGentNoRes"]

    results = []
    for method in comparisons:
        row = {"PerGent vs": method}
        for metric in metrics:
            x = [float(r[metric]) for r in rows_sorted if r["Method"] == "PerGent"]
            y = [float(r[metric]) for r in rows_sorted if r["Method"] == method]
            stat = wilcoxon(x, y, zero_method="wilcox", alternative="two-sided", mode="approx")
            p_value = float(stat.pvalue)
            a = a12(x, y)
            row[f"{metric} p-value"] = f"{p_value:.3f}"
            row[f"{metric} A12"] = f"{a:.2f} ({effect_label(a)})"
        results.append(row)

    header = [
        "PerGent vs",
        "Distinctness p-value",
        "Distinctness A12",
        "Full Preservation p-value",
        "Full Preservation A12",
        "Partial Preservation p-value",
        "Partial Preservation A12",
    ]

    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()

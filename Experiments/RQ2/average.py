import csv
from collections import defaultdict
from pathlib import Path


def read_avg_order(obs_path):
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


def compute_averages(obs_path):
    sums = defaultdict(lambda: defaultdict(float))
    counts = defaultdict(int)
    with obs_path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            method = row["Method"].strip()
            l_val = row["LLM"].strip()
            key = (method, l_val)
            sums[key]["Distinctness"] += float(row["Distinctness"])
            sums[key]["Full Preservation"] += float(row["Full Preservation"])
            sums[key]["Partial Preservation"] += float(row["Partial Preservation"])
            counts[key] += 1

    averages = defaultdict(dict)
    for (method, l_val), metrics in sums.items():
        averages[(method, l_val)] = {
            "Distinctness": metrics["Distinctness"] / counts[(method, l_val)],
            "Full Preservation": metrics["Full Preservation"] / counts[(method, l_val)],
            "Partial Preservation": metrics["Partial Preservation"] / counts[(method, l_val)],
        }
    return averages


def write_avg_csv(out_path, methods, l_order, averages):
    header = ["Method", "LLM", "Distinctness", "Full Preservation", "Partial Preservation"]
    lines = ["%s\n" % ",".join(header)]

    for method in methods:
        # per-L rows
        for l_val in l_order:
            row = averages[(method, l_val)]
            lines.append(
                "%s,%s,%.3f,%.3f,%.3f\n"
                % (method, l_val, row["Distinctness"], row["Full Preservation"], row["Partial Preservation"])
            )
        # Average row per method
        total = {"Distinctness": 0.0, "Full Preservation": 0.0, "Partial Preservation": 0.0}
        for l_val in l_order:
            for k in total:
                total[k] += averages[(method, l_val)][k]
        avg = {k: total[k] / len(l_order) for k in total}
        lines.append(
            "%s,Average,%.3f,%.3f,%.3f\n"
            % (method, avg["Distinctness"], avg["Full Preservation"], avg["Partial Preservation"])
        )
        lines.append("\n")

    out_path.write_text("".join(lines), encoding="utf-8")


def main():
    obs_path = Path("measurements.csv")
    out_path = Path("avg.csv")

    methods, l_order = read_avg_order(obs_path)
    averages = compute_averages(obs_path)
    write_avg_csv(out_path, methods, l_order, averages)


if __name__ == "__main__":
    main()

import csv
from collections import defaultdict


def format_value(value, force_one_decimal=False):
    if force_one_decimal:
        return f"{value:.1f}"
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.1f}"


def main():
    input_path = "observation.csv"
    output_path = "avg.csv"

    method_order = []
    l_order = defaultdict(list)
    sums = defaultdict(lambda: [0, 0, 0, 0])

    with open(input_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            method = row["Method"]
            lval = row["LLM"]
            if method not in method_order:
                method_order.append(method)
            if lval not in l_order[method]:
                l_order[method].append(lval)

            key = (method, lval)
            sums[key][0] += int(row["Input Tokens"])
            sums[key][1] += int(row["Output Tokens"])
            sums[key][2] += int(row["Number of Calls"])
            sums[key][3] += 1

    with open(output_path, "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow([
            "Method",
            "LLM",
            "Average Input Tokens",
            "Average Output Tokens",
            "Average Number of Calls",
        ])

        for method in method_order:
            total_input = 0
            total_output = 0
            total_calls = 0
            total_count = 0

            for lval in l_order[method]:
                key = (method, lval)
                in_sum, out_sum, call_sum, count = sums[key]
                avg_in = in_sum / count
                avg_out = out_sum / count
                avg_calls = call_sum / count

                writer.writerow([
                    method,
                    lval,
                    format_value(avg_in),
                    format_value(avg_out),
                    format_value(avg_calls),
                ])

                total_input += in_sum
                total_output += out_sum
                total_calls += call_sum
                total_count += count

            if total_count:
                writer.writerow([
                    method,
                    "Average",
                    format_value(total_input / total_count, True),
                    format_value(total_output / total_count, True),
                    format_value(total_calls / total_count, True),
                ])

            writer.writerow([])


if __name__ == "__main__":
    main()

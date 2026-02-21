# Name:
# Student ID:
# Email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?

import csv


def read_data(filename):
    data = []
    with open(filename, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def calc_avg_profit_by_region(data):
    region_totals = {}
    region_counts = {}

    for row in data:
        sales = float(row["Sales"])
        profit = float(row["Profit"])
        region = row["Region"]

        if sales > 100:
            if region not in region_totals:
                region_totals[region] = 0
                region_counts[region] = 0

            region_totals[region] += profit
            region_counts[region] += 1

    averages = {}

    for region in region_totals:
        count = region_counts[region]
        if count > 0:
            averages[region] = region_totals[region] / count
        else:
            averages[region] = 0

    return averages


def main():
    data = read_data("SampleSuperstore.csv")

    avg_profit = calc_avg_profit_by_region(data)

    print("Average Profit by Region (Sales > 100):")
    print(avg_profit)


if __name__ == "__main__":
    main()
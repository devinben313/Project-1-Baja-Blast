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
import unittest


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


def calc_category_totals(data):
    category_totals = {}

    for row in data:
        if row["Ship Mode"] == "Standard Class":
            category = row["Category"]
            sales = float(row["Sales"])
            profit = float(row["Profit"])

            if category not in category_totals:
                category_totals[category] = [0, 0]

            category_totals[category][0] += sales
            category_totals[category][1] += profit

    return category_totals


def write_output(avg_profit, category_totals, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Average Profit by Region (Sales > 100)"])
        writer.writerow(["Region", "Average Profit"])

        for region in avg_profit:
            writer.writerow([region, avg_profit[region]])

        writer.writerow([])
        writer.writerow(["Category Totals (Standard Class Only)"])
        writer.writerow(["Category", "Total Sales", "Total Profit"])

        for category in category_totals:
            writer.writerow([
                category,
                category_totals[category][0],
                category_totals[category][1]
            ])


def main():
    data = read_data("SampleSuperstore.csv")

    avg_profit = calc_avg_profit_by_region(data)
    category_totals = calc_category_totals(data)

    write_output(avg_profit, category_totals, "output.csv")

    print("Results written to output.csv")


# -----------------------
# UNIT TESTS
# -----------------------

class TestProject1(unittest.TestCase):

    def test_avg_profit_normal(self):
        test_data = [
            {"Region": "West", "Sales": "200", "Profit": "50"},
            {"Region": "West", "Sales": "300", "Profit": "70"},
            {"Region": "East", "Sales": "150", "Profit": "30"}
        ]

        result = calc_avg_profit_by_region(test_data)

        self.assertAlmostEqual(result["West"], 60)
        self.assertAlmostEqual(result["East"], 30)

    def test_avg_profit_edge(self):
        test_data = [
            {"Region": "West", "Sales": "50", "Profit": "20"}
        ]

        result = calc_avg_profit_by_region(test_data)

        self.assertEqual(result, {})

    def test_category_totals_normal(self):
        test_data = [
            {"Category": "Furniture", "Ship Mode": "Standard Class", "Sales": "200", "Profit": "50"},
            {"Category": "Furniture", "Ship Mode": "Standard Class", "Sales": "300", "Profit": "70"},
            {"Category": "Technology", "Ship Mode": "Standard Class", "Sales": "150", "Profit": "30"}
        ]

        result = calc_category_totals(test_data)

        self.assertEqual(result["Furniture"][0], 500)
        self.assertEqual(result["Furniture"][1], 120)
        self.assertEqual(result["Technology"][0], 150)
        self.assertEqual(result["Technology"][1], 30)

    def test_category_totals_edge(self):
        test_data = [
            {"Category": "Furniture", "Ship Mode": "Second Class", "Sales": "200", "Profit": "50"}
        ]

        result = calc_category_totals(test_data)

        self.assertEqual(result, {})


if __name__ == "__main__":
    main()
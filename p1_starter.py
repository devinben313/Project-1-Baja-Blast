# Name:Devin Benson & Alyssa Davis
# Student ID:80095600 & 80936839
# Email: devinben@umich.edu & aljdavis@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Worked together as a team to write the code and unit tests, and used ChatGPT for debugging assistance and understanding Git workflow.
# If you worked with generative AI also add a statement for how you used it. Used ChatGPT for debugging assistance and understanding Git workflow.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?Use of GenAI aligned with my GenAI contract.
# Dataset used: superstore_subset.csv (derived from SampleSuperstore dataset)

import csv
import unittest


# -----------------------
# READ DATA
# -----------------------

def read_data(filename):
    data = []

    with open(filename, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data


# -----------------------
# DEVIN FUNCTIONS
# -----------------------

# Calculates average profit per category where Sales > 100
# Uses Category, Sales, Profit
def calc_avg_profit_by_category_high_sales(data):
    totals = {}
    counts = {}

    for row in data:
        if float(row["Sales"]) > 100:
            category = row["Category"]
            profit = float(row["Profit"])

            if category not in totals:
                totals[category] = 0
                counts[category] = 0

            totals[category] += profit
            counts[category] += 1

    averages = {}

    for category in totals:
        averages[category] = totals[category] / counts[category]

    return averages


# Calculates total sales per region where Ship Mode is Standard Class
# Uses Region, Ship Mode, Sales
def calc_total_sales_by_region_standard_ship(data):
    totals = {}

    for row in data:
        if row["Ship Mode"] == "Standard Class":
            region = row["Region"]
            sales = float(row["Sales"])

            if region not in totals:
                totals[region] = 0

            totals[region] += sales

    return totals


# -----------------------
# ALYSSA FUNCTIONS
# -----------------------

# Calculates average discount per category where Profit > 0
# Uses Category, Discount, Profit
def calc_avg_discount_by_category_profitable(data):
    totals = {}
    counts = {}

    for row in data:
        if float(row["Profit"]) > 0:
            category = row["Category"]
            discount = float(row["Discount"])

            if category not in totals:
                totals[category] = 0
                counts[category] = 0

            totals[category] += discount
            counts[category] += 1

    averages = {}

    for category in totals:
        averages[category] = totals[category] / counts[category]

    return averages


# Calculates total profit per region where Discount > 0.2
# Uses Region, Discount, Profit
def calc_total_profit_by_region_high_discount(data):
    totals = {}

    for row in data:
        if float(row["Discount"]) > 0.2:
            region = row["Region"]
            profit = float(row["Profit"])

            if region not in totals:
                totals[region] = 0

            totals[region] += profit

    return totals


# -----------------------
# WRITE OUTPUT
# -----------------------

def write_output(avg_profit_cat, total_sales_reg,
                 avg_discount_cat, total_profit_reg, filename):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Average Profit by Category (Sales > 100)"])
        for key in avg_profit_cat:
            writer.writerow([key, avg_profit_cat[key]])

        writer.writerow([])

        writer.writerow(["Total Sales by Region (Standard Class)"])
        for key in total_sales_reg:
            writer.writerow([key, total_sales_reg[key]])

        writer.writerow([])

        writer.writerow(["Average Discount by Category (Profit > 0)"])
        for key in avg_discount_cat:
            writer.writerow([key, avg_discount_cat[key]])

        writer.writerow([])

        writer.writerow(["Total Profit by Region (Discount > 0.2)"])
        for key in total_profit_reg:
            writer.writerow([key, total_profit_reg[key]])


# -----------------------
# MAIN
# -----------------------

def main():
    data = read_data("superstore_subset.csv")

    avg_profit_category = calc_avg_profit_by_category_high_sales(data)
    total_sales_region = calc_total_sales_by_region_standard_ship(data)
    avg_discount_category = calc_avg_discount_by_category_profitable(data)
    total_profit_region = calc_total_profit_by_region_high_discount(data)

    write_output(
        avg_profit_category,
        total_sales_region,
        avg_discount_category,
        total_profit_region,
        "output.csv"
    )

    print("Results written to output.csv")


# -----------------------
# UNIT TESTS
# -----------------------

class TestProject1(unittest.TestCase):

    def test_avg_profit_by_category(self):
        test_data = [
            {"Category": "Furniture", "Sales": "200", "Profit": "50"},
            {"Category": "Furniture", "Sales": "300", "Profit": "70"},
            {"Category": "Technology", "Sales": "50", "Profit": "30"}
        ]

        result = calc_avg_profit_by_category_high_sales(test_data)

        self.assertAlmostEqual(result["Furniture"], 60)
        self.assertNotIn("Technology", result)

    def test_total_sales_by_region(self):
        test_data = [
            {"Region": "West", "Ship Mode": "Standard Class", "Sales": "200"},
            {"Region": "West", "Ship Mode": "Second Class", "Sales": "100"},
            {"Region": "East", "Ship Mode": "Standard Class", "Sales": "300"}
        ]

        result = calc_total_sales_by_region_standard_ship(test_data)

        self.assertEqual(result["West"], 200)
        self.assertEqual(result["East"], 300)

    def test_avg_discount_by_category(self):
        test_data = [
            {"Category": "Furniture", "Discount": "0.1", "Profit": "50"},
            {"Category": "Furniture", "Discount": "0.2", "Profit": "60"},
            {"Category": "Technology", "Discount": "0.3", "Profit": "-10"}
        ]

        result = calc_avg_discount_by_category_profitable(test_data)

        self.assertAlmostEqual(result["Furniture"], 0.15)
        self.assertNotIn("Technology", result)

    def test_total_profit_by_region(self):
        test_data = [
            {"Region": "West", "Discount": "0.3", "Profit": "50"},
            {"Region": "West", "Discount": "0.1", "Profit": "30"},
            {"Region": "East", "Discount": "0.25", "Profit": "40"}
        ]

        result = calc_total_profit_by_region_high_discount(test_data)

        self.assertEqual(result["West"], 50)
        self.assertEqual(result["East"], 40)


if __name__ == "__main__":
    main()
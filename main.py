import csv
import os


DATA_PATH = "data"

OUTPUT_FILE = "ping_morsel_sales.csv"

FILES = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv",
]


rows_out = []


for filename in FILES:
    with open(os.path.join(DATA_PATH, filename), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["product"] != "pink morsel":
                continue
            

            price = float(row["price"].replace("$", ""))
            quantity = int(row["quantity"])
            sales = price * quantity

            rows_out.append({
                "sales": sales,
                "date": row["date"],
                "region": row["region"],
            })




with open(OUTPUT_FILE, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=["sales", "date", "region"])
    writer.writeheader()
    writer.writerows(rows_out)



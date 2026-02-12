import pandas as pd

def main():
    # Load the three CSV files
    files = [
        "data/daily_sales_data_0.csv",
        "data/daily_sales_data_1.csv",
        "data/daily_sales_data_2.csv",
    ]

    # Read each CSV into a table (DataFrame)
    tables = []
    for f in files:
        tables.append(pd.read_csv(f))

    # Combine (stack) the three tables into one
    df = pd.concat(tables, ignore_index=True)

    # Keep only rows where product is pink morsels
    df = df[df["product"] == "pink morsels"].copy()

    # Create sales = quantity * price
    df["sales"] = df["quantity"] * df["price"]

    # Keep only sales, date, region
    out = df[["sales", "date", "region"]].copy()

    # Rename columns to match the required output fields
    out.columns = ["Sales", "Date", "Region"]

    # Save the final output file in the repo root
    out.to_csv("formatted_sales.csv", index=False)

    print("Done! Created formatted_sales.csv")

if __name__ == "__main__":
    main()

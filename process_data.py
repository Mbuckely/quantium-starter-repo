import pandas as pd

def main():
    files = [
        "data/daily_sales_data_0.csv",
        "data/daily_sales_data_1.csv",
        "data/daily_sales_data_2.csv",
    ]

    dfs = [pd.read_csv(f) for f in files]
    df = pd.concat(dfs, ignore_index=True)

    # Clean fields (strip spaces)
    df["product"] = df["product"].astype(str).str.strip()
    df["region"] = df["region"].astype(str).str.strip()

    # Keep only pink morsel (singular in your data)
    df = df[df["product"] == "pink morsel"].copy()

    # Convert price from "$3.00" -> 3.00
    df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)

    # Ensure quantity is numeric
    df["quantity"] = df["quantity"].astype(int)

    # Compute sales
    df["sales"] = df["quantity"] * df["price"]

    # Output only required columns
    out = df[["sales", "date", "region"]].copy()
    out.columns = ["Sales", "Date", "Region"]

    # Put regions in a custom order, then sort
    region_order = ["north", "south", "east", "west"]
    out["Region"] = out["Region"].astype(str).str.strip()
    out["Region"] = pd.Categorical(out["Region"], categories=region_order, ordered=True)

    # Sort by Region first (custom order), then by Date
    out = out.sort_values(["Region", "Date"])

    out.to_csv("formatted_sales.csv", index=False)
    print(f"Done! Wrote {len(out)} rows to formatted_sales.csv")

if __name__ == "__main__":
    main()

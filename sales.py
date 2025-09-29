# CSV Data Analysis Script

# Step 1: Import minimal libraries first
import sys

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    print("Pandas or Matplotlib not installed. Install them with:")
    print("pip install pandas matplotlib")
    sys.exit(1)

# Step 2: Create sample CSV data
data = {
    "Date": ["2025-09-01", "2025-09-01", "2025-09-02", "2025-09-02", "2025-09-03", "2025-09-03"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Region": ["North", "South", "North", "South", "East", "West"],
    "Sales": [100, 150, 120, 130, 90, 110]
}

df = pd.DataFrame(data)

# Step 3: Save CSV file
csv_file = "sales.csv"
df.to_csv(csv_file, index=False)
print(f"Sample CSV '{csv_file}' created successfully!\n")

# Step 4: Load CSV
df = pd.read_csv(csv_file)
print("First 5 rows of the data:")
print(df.head(), "\n")

# Step 5: Basic summary statistics
print("Summary statistics:")
print(df.describe(), "\n")

# Step 6: Total sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("Total sales by product:")
print(sales_by_product, "\n")

# Step 7: Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("Total sales by region:")
print(sales_by_region, "\n")

# Step 8: Plot total sales by product (bar chart)
plt.figure(figsize=(6,4))
sales_by_product.plot(kind="bar", color="skyblue", title="Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Step 9: Plot total sales by region (pie chart)
plt.figure(figsize=(6,6))
sales_by_region.plot(kind="pie", autopct="%1.1f%%", startangle=90, title="Total Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

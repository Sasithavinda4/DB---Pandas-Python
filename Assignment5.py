import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset

data = {
    "Date": ["2024-05-01", "2024-10-25", "2024-12-08", "2024-12-08"],
    "Product": ["Laptop", "Mobile", "Headphones", "Tabs"],
    "Units Sold": [23, 45, 67, 34],
    "Revenue": [20000, 40000, 30000, 40000],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories"]
}
table = pd.DataFrame(data)
table.to_csv("sales_data.csv", index=False)

df = pd.read_csv("sales_data.csv")

print("Initial DataFrame:")
print(df)
print("\nChecking for missing values...")
print(df.isna().sum())
df = df.dropna()

df["Date"] = pd.to_datetime(df["Date"])

df = df[(df["Units Sold"] >= 0) & (df["Revenue"] >= 0)]

# Data Analysis

revenue_by_product = df.groupby("Product")["Revenue"].sum()
average_units_sold = df.groupby("Product")["Units Sold"].mean()

highest_revenue_product = revenue_by_product.idxmax()
highest_units_sold_product = df.groupby("Product")["Units Sold"].sum().idxmax()

print("\nTotal Revenue by Product:")
print(revenue_by_product)
print("\nAverage Units Sold by Product:")
print(average_units_sold)
print(f"\nProduct with Highest Revenue: {highest_revenue_product}")
print(f"Product with Highest Units Sold: {highest_units_sold_product}")

# Data Visualization

# Bar chart
plt.bar(revenue_by_product.index, revenue_by_product.values, color='skyblue')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# Line plot
revenue_trend = df.groupby("Date")["Revenue"].sum()
plt.plot(revenue_trend.index, revenue_trend.values, marker='o', linestyle='-', color='green')
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# Pie chart
revenue_by_category = df.groupby("Category")["Revenue"].sum()
plt.pie(revenue_by_category.values, labels=revenue_by_category.index, autopct='%1.1f%%', startangle=140)
plt.title("Revenue Distribution by Category")
plt.show()

# Calculate growth rate of revenue
df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby(["Month", "Product"])["Revenue"].sum().unstack()

# Calculate the growth rate
growth_rate = (monthly_revenue.iloc[-1] - monthly_revenue.iloc[0]) / monthly_revenue.iloc[0] * 100
highest_growth_rate_product = growth_rate.idxmax()

print("\nGrowth Rate of Revenue by Product:")
print(growth_rate)

# Display the product with the highest growth rate

print(f"Product with Highest Growth Rate: {highest_growth_rate_product}")

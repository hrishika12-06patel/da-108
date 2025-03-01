import pandas as pd
import matplotlib.pyplot as plt

# Part 1: Data Handling with Pandas

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("sales_data_india.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Handle missing values (if any) by filling or removing them
df.fillna(method='ffill', inplace=True)

# Part 2: Implementing OOP Concepts

class SalesDataProcessor:
    def __init__(self, df):
        self.df = df

    def load_data(self, file_path):
        self.df = pd.read_csv(file_path)

    def clean_data(self):
        self.df.fillna(method='ffill', inplace=True)

    def get_total_sales(self):
        return self.df['TotalPrice'].sum()

    def get_unique_products(self):
        return self.df['Product'].unique().tolist()

    def get_sales_by_category(self):
        return self.df.groupby('Category')['TotalPrice'].sum()

    def get_top_selling_product(self):
        return self.df.groupby('Product')['TotalPrice'].sum().idxmax()

# Testing SalesDataProcessor
processor = SalesDataProcessor(df)
print("\nTotal Sales:", processor.get_total_sales())
print("Unique Products:", processor.get_unique_products())
print("Sales by Category:")
print(processor.get_sales_by_category())
print("Top Selling Product:", processor.get_top_selling_product())

# Part 3: Extending OOP with Inheritance

class CustomerSalesProcessor(SalesDataProcessor):
    def get_total_sales_by_customer(self, customer_id):
        return self.df[self.df['CustomerID'] == customer_id]['TotalPrice'].sum()

    def get_frequent_customers(self, n):
        return self.df['CustomerID'].value_counts().head(n)

    def get_sales_by_city(self):
        return self.df.groupby('City')['TotalPrice'].sum()

# Testing CustomerSalesProcessor
customer_processor = CustomerSalesProcessor(df)
print("\nTotal Sales by Customer (C001):", customer_processor.get_total_sales_by_customer('C001'))
print("Frequent Customers (Top 3):")
print(customer_processor.get_frequent_customers(3))
print("Sales by City:")
print(customer_processor.get_sales_by_city())

# Part 4: Data Visualization

# Plot a bar chart showing total sales by category
category_sales = processor.get_sales_by_category()
category_sales.plot(kind='bar', title='Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

# Plot a line graph of daily sales trends
daily_sales = df.groupby('Date')['TotalPrice'].sum()
daily_sales.plot(kind='line', title='Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Plot a pie chart showing the percentage contribution of different cities to total sales
city_sales = customer_processor.get_sales_by_city()
city_sales.plot(kind='pie', title='Total Sales by City', autopct='%1.1f%%')
plt.ylabel('')
plt.show()
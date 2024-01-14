# Attempt to load the dataset with a different encoding
try:
    superstore_data = pd.read_csv(file_path, encoding='ISO-8859-1')
except Exception as e:
    # If it still fails, print the error
    error_message = str(e)
    superstore_data = None
    error_message

# If successful, display the first few rows of the dataset
if superstore_data is not None:
    superstore_data.head()


# Exploring the dataset
data_overview = {
    "Data Shape": superstore_data.shape,
    "Data Types": superstore_data.dtypes,
    "Missing Values": superstore_data.isnull().sum(),
    "Sample Data": superstore_data.head()
}

data_overview["Sample Data"]

# Data Cleaning: Checking for missing values and data inconsistencies

# Summary of missing values in each column
missing_values = superstore_data.isnull().sum()

# Checking for any duplicate rows
duplicate_rows = superstore_data.duplicated().sum()

# Data types of each column for consistency
column_data_types = superstore_data.dtypes

# Summary of missing values, duplicate rows, and data types
data_cleaning_summary = {
    "Missing Values": missing_values,
    "Duplicate Rows": duplicate_rows,
    "Column Data Types": column_data_types
}

data_cleaning_summary

import matplotlib.pyplot as plt
import seaborn as sns

# Converting 'Order Date' and 'Ship Date' to datetime format
superstore_data['Order Date'] = pd.to_datetime(superstore_data['Order Date'])
superstore_data['Ship Date'] = pd.to_datetime(superstore_data['Ship Date'])

# Analyzing the impact of Discounts on Sales and Profit
discount_impact = superstore_data.groupby('Discount').agg({'Sales': 'mean', 'Profit': 'mean'}).reset_index()

# Visualizing the impact of Discounts on Sales and Profit
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.lineplot(data=discount_impact, x='Discount', y='Sales')
plt.title('Impact of Discount on Sales')

plt.subplot(1, 2, 2)
sns.lineplot(data=discount_impact, x='Discount', y='Profit')
plt.title('Impact of Discount on Profit')

plt.tight_layout()
plt.show()

# Summary of the analysis
discount_impact_summary = discount_impact.describe()
discount_impact_summary

# Analyzing Sales and Profit by Category and Sub-Category
category_analysis = superstore_data.groupby(['Category', 'Sub-Category']).agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Visualizing Sales and Profit by Category and Sub-Category
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(data=category_analysis, x='Sales', y='Sub-Category', hue='Category')
plt.title('Sales by Category and Sub-Category')

plt.subplot(1, 2, 2)
sns.barplot(data=category_analysis, x='Profit', y='Sub-Category', hue='Category')
plt.title('Profit by Category and Sub-Category')

plt.tight_layout()
plt.show()

# Summary of Category and Sub-Category Analysis
category_analysis_summary = category_analysis.describe()
category_analysis_summary


# Creating a year and month column for temporal analysis
superstore_data['Year'] = superstore_data['Order Date'].dt.year
superstore_data['Month'] = superstore_data['Order Date'].dt.month

# Temporal Analysis: Monthly and Yearly Trends in Sales
monthly_sales = superstore_data.groupby(['Year', 'Month']).agg({'Sales': 'sum'}).reset_index()

# Visualizing Monthly Sales Trends
plt.figure(figsize=(14, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend(title='Year')
plt.show()

# Yearly Sales Summary
yearly_sales_summary = monthly_sales.groupby('Year').agg({'Sales': 'sum'})
yearly_sales_summary

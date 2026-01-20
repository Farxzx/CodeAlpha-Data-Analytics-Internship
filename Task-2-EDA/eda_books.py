import pandas as pd

# Load dataset
df = pd.read_csv("books_data.csv")

# Basic info
print("Dataset Info:")
print(df.info())

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Convert Price to numeric
df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)


# Rating count
rating_count = df["Rating"].value_counts()
print("\nRating Distribution:")
print(rating_count)

# Average price
avg_price = df["Price"].mean()
print("\nAverage Book Price:", avg_price)

# Most expensive book
max_price = df["Price"].max()
print("\nMost Expensive Book Price:", max_price)

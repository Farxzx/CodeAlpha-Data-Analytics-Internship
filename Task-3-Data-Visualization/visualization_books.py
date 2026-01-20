import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("books_data.csv")

# Clean price column
df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# 1. Rating distribution bar chart
rating_counts = df["Rating"].value_counts()

plt.figure()
rating_counts.plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.show()

# 2. Price distribution histogram
plt.figure()
plt.hist(df["Price"], bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.show()

import numpy as np 
import pandas as pd 


data =pd.read_csv("./data/amazon.csv")


#Data set Shape
print(f"Data set shape",data.shape)
print(f"Shape of the row -{data.shape[0]}")
print(f"Shape of the column -{data.shape[1]}")


#  Columns validated

print(data.columns)


#  Missing values identified

missing_value=data.isnull().sum()
print(missing_value)

missing_value_rating=data["rating_count"].isnull().sum()
print("The missing values in rating_count",missing_value_rating)


data["rating_count"] = (
    data["rating_count"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

data["rating_count"] = pd.to_numeric(
    data["rating_count"],
    errors="coerce"
)
data["rating_count"] = data["rating_count"].fillna(
    data["rating_count"].median()
)
print("The missing values in rating_count after fillna",data["rating_count"].isnull().sum())


# info

print(data.info())
print(data.describe())


#-----------------------------------------------
# Check duplicate records

duplicate = data["product_id"].duplicated().sum()
print("Number of duplicate records",duplicate)

# Remove duplicate records
print(data.duplicated().sum())

df=data[~data.duplicated(subset=["product_id"], keep="first")]


# Convert discounted_price to numeric
df["discounted_price"] = (
    df["discounted_price"].astype(str)
    .str.replace("₹","",regex=False)
    .str.replace(",","",regex=False)
    .str.strip()
)
df["discounded_price"]=pd.to_numeric(df["discounted_price"], errors="coerce")

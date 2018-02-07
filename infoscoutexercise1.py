import pandas as pd



def retailer_affinity(focus_brand):

    transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")
    transactions["Parent Brand"] == focus_brand

    transactions = transactions.head(15)
    transactions['Item Dollars'] = transactions['Item Dollars'].str.replace('$', '')
    transactions['Item Dollars'] = transactions['Item Dollars'].astype(float)

    transactions["Total"] = transactions["Item Dollars"] * transactions["Item Units"]
    transactions_by_brand_and_retailer = transactions.groupby(["Parent Brand", "Retailer"])["Total"].sum()
    # return transactions_by_brand_and_retailer
    total_sales_per_retailer = transactions.groupby(["Retailer"])["Total"].sum()
    # return total_sales_per_retailer
    return (transactions_by_brand_and_retailer/total_sales_per_retailer)[focus_brand].idxmax()



print retailer_affinity("Rockstar")
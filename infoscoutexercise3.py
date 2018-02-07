import pandas as pd



def top_buying_brand():

    transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")
    transactions['Item Dollars'] = transactions['Item Dollars'].str.replace('$', '')
    transactions['Item Dollars'] = transactions['Item Dollars'].astype(float)

    transactions["Total"] = transactions["Item Dollars"] * transactions["Item Units"]
    transactions.head()

    total_amount_by_household = transactions.groupby(["Parent Brand","User ID"])["Total"].sum()
    brand = total_amount_by_household.idxmax()[0]
    return brand


print top_buying_brand()
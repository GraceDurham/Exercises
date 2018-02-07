import pandas as pd

transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")

def retailer_affinity(focus_brand, transactions):

    # transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")
    transactions["Parent Brand"] == focus_brand

    # transactions = transactions.head(15)
    transactions['Item Dollars'] = transactions['Item Dollars'].str.replace('$', '')
    transactions['Item Dollars'] = transactions['Item Dollars'].astype(float)

    transactions["Total"] = transactions["Item Dollars"] * transactions["Item Units"]
    transactions_by_brand_and_retailer = transactions.groupby(["Parent Brand", "Retailer"])["Total"].sum()
    # return transactions_by_brand_and_retailer
    total_sales_per_retailer = transactions.groupby(["Retailer"])["Total"].sum()
    # return total_sales_per_retailer
    return (transactions_by_brand_and_retailer/total_sales_per_retailer)[focus_brand].idxmax()

  
def menu(transactions):
    while True:
        # print("\nRockstar")
        # print("Monster")
        # print("5 Hour Energy")
        # print("Red Bull")

        unique_brands = transactions["Parent Brand"].unique()
        print "\n"
        print "\n".join(unique_brands)
        print ( "q to quit the program.\n")

        brand = raw_input("\nPlease pick one of the brands from the menu options: Rockstar, Monster, 5 Hour Energy, Red Bull, or q.\n")

        if brand in unique_brands:
            print "Your answer is: "
            print retailer_affinity(brand, transactions) 
            print "\n"
            break
        elif brand == "q":
            break       
        else :
            print "Please re run this program and re input one of the selections again.\n"
            


menu(transactions)

        





# print retailer_affinity(brand, transactions)
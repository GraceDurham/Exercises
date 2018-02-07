import pandas as pd
from datetime import datetime


transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")

def count_hhs(brand, retailer, start_date, end_date, transactions):

    query = 1


    transactions['Date'] = pd.to_datetime(transactions.Date)
    transactions["Date"]
    
  
    if(brand == None and retailer == None and start_date == None and end_date == None):
        return transactions


    if (brand != None):
        query = 1 and (transactions["Parent Brand"] == brand)
    
    if (retailer != None):
        query =  query & (transactions["Retailer"] == retailer) 


    if (start_date!= None):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        query = query & (transactions['Date'] > start_date) 
        
    
    if (end_date!= None):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        query = query & (transactions['Date'] < end_date)
    

    
    filtered_transactions = transactions[query]
    unique = filtered_transactions["User ID"].unique()
    count_hh_= len(unique)
    return count_hh_


print count_hhs("5 Hour Energy","Walmart", None, "2017-12-12", transactions)
# def menu(transactions):
#     while True:
        
#         unique_brands = transactions["Parent Brand"].unique()
#         print "\n"
#         print "\n".join(unique_brands)
#         print None
#         print ( "q to quit the program.\n")

#         brand = raw_input("\nPlease pick one of the brands from the menu options: Rockstar, Monster, 5 Hour Energy, Red Bull, or q.\n")

#         unique_retailers = transactions["Retailer"].unique()

#         print "\n"
#         print "\n".join(unique_retailers)
#         print None
#         print ( "q to quit the program.\n")

#         retailer = raw_input("\nPlease pick one of the Retailers from the menu options: Walmart, Walgreens, Kroger, CVS, Publix, Costco, Target, Safeway, None, or q.\n")


#         if brand in unique_brands or None and retailer in unique_retailers or None:
#             print "Your answer is: "
#             print count_hhs(brand, retailer, "2014-6-1", "2017-4-1", transactions)
#             print "\n"
#             break
#         elif brand == "q":
#             break       
#         else :
#             print "Please re run this program and re input one of the selections again.\n"
            


# menu(transactions)












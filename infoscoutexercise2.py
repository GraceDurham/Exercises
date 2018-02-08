import pandas as pd
from datetime import datetime


transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")

def count_hhs(brand, retailer, start_date, end_date):

    query = 1


    transactions['Date'] = pd.to_datetime(transactions.Date)
    transactions["Date"]
    
  
    if(brand == "" and retailer == "" and start_date == "" and end_date == ""):
        return transactions


    if (brand != ""):
        query = 1 and (transactions["Parent Brand"] == brand)
    
    if (retailer != ""):
        query =  query & (transactions["Retailer"] == retailer) 


    if (start_date!= ""):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        query = query & (transactions['Date'] > start_date) 
        
    
    if (end_date!= ""):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        query = query & (transactions['Date'] < end_date)
    

    
    filtered_transactions = transactions[query]
    unique = filtered_transactions["User ID"].unique()
    count_hh_= len(unique)
    return count_hh_

def is_valid_date(str_date):
    if(str_date == ""):
        return True
    try:
        datetime.strptime(str_date, '%Y-%m-%d')
        return True
    except:
        return False

def menu():
    unique_brands = transactions["Parent Brand"].unique()
    brand_list = "\n".join(unique_brands)

    brand = raw_input("\nPlease pick one of the brands from the options below or press enter to skip.\n" + brand_list + "\n").strip()


    if brand != "" and brand not in unique_brands:
        brand = ""
        print "Warning invalid brand.  Ignoring it."

    unique_retailers = transactions["Retailer"].unique()
    retailer_list = "\n".join(unique_retailers)        
    retailer = raw_input("\nPlease pick one of the retailers from the options below or press enter to skip.\n" + retailer_list + "\n").strip()

    if retailer != "" and retailer not in unique_retailers:
        retailer = ""
        print "Warning invalid retailer.  Ignoring it."

    dates = transactions["Date"]

    start_date = raw_input("\nPlease input either an start date in this format year-month-day ex. 2014-6-1 or press enter to skip.\n").strip()
    
    if(is_valid_date(start_date) == False):
        start_date = ""
        print "Invalid date.  Ignoring."

    end_date = raw_input("\nPlease input either an end date in this format year-month-day ex. 2018-2-7 or press enter to skip.\n").strip()

    if(is_valid_date(end_date) == False):
        end_date = ""
        print "Invalid date.  Ignoring."

    print "\nCalculating your answer..."
    print count_hhs(brand, retailer, start_date, end_date)
    print "\n"

    
            


menu()












import pandas as pd
from datetime import datetime



def count_hhs(brand, retailer, start_date, end_date):

    transactions = pd.read_csv("https://s3.amazonaws.com/isc-isc/trips_gdrive.csv")
    transactions['Date'] = pd.to_datetime(transactions.Date)
    transactions["Date"]
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
   
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    
    
    if(brand == None and retailer == None and start_date == None and end_date == None):
        return transactions

    # # query = 1

    if(brand != None and retailer != None and start_date != None and end_date != None):
        # filtered_transactions = transactions[1 and (transactions["Parent Brand"] == brand) & (transactions["Retailer"] == retailer) & (transactions["Date"] > start_date) & (transactions["Date"] < end_date)]
        filtered_transactions = transactions[1 and (transactions["Parent Brand"] == brand) & (transactions["Retailer"] == retailer) & (transactions["Date"] > start_date) & (transactions['Date']< end_date)]
        unique = filtered_transactions["User ID"].unique()
        count_hh_costco_monster = len(unique)
        return count_hh_costco_monster


    # if(retailer != None):
    #     query = transactions[query & (transactions["Retailer"] == retailer)]

    # return transactions[query]

    # filtered_transactions = transactions[1 & (transactions["Parent Brand"] == "Monster") & (transactions["Retailer"] == "Costco")]


print count_hhs("Red Bull", "Costco", "2014-6-1", "2017-4-1")










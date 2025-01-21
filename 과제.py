import requests
import pandas as pd
import numpy as np

headers = {
    'accept': 'application/json',
    'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDA1NzE1OTgifQ.bP7GvgsnchBkT3mKmxF3zw4M4-7CWV5zLTpMBU2NMRvzhHzkIkZW_ayEb0VZ5qi8hWIBGchm9jJGyrzgz1N7UK3ZJ_nlK9wR_Jl1f7wOSjEFUNOXm5X4u-IUcxcC7OsaWhgsQBhZ18OzkxI0vTyq0qW-dcZ1EKbS7sn_Pi6MnVGMApAhX-b9-H8dxKoNUjLKIhWEjkTM2dhR869pChEK_-VoEHwFk-Tsmdd8B_oWCUG33Z4foSQqS0Q8Igh8mHgLFVEX8lvDg9ynB7QFE8LbFYr7REXMCXG2lg9_AWIMQgzmvUDM7nlkXSwoMWi4UZWaqxCJ0AbjHwKaDSjOLRFfWA'
}
url = 'https://developer-lostark.game.onstove.com/auctions/items'
data1 = {"ItemName": "10레벨 겁화", "Sort": "BUY_PRICE", "CategoryCode": 210000}
data2 = {"ItemName": "10레벨 작열", "Sort": "BUY_PRICE", "CategoryCode": 210000}
data3 = {"ItemName": "9레벨 작열", "Sort": "BUY_PRICE", "CategoryCode": 210000}


def jewel(df):
    response = requests.post(url, headers=headers, json=df)
    response_data = response.json()
    items = response_data.get("Items", [])
    
    data_jewel = []
    
    for item in items:
        data_jewel_a = {
            "아이템명": item.get("Name", "Unknown"),
            "가격": item.get("AuctionInfo", {}).get("BuyPrice")
        }
        data_jewel.append(data_jewel_a)
    return pd.DataFrame(data_jewel)
   
df1 = jewel(data1)
df2 = jewel(data2)
df3 = jewel(data3)

겁화작열_df = pd.concat([df1, df2], axis=1)
합성_df = df3

price_df1 = df1['가격'].min()  
price_df2 = df2['가격'].min() 

합성_df['합성 성공'] = ((price_df1 / 3)*0.95 - 합성_df['가격']).astype(int) 
합성_df['합성 실패'] = ((price_df2 / 3)*0.95 - 합성_df['가격']).astype(int)


display(겁화작열_df)
display(합성_df)

import requests
def main():
    year = 2021
    isFirstIteration = True
    for i in range(1, 3):
        url = "https://aemo.com.au/aemo/data/nem/priceanddemand/PRICE_AND_DEMAND_{}{}_{}.csv".format("2021", str(i).zfill(2), "NSW1")
        print(url)
        
        
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36", 
            "Origin": "https://www.aemo.com.au",
            "Content-Type": "application/json",
            "Host": "www.aemo.com.au",
            "Origin": "https://www.aemo.com.au",
            #"Referer": "https://aemo.com.au/en/energy-systems/electricity/national-electricity-market-nem/data-nem/data-dashboard-nem",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            #"Cookie": " _fbp=fb.2.1622093470156.2066380736; _ga=GA1.3.986617177.1622093470; _gid=GA1.3.2087383874.1622093470; sxa_site=Corporate; SC_ANALYTICS_GLOBAL_COOKIE=e84a7a53140f48a79ded10be155e89c8|True; _gat_UA-20369317-1=1; ASP.NET_SessionId=zmidmmwjv4ytjjighhe2plif; __RequestVerificationToken=rop7y3Rz8bbgLL6vHdCZaghkKY0z5nn1e_mvLpTKkoaMLTivLlVlz5qpJ0qk-4QU5dHoecA0qyim2BNbpYSZwnCvpdvktzHLMQqTdJrjYj01; corporate#lang=en"
        }
        import csv
        session = requests.Session()
        session.headers = header
        req = session.get(url)
        url_content = req.content
        if(isFirstIteration):
            isFirstIteration = False
            csv_file = open('aemo2021.csv', 'wb')
            csv_file.write(url_content)
        else:
            temp_csv = open('temp.csv', 'wb')
            temp_csv.write(url_content)
            temp_csv.close()
            
            temp_csv = open("temp.csv",'r')
            next(temp_csv)
            csv_file = open('aemo2021.csv', 'a')
            for line in temp_csv:
                csv_file.write(line)
        csv_file.close()

main()


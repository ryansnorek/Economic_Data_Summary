from bs4 import BeautifulSoup as bs
import requests

# Source links
investorSentiment = 'https://ycharts.com/indicators/us_investor_sentiment_bull_bear_spread'
cashAllocation = 'https://ycharts.com/indicators/aaii_cash_allocation'
usInflation = 'https://ycharts.com/indicators/us_inflation_rate'
japanInflation = 'https://ycharts.com/indicators/japan_inflation_rate'
ukInflation = 'https://ycharts.com/indicators/uk_inflation_rate'
chinaInflation = 'https://ycharts.com/indicators/china_inflation_rate'
realDollarIndex = 'https://ycharts.com/indicators/real_trade_weighted_us_dollar_index_broad_goods_and_services'
velocityM2 = 'https://ycharts.com/indicators/velocity_of_us_m2_money_stock'
m2supply = 'https://ycharts.com/indicators/us_m2_money_stock'

# Ask user for selection and return the source link
def htmlSource():
    print("")
    print("1. US Investor Sentiment %")
    print("2. Cash Allocation")
    print("3. US Inflation")
    print("4. Japan Inflation")
    print("5. UK Inflation")
    print("6. China Inflation")
    print("7. Real Dollar Index")
    print("8. Velocity of M2 Money")
    print("9. M2 Money Supply")
    print("")
    selection = input("Enter a number from the list: ")
    
    if selection == '1':
        link = investorSentiment
    elif selection == '2':
        link = cashAllocation
    elif selection == '3':
        link = usInflation
    elif selection == '4':
        link = japanInflation
    elif selection == '5':
        link = ukInflation
    elif selection == '6':
        link = chinaInflation
    elif selection == '7':
        link = realDollarIndex
    elif selection == '8':
        link = velocityM2
    elif selection == '9':
        link = m2supply
    return link

# Pull the data from the selected link and print summary
def dataFromSource(source):
    html = requests.get(source).text
    soup = bs(html,'html.parser')
    statsArray = []
    stats = soup.find_all('tbody')

    for stat in stats:
        statElement = stat.find_all('td')

        for elem in statElement:
            statsArray.append(elem.text)

    summary = statsArray[0]    
    dates = statsArray[11:15] 
    print(summary) 
    return dates

# Print the date/time stamps and option to rerun program
def printDates(data):
    for d in data:
        print(d)

    print("")
    inp = input("Run program again? y/n ")
    if inp == 'y':
        printDates( dataFromSource ( htmlSource() ))   

# Run program
printDates( dataFromSource ( htmlSource() ))   






from bs4 import BeautifulSoup as bs
import requests

# Contains all the URL links required to run the program
from ycharts import *

# Subset of selections that can print everything or returns URL link
def inflation():
    print('\n0. PRINT ALL')
    print('\n1. US Consumer Prices')
    print('2. US Inflation Rate')
    print('3. US M2 Money Supply')
    print('4. US M2 Money Velocity')
    print('5. Japan Inflation')
    print('6. UK Inflation')
    print('7. China Inflation')
    print('8. China M2 Money Supply')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 8:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
      printAll(inflationURLs)
      return exit()

    elif selection == 1:
        link = inflationURLs['usCPI']
    elif selection == 2:
        link = inflationURLs['us']
    elif selection == 3:
        link = inflationURLs['usM2money']
    elif selection == 4:
        link = inflationURLs['usM2Velocity']
    elif selection == 5:
        link = inflationURLs['japan']
    elif selection == 6:
        link = inflationURLs['uk']
    elif selection == 7:
        link = inflationURLs['china']
    elif selection == 8:
        link = inflationURLs['chinaM2supply']

    return link
def sentiment():
    print('\n0. PRINT ALL')
    print('\n1. US Investor Sentiment')
    print('2. US Consumer Sentiment')
    print('3. Cash Allocation')
    print('4. Bond Allocation')
    print('5. Stock Allocation')
    print('6. EU Consumer Confidence')
    print('7. EU Economic Sentiment')
    print('8. Japan Consumer Confidence')
    print('9. UK Economic Sentiment')
    print('10. US Unemployment Rate')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 10:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
        printAll(sentimentURLs)
        return exit()

    if selection == 1:
        link = sentimentURLs['usInvestor']
    elif selection == 2:
        link = sentimentURLs['usConsumer']
    elif selection == 3:
        link = sentimentURLs['cash']
    elif selection == 4:
        link = sentimentURLs['bonds']
    elif selection == 5:
        link = sentimentURLs['stocks']
    elif selection == 6:
        link = sentimentURLs['euInvestor']
    elif selection == 7:
        link = sentimentURLs['eu']
    elif selection == 8:
        link = sentimentURLs['japanConsumer']
    elif selection == 9:
        link = sentimentURLs['uk']
    elif selection == 10:
        link = sentimentURLs['usUnemployment']

    return link
def monetary():
    print('\n0. PRINT ALL')
    print('\n1. Real Dollar Index')
    print('2. M1 Money Supply')
    print('3. M1 Money Velocity')
    print('4. US Bank Loans: Commercial')
    print('5. US Bank Loans: Credit Card')
    print('6. US GDP')
    print('7. UK GDP')
    print('8. Sweden GDP')
    print('9. Netherlands GDP')
    print('10. EU GDP')
    print('11. China GDP')
    print('12. World GDP')
    print('13. US Public Debt')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 13:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
        printAll(monetaryURLs)
        return exit()

    if selection == 1:
        link = monetaryURLs['realDollar']
    elif selection == 2:
        link = monetaryURLs['m1Supply']
    elif selection == 3:
        link = monetaryURLs['m1Velocity']
    elif selection == 4:
        link = monetaryURLs['usLoansCommercial']
    elif selection == 5:
        link = monetaryURLs['usLoansCC']
    elif selection == 6:
        link = monetaryURLs['usGDP']
    elif selection == 7:
        link = monetaryURLs['ukGDP']
    elif selection == 8:
        link = monetaryURLs['swedenGDP']
    elif selection == 9:
        link = monetaryURLs['netherGDP']
    elif selection == 10:
        link = monetaryURLs['euGDP']
    elif selection == 11:
        link = monetaryURLs['chinaGDP']
    elif selection == 12:
        link = monetaryURLs['worldGDP']
    elif selection == 13:
        link = monetaryURLs['usDebt']

    return link
def energy():
    print('\n0. PRINT ALL')
    print('\n1. US Energy Consumption')
    print('2. US Wind Production')
    print('3. US Solar Production')
    print('4. US Natural Gas Production')
    print('5. US Nuclear Electric Production')
    print('6. US Oil Production')
    print('7. US Oil Imports')
    print('8. Iran Oil Production')
    print('9. OPEC Oil Production')
    print('10. Saudi Arabia Oil Production')
    print('11. World Oil Production')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 11:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
        printAll(energyURLs)
        return exit()

    elif selection == 1:
        link = monetaryURLs['usEnergyConsumption']
    elif selection == 2:
        link = monetaryURLs['usWindProduction']
    elif selection == 3:
        link = monetaryURLs['usSolarProduction']
    elif selection == 4:
        link = monetaryURLs['usNGProduction']
    elif selection == 5:
        link = monetaryURLs['usNuclearProduction']
    elif selection == 6:
        link = monetaryURLs['usOilProduction']
    elif selection == 7:
        link = monetaryURLs['usOilImports']
    elif selection == 8:
        link = monetaryURLs['IranOilProduction']
    elif selection == 9:
        link = monetaryURLs['opecOilProduction']
    elif selection == 10:
        link = monetaryURLs['saOilProduction']
    elif selection == 11:
        link = monetaryURLs['worldOilProduction']

    return link
def petroleum():
    print('\n0. PRINT ALL')
    print('\n1. US Petroleum Imports')
    print('2. US Petroleum Exports')
    print('3. US Oil Imports')
    print('4. US Oil Exports')
    print('5. US Crude Imports')
    print('6. US Crude Exports')
    print('7. US Crude Stocks')
    print('8. US Gasoline Imports')
    print('9. US Gasoline Stocks')
    print('10. US Oil Rigs')
    print('11. World Oil Rigs')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 11:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
        printAll(petroleumURLs)
        return exit()

    elif selection == 1:
        link = petroleumURLs['petroImportsWk']
    elif selection == 2:
        link = petroleumURLs['petroExportsWk']
    elif selection == 3:
        link = petroleumURLs['oilImportsWk']
    elif selection == 4:
        link = petroleumURLs['oilExportsWk']
    elif selection == 5:
        link = petroleumURLs['crudeImportsWk']
    elif selection == 6:
        link = petroleumURLs['crudeExportsWk']
    elif selection == 7:
        link = petroleumURLs['crudeStocksWk']
    elif selection == 8:
        link = petroleumURLs['gasImportsWk']
    elif selection == 9:
        link = petroleumURLs['gasStocksWk']
    elif selection == 10:
        link = petroleumURLs['oilRigs']
    elif selection == 11:
        link = petroleumURLs['worldRigs']

    return link
def naturalGas():
    print('\n0. PRINT ALL')
    print('\n1. LNG Imports')
    print('2. LNG Exports')
    print('3. Natural Gas Imports')
    print('4. Natural Gas Exports')
    print('5. Natural Gas Production')
    print('6. Natural Gas Consumption')
    print('7. Natural Gas Storage')
    print('8. Natural Gas Storage Volume')
    print('9. Natural Gas Rigs')

    # Get selection from user and return the URL link
    selection = int(input('\nEnter number from the list: '))
    while selection < 0 or selection > 9:
        selection = int(input('\nEnter number from the list: '))

    if selection == 0:
        printAll(naturalGasURLs)
        return exit()

    elif selection == 1:
        link = naturalGasURLs['lngImports']
    elif selection == 2:
        link = naturalGasURLs['lngExports']
    elif selection == 3:
        link = naturalGasURLs['ngImports']
    elif selection == 4:
        link = naturalGasURLs['ngExports']
    elif selection == 5:
        link = naturalGasURLs['ngProduction']
    elif selection == 6:
        link = naturalGasURLs['ngConsumption']
    elif selection == 7:
        link = naturalGasURLs['ngStorage']
    elif selection == 8:
        link = naturalGasURLs['ngVolume']
    elif selection == 9:
        link = naturalGasURLs['ngRigs']

    return link

# Get selection from user and return a URL link
def getLink():
    print('\n1. Inflation')
    print('2. Sentiment')
    print('3. Monetary')
    print('4. Macro Energy')
    print('5. Weekly Petroleum')
    print('6. Natural Gas')

    selection = int(input('\nEnter number from the list: '))
    while selection < 1 or selection > 6:
        selection = int(input('\nEnter number from the list: '))

    if selection == 1:
        link = inflation()
    elif selection == 2:
        link = sentiment()
    elif selection == 3:
        link = monetary()
    elif selection == 4:
        link = energy()
    elif selection == 5:
        link = petroleum()
    elif selection == 6:
        link = naturalGas()
    
    return link

# Parse HTML from URL link and return the data in an array
def getData(link):
    source = requests.get(link).text
    soup = bs(source,'html.parser')
    stats = soup.find_all('tbody')

    arrayOfData = []

    for stat in stats:
        statElement = stat.find_all('td')
        for el in statElement:
            arrayOfData.append(el.text) 

    return arrayOfData

# Organize parsed data by summary/release dates and print
def printData(data):
    summary = data[0]    
    dates = data[11:17]

    print('-------------------------------------')
    print(summary)
    print(dates)
    print('-------------------------------------')

def printAll(data):
    for link in data:
        printData(getData(data[link]))
        
# Run program -> Print out the data from the selected URL link
printData(getData(getLink()))

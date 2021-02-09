from bs4 import BeautifulSoup as bs
import requests

# Contains all the URL links required to run the program
from ycharts import *

class Data:
    def __init__(self, summary, dates):
        self.summary = summary
        self.dates = dates

# Subset of selections that either prints everything or returns URL link
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
        printAll(getData(usCPI))
        printAll(getData(usInflation)) 
        printAll(getData(usM2supply))
        printAll(getData(usM2Velocity))
        printAll(getData(japanInflation))
        printAll(getData(ukInflation))
        printAll(getData(chinaInflation))
        printData(getData(chinaM2supply))

    elif selection == 1:
        link = usCPI
    elif selection == 2:
        link = usInflation
    elif selection == 3:
        link = usM2supply
    elif selection == 4:
        link = usM2Velocity
    elif selection == 5:
        link = japanInflation
    elif selection == 6:
        link = ukInflation
    elif selection == 7:
        link = chinaInflation
    elif selection == 8:
        link = chinaM2supply

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
            printAll(getData(investorSentiment))
            printAll(getData(usCCI)) 
            printAll(getData(cashAllocation))
            printAll(getData(bondAllocation))
            printAll(getData(stockAllocation))
            printAll(getData(euCCI))
            printAll(getData(euSentiment))
            printAll(getData(japanCCI))
            printAll(getData(ukSentiment))
            printData(getData(usUnemployment))

    if selection == 1:
        link = investorSentiment
    elif selection == 2:
        link = usCCI
    elif selection == 3:
        link = cashAllocation
    elif selection == 4:
        link = bondAllocation
    elif selection == 5:
        link = stockAllocation
    elif selection == 6:
        link = euCCI
    elif selection == 7:
        link = euSentiment
    elif selection == 8:
        link = japanCCI
    elif selection == 9:
        link = ukSentiment
    elif selection == 10:
        link = usUnemployment

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
            printAll(getData(realDollarIndex))
            printAll(getData(m1supply)) 
            printAll(getData(m1Velocity))
            printAll(getData(usLoansCommercial))
            printAll(getData(usLoansCC))
            printAll(getData(usGDP))
            printAll(getData(ukGDP))
            printAll(getData(swedenGDP))
            printAll(getData(netherGDP))  
            printAll(getData(euGDP))
            printAll(getData(chinaGDP))
            printAll(getData(worldGDP))
            printData(getData(usDebt))

    if selection == 1:
        link = realDollarIndex
    elif selection == 2:
        link = m1supply
    elif selection == 3:
        link = m1Velocity
    elif selection == 4:
        link = usLoansCommercial
    elif selection == 5:
        link = usLoansCC
    elif selection == 6:
        link = usGDP
    elif selection == 7:
        link = ukGDP
    elif selection == 8:
        link = swedenGDP
    elif selection == 9:
        link = netherGDP
    elif selection == 10:
        link = euGDP
    elif selection == 11:
        link = chinaGDP
    elif selection == 12:
        link = worldGDP
    elif selection == 13:
        link = usDebt

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
            printAll(getData(usEnergyConsumption))
            printAll(getData(usWindProduction)) 
            printAll(getData(usSolarProduction))
            printAll(getData(usNGProduction))
            printAll(getData(usNuclearProduction))
            printAll(getData(usOilProduction))
            printAll(getData(usOilImports))
            printAll(getData(iranOilProduction))
            printAll(getData(opecOilProduction))  
            printAll(getData(saOilProduction))
            printData(getData(worldOilProduction))

    elif selection == 1:
        link = usEnergyConsumption
    elif selection == 2:
        link = usWindProduction
    elif selection == 3:
        link = usSolarProduction
    elif selection == 4:
        link = usNGProduction
    elif selection == 5:
        link = usNuclearProduction
    elif selection == 6:
        link = usOilProduction
    elif selection == 7:
        link = usOilImports
    elif selection == 8:
        link = iranOilProduction
    elif selection == 9:
        link = opecOilProduction
    elif selection == 10:
        link = saOilProduction
    elif selection == 11:
        link = worldOilProduction

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
            printAll(getData(petroImportsWk))
            printAll(getData(petroExportsWk)) 
            printAll(getData(oilImportsWk))
            printAll(getData(oilExportsWk))
            printAll(getData(crudeImportsWk))
            printAll(getData(crudeExportsWk))
            printAll(getData(crudeStocksWk))
            printAll(getData(gasImportsWk))
            printAll(getData(gasStocksWk)) 
            printAll(getData(oilRigs))
            printData(getData(worldRigs))

    elif selection == 1:
        link = petroImportsWk
    elif selection == 2:
        link = petroExportsWk
    elif selection == 3:
        link = oilImportsWk
    elif selection == 4:
        link = oilExportsWk
    elif selection == 5:
        link = crudeImportsWk
    elif selection == 6:
        link = crudeExportsWk
    elif selection == 7:
        link = crudeStocksWk
    elif selection == 8:
        link = gasImportsWk
    elif selection == 9:
        link = gasStocksWk
    elif selection == 10:
        link = oilRigs
    elif selection == 11:
        link = worldRigs

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
            printAll(getData(lngImports))
            printAll(getData(lngExports)) 
            printAll(getData(ngImports))
            printAll(getData(ngExports))
            printAll(getData(ngProduction))
            printAll(getData(ngConsumption))
            printAll(getData(ngStorage))
            printAll(getData(ngVolume))
            printData(getData(ngRigs))

    elif selection == 1:
        link = lngImports
    elif selection == 2:
        link = lngExports
    elif selection == 3:
        link = ngImports
    elif selection == 4:
        link = ngExports
    elif selection == 5:
        link = ngProduction
    elif selection == 6:
        link = ngConsumption
    elif selection == 7:
        link = ngStorage
    elif selection == 8:
        link = ngVolume
    elif selection == 9:
        link = ngRigs

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
    DATA = Data(summary, dates)

    print(DATA.summary)
    print(DATA.dates,'\n')

    # Option to rerun or end the program
    runAgain = input("\nWould you like to run program again? y/n ")
    if runAgain == 'y':
        printData(getData(getLink()))
    else:
        exit()

# Reserved for the 'PRINT ALL' option, for printing in sequence
def printAll(data):
    summary = data[0]    
    dates = data[11:17]
    DATA = Data(summary, dates)

    print(DATA.summary)
    print(DATA.dates,'\n')


# Run program -> Print out the data from the selected URL link
printData(getData(getLink()))






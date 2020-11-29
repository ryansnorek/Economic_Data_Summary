from bs4 import BeautifulSoup as bs
import requests
from ycharts import *

class Data:
    def __init__(self, summary, dates):
        self.summary = summary
        self.dates = dates

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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 8:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
        printAll( getData(usCPI))
        printAll( getData(usInflation)) 
        printAll( getData(usM2supply))
        printAll( getData(usM2Velocity))
        printAll( getData(japanInflation))
        printAll( getData(ukInflation))
        printAll( getData(chinaInflation))
        printData( getData(chinaM2supply))
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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 9:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
            printAll( getData(investorSentiment))
            printAll( getData(usCCI)) 
            printAll( getData(cashAllocation))
            printAll( getData(bondAllocation))
            printAll( getData(stockAllocation))
            printAll( getData(euCCI))
            printAll( getData(euSentiment))
            printAll( getData(japanCCI))
            printData( getData(ukSentiment))
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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 13:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
            printAll( getData(realDollarIndex))
            printAll( getData(m1supply)) 
            printAll( getData(m1Velocity))
            printAll( getData(usLoansCommercial))
            printAll( getData(usLoansCC))
            printAll( getData(usGDP))
            printAll( getData(ukGDP))
            printAll( getData(swedenGDP))
            printAll( getData(netherGDP))  
            printAll( getData(euGDP))
            printAll( getData(chinaGDP))
            printAll( getData(worldGDP))
            printData( getData(usDebt))
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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 11:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
            printAll( getData(usEnergyConsumption))
            printAll( getData(usWindProduction)) 
            printAll( getData(usSolarProduction))
            printAll( getData(usNGProduction))
            printAll( getData(usNuclearProduction))
            printAll( getData(usOilProduction))
            printAll( getData(usOilImports))
            printAll( getData(iranOilProduction))
            printAll( getData(opecOilProduction))  
            printAll( getData(saOilProduction))
            printData( getData(worldOilProduction))
    if selection == 1:
        link = usEnergyConsumption
    if selection == 2:
        link = usWindProduction
    if selection == 3:
        link = usSolarProduction
    if selection == 4:
        link = usNGProduction
    if selection == 5:
        link = usNuclearProduction
    if selection == 6:
        link = usOilProduction
    if selection == 7:
        link = usOilImports
    if selection == 8:
        link = iranOilProduction
    if selection == 9:
        link = opecOilProduction
    if selection == 10:
        link = saOilProduction
    if selection == 11:
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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 9:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
            printAll( getData(petroImportsWk))
            printAll( getData(petroExportsWk)) 
            printAll( getData(oilImportsWk))
            printAll( getData(oilExportsWk))
            printAll( getData(crudeImportsWk))
            printAll( getData(crudeExportsWk))
            printAll( getData(crudeStocksWk))
            printAll( getData(gasImportsWk))
            printData( getData(gasStocksWk))  
    if selection == 1:
        link = petroImportsWk
    if selection == 2:
        link = petroExportsWk
    if selection == 3:
        link = oilImportsWk
    if selection == 4:
        link = oilExportsWk
    if selection == 5:
        link = crudeImportsWk
    if selection == 6:
        link = crudeExportsWk
    if selection == 7:
        link = crudeStocksWk
    if selection == 8:
        link = gasImportsWk
    if selection == 9:
        link = gasStocksWk
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

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 0 or selection > 8:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

    if selection == 0:
            printAll( getData(lngImports))
            printAll( getData(lngExports)) 
            printAll( getData(ngImports))
            printAll( getData(ngExports))
            printAll( getData(ngProduction))
            printAll( getData(ngConsumption))
            printAll( getData(ngStorage))
            printData( getData(ngVolume))
    if selection == 1:
        link = lngImports
    if selection == 2:
        link = lngExports
    if selection == 3:
        link = ngImports
    if selection == 4:
        link = ngExports
    if selection == 5:
        link = ngProduction
    if selection == 6:
        link = ngConsumption
    if selection == 7:
        link = ngStorage
    if selection == 8:
        link = ngVolume
    return link

def getHTML():
    print('\n1. Inflation')
    print('2. Sentiment')
    print('3. Monetary')
    print('4. Macro Energy')
    print('5. Weekly Petroleum')
    print('6. Natural Gas')

    selection = input('\nEnter number from the list: ')
    selection = int(selection)
    while selection < 1 or selection > 6:
        selection = input('\nEnter number from the list: ')
        selection = int(selection)

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

def getData(html):
    source = requests.get(html).text
    soup = bs(source,'html.parser')
    stats = soup.find_all('tbody')

    STATS = []
    for stat in stats:
        statElement = stat.find_all('td')
        for elem in statElement:
            STATS.append(elem.text) 
    return STATS

def printData(data):
    summary = data[0]    
    dates = data[11:17]
    DATA = Data(summary, dates)

    print(DATA.summary)
    print(DATA.dates,'\n')

    again = input("\nWould you like to run program again? y/n ")
    if again == 'y':
        printData( getData( getHTML() ))
    else:
        exit()

def printAll(data):
    summary = data[0]    
    dates = data[11:17]
    DATA = Data(summary, dates)

    print(DATA.summary)
    print(DATA.dates,'\n')

# Run program
printData( getData( getHTML() ))






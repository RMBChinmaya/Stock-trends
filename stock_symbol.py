import yfinance as yf

def getCompany(text):
    company_names = []
    li = list(text.split(" "))
    for stocks in li:
        if stocks is not None and len(str(stocks)) > 0:
            company_name = (yf.Ticker(stocks)).info['longName']
            company_names.append(company_name)
        else:
            continue
    
    return company_names


#getCompany('GOOG')
#getCompany('Alphabet')
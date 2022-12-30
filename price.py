import requests, bs4

def getSPPrice():
    resSP = requests.get('https://www.google.com/finance/quote/SPY:NYSEARCA?hl=en')
    resSP.raise_for_status()
    SoupSP = bs4.BeautifulSoup(resSP.text, 'html.parser')
    SP_price = (SoupSP.select('#yDmH0d > c-wiz.zQTmif.SSPGKf.u5wqUe > div > div.e1AOyf > div > main > div.Gfxi4 > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc > div > div:nth-child(1) > div > span > div > div'))
    return(SP_price)

def getDowPrice():
    resDow = requests.get('https://www.google.com/finance/quote/DOW:NYSE')
    resDow.raise_for_status()
    SoupDow = bs4.BeautifulSoup(resDow.text, 'html.parser')
    DOW_price = (SoupDow.select('#yDmH0d > c-wiz > div > div.e1AOyf > div > main > div.Gfxi4 > div.VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.QZMA8b > c-wiz > div > div:nth-child(1) > div > div.rPF6Lc > div > div:nth-child(1) > div > span > div > div'))
    return(DOW_price)
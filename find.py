import re


def regex(userIn):
    dollarReg = re.compile(r'\$\d+.\d\d')
    price = dollarReg.search(userIn)
    return(price.group())
import find, window, spread, price

# Gets stock price from Google
DOW_price = price.getDowPrice()
SP_price = price.getSPPrice()


# Converting the output to a string
DOW_price = str(DOW_price)
SP_price = str(SP_price)

# Regex to get just the price 
SP_price = find.regex(SP_price)
DOW_price = find.regex(DOW_price)


# Calls our custom function that creates a window that displays the current prices for the stocks
window.show(SP_price, DOW_price)

# A function that puts the values in a csv and prints the values to the terminal
spread.addPrice("S&P", SP_price)
spread.addPrice("DOW", DOW_price)

spread.printPrices()

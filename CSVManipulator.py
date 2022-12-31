import csv
import time

def addPrice(stockName, stockValue):
    outputFile = open("output.csv", 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow([stockName, stockValue, time.ctime()])
    outputFile.close()

def printPrices():
    readCSVFile = open('output.csv', 'r')
    CSVReader = csv.reader(readCSVFile)
    for row in CSVReader:
        print(str(row))
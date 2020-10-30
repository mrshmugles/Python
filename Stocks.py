stocks = {
    "XOM": "34.15",
    "GE": "6.82",
    "MSFT": "220.86",
    "BP": "16.59",
    "C": "43.03",
    "PG": "144.04",
    "WMT": "143.94",
    "PFE": "36.86",
    "DIS": "126.59",
    "TM": "131.53"
}
x = input("Please enter a ticker symbol: ")

if x in stocks:
    y = stocks[x]
    print (f"\nTicker symbol: {x} \nStock price: ${y}")
else:
    print ("\nTicker symbol not found")
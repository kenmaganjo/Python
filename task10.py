#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
def stock_total():
        prods = [['omo','30kshs',300], ['milk','50kshs',200],['bread','45kshs',359], ['coffee','5kshs',79]]
        total_stock = 0
        for i in prods:
                total_stock = total_stock + i[2]

        return total_stock

stock = stock_total()

print(stock)

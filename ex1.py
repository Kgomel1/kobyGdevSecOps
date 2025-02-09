# homework  to serve ex1
def findDividends(number):

    for x in range(1, number):
        if number % x == 0:
            print(x)

number = int(input('Please enter a number: '))

findDividends(number);


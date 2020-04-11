def multiplicationTable(number: int, upto: int = 10):
    for i in range(10):
        index = i+1
        print(index, " x ", num, " = ", index * num)

num = int(input("Please enter a number: "))
multiplicationTable(num) 

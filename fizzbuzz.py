numbersWithSpace = input()

yoink = numbersWithSpace.split(" ")

i = 1
while i <= int(yoink[2]):
    if i % int(yoink[0]) == 0:
        if i % int(yoink[1]) == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % int(yoink[1]) == 0:
            if i % int(yoink[0]) == 0:
                print("FizzBuzz")
            else:
                print("Buzz")
    else:
        print(i)
    i = i+1
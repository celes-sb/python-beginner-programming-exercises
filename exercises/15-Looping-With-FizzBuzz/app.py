def fizz_buzz():
    # your code here
    for number in range(1, 101):
        if (number % 3 == 0 and number % 5 == 0):
            print('FizzBuzz')
        elif (number % 3 == 0):
            print('Fizz')
        elif (number % 5 == 0):
            print('Buzz')
        else:
            print(number)

fizz_buzz()
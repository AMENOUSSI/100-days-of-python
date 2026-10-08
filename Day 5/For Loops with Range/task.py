# sum_num = 0
# for number in range(1,101):
#     # print(number)
#     sum_num += number
# print(sum_num)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
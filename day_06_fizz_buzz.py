# Write a program for generating a list from 1-100 where numbers divisible by 3 
# are replaced with Fizz, and numbers divisible by 5 are replaced with Buzz
# and numbers divisible by both 3 and 5 are replaced with FizzBuzz

for x in range(1,101):
    if(x%3 == 0 and x%5 == 0):
        print("FizzBuzz")
    elif(x%3 == 0):
        print("Fizz")
    elif(x%5 == 0):
        print("Buzz")
    else:
        print(x)

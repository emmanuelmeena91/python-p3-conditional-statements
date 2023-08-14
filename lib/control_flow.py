#!/usr/bin/env python3

def admin_login(username, password):
    print("Access granted") if ((username == "admin" or username == "ADMIN") and password == "12345") else print("Access denied")
    
    pass
              
def hows_the_weather(temperature):
    if temperature < 40:
        print("It's brisk out there!")
    elif temperature >= 40 and temperature <= 65:
        print("It's a little chilly out there!")
    elif temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")                  

    pass


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)            

    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None


admin_login("sudo", "12345")

admin_login("admin", "12345")

admin_login("ADMIN", "12345")



hows_the_weather(33)

hows_the_weather(99)

hows_the_weather(75)


fizzbuzz(1)

fizzbuzz(2)

fizzbuzz(3)

fizzbuzz(4)

fizzbuzz(5)

fizzbuzz(15)

print(calculator("+", 1, 1))
print(calculator("-", 3, 1))
print(calculator("*", 3, 2))
print(calculator("/", 4, 2))
print(calculator("nope", 4, 2))



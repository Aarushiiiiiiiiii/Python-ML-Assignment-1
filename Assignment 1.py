# Program to take two numbers as input and print their sum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("The sum is:", num1 + num2)


# Program to check whether a given number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Program to calculate the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("The factorial is:", factorial(num))


# Program to ask the user for their name and print a greeting message
name = input("Enter your name: ")
print(f"Hello, {name}!")


# Program to take a string input from the user and write it to a text file
user_input = input("Enter a string: ")
with open("output.txt", "w") as file:
    file.write(user_input)


# Program to read the content of a text file and print it to the console
with open("output.txt", "r") as file:
    content = file.read()
    print(content)


# Program to take a string as input and return its length
user_input = input("Enter a string: ")
print("The length of the string is:", len(user_input))


# Program to concatenate two strings and return the result
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = string1 + string2
print("The concatenated string is:", result)


# Program to check if a substring is present in a given string
string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in string:
    print("Substring is present in the main string.")
else:
    print("Substring is not present in the main string.")


# Program to check if a substring is present in a given string
string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in string:
    print("Substring is present in the main string.")
else:
    print("Substring is not present in the main string.")


# Program to convert a given string to uppercase
user_input = input("Enter a string: ")
print("Uppercase string:", user_input.upper())


# Program to generate the first n numbers in the Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("Fibonacci sequence:", fibonacci(n))


# Program to calculate the sum of the digits of a given number
num = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in num)
print("Sum of the digits:", sum_of_digits)


# Program to ask the user for their birth year and calculate their age
from datetime import datetime

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Your age is: {age}")


# Program to read multiple lines of input from the user until they enter an empty line, then print all the lines
lines = []
print("Enter multiple lines of text (Enter an empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)


# Program to read data from a CSV file and print it to the console
import csv

with open('data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))


# Program to count the frequency of each character in a string
from collections import Counter

user_input = input("Enter a string: ")
frequency = Counter(user_input)
print("Character frequencies:", frequency)

# Program to convert a given string to title case
user_input = input("Enter a string: ")
print("Title case string:", user_input.title())


# Program to check if two strings are anagrams of each other
from collections import Counter

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if Counter(string1) == Counter(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# Program to remove all punctuation from a given string
import string

user_input = input("Enter a string: ")
result = user_input.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", result)


# Program to take a list of numbers and return their sum
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("The sum of the numbers is:", sum(numbers))


# Program to count the occurrences of a specific element in a list
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element {element} occurs {count} times in the list.")


# Program to return the minimum and maximum values in a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))


# Program to convert temperature from Celsius to Fahrenheit and vice versa based on user input
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()
temperature = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temperature} Celsius is {celsius_to_fahrenheit(temperature)} Fahrenheit.")
elif choice == 'F':
    print(f"{temperature} Fahrenheit is {fahrenheit_to_celsius(temperature)} Celsius.")
else:
    print("Invalid choice.")


# Program to act as a simple calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator."

print("The result is:", result)


# Program to copy the contents of one text file to another
with open("source.txt", "r") as source_file:
    content = source_file.read()

with open("destination.txt", "w") as destination_file:
    destination_file.write(content)


# Program to check if a string starts with a given prefix or ends with a given suffix
user_input = input("Enter a string: ")
prefix = input("Enter the prefix: ")
suffix = input("Enter the suffix: ")

if user_input.startswith(prefix):
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if user_input.endswith(suffix):
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")


# Program to convert a string into a list of its characters
user_input = input("Enter a string: ")
character_list = list(user_input)
print("List of characters:", character_list)

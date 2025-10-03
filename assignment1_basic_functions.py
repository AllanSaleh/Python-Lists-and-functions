def greet(name):
  print(f"Hello, {name}!")

greet("allan")

def rectangle_area(length, width):
  return length * width

area = rectangle_area(6, 7)
print(area)

def add(num1, num2):
  # showing on the screen and then python forgets about it
  print(num1 + num2)

def add_with_return(num1, num2):
  # give it back to us to use later in our program
  return num1 + num2

add(5,8)

result = add_with_return(5, 8)
print("The result is:", result)
print("The average is:", result/2)


def celcius_to_farenheit(celcius):
  return f"The result is {(celcius * 9/5) + 32} Farenheit!"

print(celcius_to_farenheit(23))


def introduce(name, title="Mr./Mrs"):
  print(f"Hello, {title} {name}! Welcome!")

introduce("Bob")
introduce("Billy", "Mr.")
introduce("Sally", "Mrs.")

def format_phone_number(number, country_code="+1"):
  return f"{country_code} {number}"

print(format_phone_number("123456789"))
print(format_phone_number("123456789","+964"))


def divide_with_remainder(dividend, divisor):
  quotient = dividend // divisor
  remainder = dividend % divisor
  return f"the quotient is {quotient} and the remainder is {remainder}"

print(divide_with_remainder(10,3))


def calculate_compound_interest(principal, rate = 0.05, compounding_period = 1, years = 1):
  # A = P(1 + r/n)^nt
  return round(principal * ((1 + rate/compounding_period)**(years * compounding_period)),2)

print(calculate_compound_interest(100))


def list_statistics(numbers):
  if not numbers:
    return "sum: 0, average: 0, count: 0"
  total = sum(numbers)
  count = len(numbers)
  average = round(total / count, 2)
  return f"sum: {total}, average: {average}, count: {count}"

print(list_statistics([2,5,8,60,4,3]))
# print(list_statistics())
# DRY - DONT REPEAT YOURSELF
# print("Hi, Javian!")
# print("Welcome to class!")

# print("Hi, Joe!")
# print("Welcome to class!")

# print("Hi, Troy!")
# print("Welcome to class!")

def say_hello(name = "No name"):
  print(f"Hi, {name}!")
  print("Welcome to class!")

say_hello("Javian")
say_hello("Edi")
say_hello("Joe")

say_hello()


# user_name = input("Enter your name: ")
# say_hello(user_name)


def area(height, width = 5):
  print(f"The area for {width} and {height} is {width*height}")

area(3,5)

area(9,84)

area(8)

area(10)

# area(height=11)


def introduce(name, age):
  print(f"{name} is {age} years old.")

introduce("Sally", 29)
introduce( 29, "John") #Order matters
introduce( age = 29, name = "John")



message = "I am a global scope"

def show_message():
  # global message
  
  message = "Hello everyone"

  # Access the message variable in the global scope
  print(message)

show_message()

print(message)

print(round(5/6, 0))

# "allan" => "Allan"
def validate_user_input(name, age):
  name = name.strip().title()
  try:
    age = int(age)
    if age < 0:
      raise ValueError("Age can't be negative")
  except ValueError:
    return None
  return f"User: {name}, Age: {age}"

print(validate_user_input("   allan    ", "-25"))
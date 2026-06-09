# User Information
greetings = input ("Hello")
name =input("What's your name? ")
age = int (input("What's your age? "))
city = input ("Where do you live? ")
country =input("Which country? ")
language = input ("What is your favorite programming language? ")
job = input("What is your dream job? ")
hobby =input("What is your favorite hobby? ")
food = input("What is your favorite food? ")
book = input("What is your favorite book? ")
movie = input("What is your favorite movie? ")
goal = input("What is one goal you want to achieve this year? ")

# Remove whitespace from string
greetings = greetings.strip()
name = name.strip()
city =city.strip()
country =country.strip()
language = language.strip()
job =job.strip()
hobby = hobby.strip()
food = food.strip()
book = book.strip()
movie = movie.strip()
goal = goal.strip()



# Capitalize User Information
greetings = greetings.capitalize()
name = name.capitalize()
city = city.capitalize()
country = country.capitalize()
language = language.capitalize()
job = job.capitalize()
hobby = hobby.capitalize()
food = food.capitalize()
book = book.capitalize()
movie = movie.capitalize()
goal = goal.capitalize()

# Outcome/Results
print("Hello")
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city} city in {country}")
print(f"My favorite programming language is {language}")
print(f"My dream job is {job}")
print(f"My favorite hobby is {hobby} ")
print(f"My favorite food is {food} ")
print(f"My favorite book is {book} .You should read it")
print(f"My favorite movie is {movie} but only a hand full of people have watched it. You should try it.")
print(f"This year my goal is {goal} and I will achieve it.")



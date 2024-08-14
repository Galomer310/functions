
# def display_massage(currently_learning):
#     print(f"i am currently learning {currently_learning}")
# display_massage("python functions")

# 🌟 Exercise 2: What’s your favorite book ?
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
# favorite_book("Alice in Wonderland")

# 🌟 Exercise 3 : Some Geography
# def describe_city(city, country="usa"):
#     return f"{city} is in {country}"
# print(describe_city("Reykjavik", "Iceland"))

# Exercise 4 : Random
import random
# def random_num(num):
#     random_number = (random.randrange(1,101))
#     if random_number == num:
#         print("Great success")
#         print(random_number)
#         print(num)
#     else:
#         print("fail attempt")
#         print(random_number)
#         print(num)
# random_num(2)

# 🌟 Exercise 5 : Let’s create some personalized shirts !
# def make_shirt(size="large", message="I Love Python"):
#     if size == "small":
#         return f"the size of the shirt is {size} and the text is: A great day start with coffee :-) "
#     elif size == "medium":
#         return f"the size of the shirt is {size} and the text is: I Love to code "
#     elif size == "xl":
#         return f"the size of the shirt is {size} and the text is: I love javaScript "
#     else:
#         return f"the size of the shirt is {size} and the text is: {message}"
# print(make_shirt(""))

# 🌟 Exercise 6 : Magicians …
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#
# def show_magicians(names):
#     for name in names:
#         print(name)
#
# def make_great(names):
#     for i in range(len(names)):
#         names[i] = f"the Great {names[i]}"
#
# make_great(magician_names)
#
# show_magicians(magician_names)

# 🌟 Exercise 7 : Temperature Advice

# def get_random_temp(season):
#     if season == "winter":
#         return random.uniform(-10.0, 16.0)
#     elif season == "summer":
#         return random.uniform(25.0, 40.0)
#     elif season == "spring":
#         return random.uniform(12.0, 25.0)
#     elif season == "autumn":
#         return random.uniform(15.0, 28.0)
#
# def main():
#     user_answer = input("type in a season 'summer', 'autumn', 'winter', 'spring'\n")
#     temp = get_random_temp(user_answer)
#     print(f"The temperature right now is {temp} degrees celsius")
#     if temp < 0:
#         print(f"Brrr, that’s freezing! Wear some extra layers today")
#     elif temp < 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif temp < 23:
#         print("it's a perfect weather today")
#     elif temp < 32:
#         print("it's hot outside today")
#     else:
#         print("it's extremely hot outside today so from ac to ac")
# main()

# Exercise 8 : Star Wars Quiz
# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]
# def star_wars_quiz():
#     wrong_answers = []
#     right_answers = []
#     for q in data:
#         print(q['question'])
#         user_answer = input("your answer?")
#         if user_answer == q['answer']:
#             right_answers.append(user_answer)
#         else:
#             wrong_answers.append(user_answer)
#     incorrect_answers = len(wrong_answers)
#     correct_answers = len(right_answers)
#     print(f"you have {incorrect_answers} incorrect answers :{wrong_answers}")
#     print(f"you have {correct_answers} correct answers : {right_answers}")
#
# star_wars_quiz()
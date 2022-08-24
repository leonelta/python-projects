from sys import argv

from click import prompt

script, user_name = argv
prompt = '> '

print(f"HI {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"Do you like me {user_name}?")
likes = input(prompt)
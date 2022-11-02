import random

computer = random.choice(['rock', 'paper', 'scissor'])

user = input('Enter you\'re choice(Rock/Paper/Scissor): ')
user = user.lower()

if (computer == 'rock' and user == 'scissor') or (computer == 'paper' and user == 'rock') or (computer == 'scissor' and user == 'paper'):
    print(f"Computer: {computer}")
    print(f"You: {user}")
    print("***************************")
    print("Computer Won!!! Better Luck Next Time!!")
    print("***************************")
elif computer == user:
    print(f"Computer: {computer}")
    print(f"You: {user}")
    print("***************************")
    print("It's a Draw!!!")
    print("***************************")
else:
    print(f"Computer: {computer}")
    print(f"You: {user}")
    print("***************************")
    print("Congratulations You Won!!!!")
    print("***************************")

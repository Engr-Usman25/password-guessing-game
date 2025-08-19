import random
easy_words= ['apple', 'train', 'tiger', 'money', 'pakistan']
medium_words= ['computer', 'keyboard', 'mouse', 'monitor', 'internet']
hard_words= ['programming', 'development', 'algorithm', 'functionality', 'optimization']
print('Welcome to Password Guessing Game!')
print('Choose a difficulty level: 1. Easy 2. Medium 3. Hard')
level= input('Enter Difficulty: ').lower()
if level== 'easy':
    secret= random.choice(easy_words)
elif level== 'medium':
    secret= random.choice(medium_words)
elif level== 'hard':
    secret= random.choice(hard_words)
else:
    print('Invalid difficulty level. Please restart the game and choose a valid level.')
    secret= random.choice(easy_words) 

attempts=0
print('\n Guess the password')
while True:
    guess= input('Enter your guess: ')
    attempts += 1
    if guess == secret:
        print(f'Congratulations! You guessed the password "{attempts}" in {attempts} attempts.')
        break

hint = ''
for i in range(len(secret)):
    if i < len(secret) and guess[i] != secret[i]:
        hint += guess[i]
    else:
        hint += '_'
    print(f'Hint: {hint}')

print('Game Over!')

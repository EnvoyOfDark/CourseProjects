import random
tries = 0
n = random.randint(1,50)
while tries < 6:
    i = int(input('Your guess (from 1 to 50): '))
    tries+=1
    if i > n:
        print('Too big...')
    if i < n:
        print('Too small...')
    if i == n:
        print(f'Correct! You guessed my number in {tries} guesses.')
    if i != n and tries == 6:
        print(f'You lose. My number swas {n}')
        break
  
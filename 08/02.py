first_word = list(input('Enter first word: '))
second_word = list(input('Enter second word: '))
bulls = 0
cows = 0

for i in range(len(first_word)):
    if first_word[i] == second_word[i]:
        bulls += 1
    elif first_word[i] in second_word:
        cows += 1

print(bulls, cows)

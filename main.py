import random

wordlist = '1234567890qwertyuiopasdfghjklçzxcvbnm!@#$%¨&*()QWERTYUIOPASDFGHJKLÇZXCVBNM'

number_of_characters = int(input("Number of chars: "))

password = random.sample(wordlist,number_of_characters)

print(password)

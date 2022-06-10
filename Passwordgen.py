import random


Character=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '1','2','3','4','5','6','7','8','9','0']

numbers=int(input("How many passwrods do you want?"))
length=int(input("Whats the length of the password?"))

for i in range(numbers):
    passwwords = " "
    for x in range(length):
        passwwords+=random.choice(Character)
    print(passwwords)


import random
letters = [chr(v) for v in range(ord('a'), ord('a') + 26)]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')']

print ("welcome to password generator")

n_letters = int(input("how many letters?\n"))

n_symbols = int(input("how many symbols?\n"))

n_numbers = int(input("how many numbers?\n"))

password_list=[]

for i in range(1,n_letters+1):
    char = random.choice(letters)
    password_list+= char

for i in range(1,n_symbols+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,n_numbers+1):
    char = random.choice(symbols)
    password_list += char        

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print("suggested password is:",password)    


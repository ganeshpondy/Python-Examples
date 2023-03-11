
import string
import random
 
print("################################")
print("    Password Generator Tool    ")
print("################################")

pass_length = int(input("Enter the Password Length: "))
if pass_length < 8:
    print("Password Length Should be Minium 8 Characters")
    quit()

pass_cap = input("Do you need CAPS in the Password? (y/n): ")
pass_num = input("Do you need Numbers in the Password? (y/n): ")
pass_spl = input("Do you need Special Characters in the Password? (y/n): ")

# print(pass_length)
# print(pass_cap)
# print(pass_num)
# print(pass_spl)

characterList = ""
characterList += string.ascii_lowercase

if pass_cap == "y":
    characterList += string.ascii_uppercase
if pass_num == "y":
    characterList += string.digits
if pass_spl == "y":
    characterList += string.punctuation

password_count=0

# print(characterList)

while password_count < 5:
    password_count = password_count + 1

    password = []
    for i in range(pass_length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
        
    print(f"The random password {password_count}: " + "".join(password))
    



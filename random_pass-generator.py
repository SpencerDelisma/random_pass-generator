import random
import math 

pass_len = int(input("Enter the length of the password: "))
password = []

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

#30-20-10
alpha_len = pass_len // 2
num_len = math.ceil(pass_len *30 / 100)
special_len = pass_len-(alpha_len + num_len)

def gen_password(length,array,is_alpha=False):
    for i in range(length):
        index = random.randint(0,len(array)-1)
        character = array[index]
        if is_alpha:
            case = random.randint(0,1)
            if case == 1:
                character = character.upper()
        password.append(character)
gen_password(alpha_len,alpha,True)
gen_password(num_len,num)
gen_password(special_len,special)
random.shuffle(password)
gen_password = " "
for i in password:
    gen_password =gen_password + str(i)
print(gen_password)
def add(user_input1, user_input2):
    total_value = user_input1 + user_input2
    return f"Final Value for Addition is {total_value}"

def sub(user_input1, user_input2):
    total_value = user_input1 - user_input2
    return f"Final Value for Subtraction is {total_value}"

def mul(user_input1, user_input2):
    total_value = user_input1 * user_input2
    return f"Final Value for Multiplication is {total_value}"

def div(user_input1, user_input2):
    total_value = user_input1 / user_input2
    return f"Final Value for Division is {total_value}"

user_input1 = int(input("enter number two value1: \n"))
user_input2 = int(input("enter number two value2: \n"))
user_cal = int(input("Select Valid Options \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n"))
#return_value = add(user_input1, user_input2)
if user_cal == 1:
    return_value = add(user_input1, user_input2)
elif user_cal == 2:
    return_value = sub(user_input1, user_input2)
elif user_cal == 3:
    return_value = mul(user_input1, user_input2)
elif user_cal == 4:
    return_value = div(user_input1, user_input2)
else:
    print("Not Valid Input Option")

print(return_value)

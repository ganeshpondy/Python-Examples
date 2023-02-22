#Importing calculator_module.py script as a Module in this Script and calling the module as "cals" here
import calculator_module as cals

user_input1 = int(input("enter number two value1: \n"))
user_input2 = int(input("enter number two value2: \n"))
user_cal = int(input("Select Valid Options \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n"))
#return_value = add(user_input1, user_input2)
if user_cal == 1:
    # calling "add" function from "cals" module, which is imported
    return_value = cals.add(user_input1, user_input2)
elif user_cal == 2:
    return_value = cals.sub(user_input1, user_input2)
elif user_cal == 3:
    return_value = cals.mul(user_input1, user_input2)
elif user_cal == 4:
    return_value = cals.div(user_input1, user_input2)
else:
    print("Not Valid Input Option")

print(return_value)

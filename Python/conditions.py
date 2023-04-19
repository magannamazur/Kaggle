# conditions are statements that are either True or False.
var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

# "if" statements
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(37))

# "if ... elif ... else" statements

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
print(evaluate_temp_with_elif(36))
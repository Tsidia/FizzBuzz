def FizzBuzz(target_number):
    if target_number < 1 or target_number > 100:
        return "Not a valid number"
    output = "" #This is what the function will return
    if target_number % 3 == 0: #If a multiple of three, add Fizz to output
        output += "Fizz"
    if target_number % 5 == 0: #If a multiple of five, add Buzz to output
        output += "Buzz"
    if output == "": #If neither Fizz nor Buzz is in the output, print number instead
        output += str(target_number)
    return output

for i in range(0, 102):
    print(FizzBuzz(i))
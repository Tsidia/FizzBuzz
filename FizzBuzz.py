import argparse

parser = argparse.ArgumentParser(description="A program that plays FizzBuzz")
parser.add_argument("-target", metavar="-t", type=int, default=100, help="The number to play up to")
parser.add_argument("-fizz", metavar="-f", type=int, default=3, help="The number to print Fizz on")
parser.add_argument("-buzz", metavar="-b", type=int, default=5, help="The number to print Buzz on")

def FizzBuzz(target_number=100, fizz=3, buzz=5):

    for i in range(target_number):
        output = "" #This is what the function will return
        if i % fizz == 0: #If a multiple of Fizz, add "Fizz" to output
            output += "Fizz"
        if i % buzz == 0: #If a multiple of Buzz, add "Buzz" to output
            output += "Buzz"
        if output == "": #If neither Fizz nor Buzz is in the output, print number instead
            output += str(i)
        print(output) # if target_number and fizz and buzz:

args = parser.parse_args()
FizzBuzz(args.target, args.fizz, args.buzz)

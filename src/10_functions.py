# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
      if num % 2 == 0:
              return True
      else:
              return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
num = int(input("Enter a number for countup: "))

# Defining a countdown function
def countdown(n):
  if n <= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n - 1)

# Defining a countup function
def countup(n):
  if n >= 0:
    print('Blastoff!')
  else:
    print(n)
    countup(n + 1)

# Cases depending on the sign of the input
if (num > 0):
  countdown(num)
elif num == 0:
  print("No ups and downs, sorry!")
else:
  countup(num)
MAX_LINES = 3

def deposit():
  while True:
    amount = input("How much do you want to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Please enter an actual amount in $")
    else:
        print("Please enter a valid amount in $")

  return amount
#  print(f"You deposited ${amount}")

def number_of_lines():
  while True:
    lines = input("How many lines of Slot do you want to bet on? (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter number of lines")
    else:
        print("Please enter a valid number")
  
  return lines
#  print(f"You entered {lines} lines")

def main() :
    balance = deposit()  
    lines = number_of_lines()
    print(balance, lines)  

main()

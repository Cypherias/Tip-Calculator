def get_float_input(prompt):
  while True:
      try:
          value = float(input(prompt))
          if value < 0:
              raise ValueError("Please enter a positive number.")
          return value
      except ValueError as e:
          print(e)

def get_int_input(prompt):
  while True:
      try:
          value = int(input(prompt))
          if value <= 0:
              raise ValueError("Please enter a positive integer.")
          return value
      except ValueError as e:
          print(e)

def tip_calculator():
  print("Tip Calculator Initialized")

  bill = get_float_input("What was the total bill amount? $")

  tip = get_float_input("How much tip would you like to give? (as a percentage) ")

  people = get_int_input("How many people to split the bill? ")

  tip_as_percent = tip / 100
  total_tip_amount = bill * tip_as_percent
  total_bill = bill + total_tip_amount
  bill_per_person = total_bill / people
  final_amount = round(bill_per_person, 2)

  print("\n--- Calculation Details ---")
  print(f"Total bill amount: ${bill:.2f}")
  print(f"Tip percentage: {tip}%")
  print(f"Total tip amount: ${total_tip_amount:.2f}")
  print(f"Total bill with tip: ${total_bill:.2f}")
  print(f"Number of people: {people}")
  print(f"Each person should pay: ${final_amount}")

tip_calculator()
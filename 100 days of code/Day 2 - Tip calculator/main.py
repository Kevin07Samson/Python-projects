print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to pay? 10 12 15"))
people = int(input("How many people to split the bill? "))
total_bill = bill + (bill * (tip/100))
totalbill_as_per_person = total_bill / people
final_amount = round(totalbill_as_per_person, 3)
print(f"Each pesron shoul pay: {totalbill_as_per_person}")
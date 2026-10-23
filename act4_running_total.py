#AQUINO HEAVEN
#BAET2102
#RUNNING TOTAL

running_total = 0
print("--- RUNNING TOTAL CALCULATOR ---")
print("Enter numbers to add them to the total. Type 0 to stop.")

while True:
    user_input = input("Enter a number: ")
    
    number = float(user_input)
    
    if number == 0:
        break
    
    running_total += number
    print(f"Current Total: {running_total}\n")

print("--- FINAL RESULT ---")
print(f"The final total is: {running_total}")

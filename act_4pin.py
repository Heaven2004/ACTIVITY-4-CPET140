#AQUINO HEAVEN
#BAET2102
#PIN LOCK

correct_pin = "0302"
attempts_left = 5

print("--- SECURE LOGIN SYSTEM ---")

while attempts_left > 0:
    user_input = input("Enter your PIN: ")
    
    if user_input == correct_pin:
        print("Access Granted! Welcome back.")
        break
    else:
        attempts_left -= 1
        print(f"Incorrect PIN. You have {attempts_left} attempts left.\n")

if attempts_left == 0:
    print("Too many incorrect attempts. Account locked.")




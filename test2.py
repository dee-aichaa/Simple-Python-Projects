y_ob = int(input("When is your year of birth?"))
if y_ob <= (1956):
    print("Your supposed to retire.")
elif y_ob > 1956:
    yr =  y_ob - 1956
    print(f"Your supposed to retire in",yr ,"years.")

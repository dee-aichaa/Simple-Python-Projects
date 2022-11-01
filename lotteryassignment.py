import random
def main():
    lottery = (int)(random.random()*100)
    print(lottery)
    guess_number = eval(input("Please guess a two digit number!"))
    lot_first = lottery // 10
    lot_last = lottery % 10
    guess_first = guess_number // 10
    guest_last = guess_number % 10

    if lottery == guess_number:
        print("You've won D20000")
    elif lot_first == guest_last and lot_last == guess_first:
        print("You've won D10000")
    elif guess_first == lot_first or guess_first == lot_last or guest_last == lot_first or guest_last == lot_last:
        print("You've won D2000")
main()
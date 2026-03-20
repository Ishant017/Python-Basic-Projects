while True:
    number = int (input("Pick the Secret Number :- "))
    print("\n" * 50)
    print("Start guessing the number... ")

    tries=0
    while True :
        guess = int(input("Take a guess: "))
        tries += 1

        if guess < number :
         print("Too Low")
        elif guess > number :
         print("Too High")
        else:
         print("You got it in " + str(tries) + " tries")
         break

    again = input("Play again? (yes / no): ").lower()
    if again != "yes":
     print("Thanks for playing ")
    break
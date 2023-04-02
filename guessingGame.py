import random
userNumber = 0
tries = 0
computerNumber = random.randint(1,9)
print(computerNumber)
while tries<5:
    print("Please type in your guess, between 1 and 9")
    userNumber = int(input())
    tries+=1
    if userNumber > computerNumber:
        print("Your guess was too high.")
        print("You have", 5-tries,"tries left.")
    elif userNumber < computerNumber:
        print("Your guess was too low.")
        print("You have", 5-tries,"tries left.")
    else:
        print("You have guessed correctly! You needed", tries,"tries to guess.")
        break
if computerNumber != userNumber:
    print("Unfortunately you did not guess the number in 5 tries.")
    print("The computer's number was",computerNumber)

    

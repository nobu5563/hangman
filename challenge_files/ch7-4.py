numbers = [11, 32, 33, 15, 1]

while True:
    a = input("Type a letter:")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("Please type a number or q t quit.")
    if a in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

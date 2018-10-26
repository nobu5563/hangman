import random

def hangman(word):
    wrong = 0           #何回間違えたか
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|/      ",
              "|     //       ",
              "|              "
              ]
    rletters = list(word)       #wordを1文字ずつの要素に分解してリストにしたもの
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman:)")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "predict a letter."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win.")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose. The answer is {}.".format(word))

hangman("twice")


# hangman game to show that I can build simple game app by myself

hangmanSteps = [
        """
                 \n
                 \n
                 \n
                 \n
                 \n
        _________\n
        """,
        """
                 \n
                 \n
                 \n
                 \n
           x     \n
        __x___ __\n
        """,
        """
                 \n
                 \n
                 \n
                 \n
           x x   \n
        __x___x__\n
        """,
        """
                 \n
                 \n
            I    \n
            I    \n
           x x   \n
        __x___x__\n
        """,
        """
                 \n
         ======= \n
            I    \n
            I    \n
           x x   \n
        __x___x__\n
        """,
        """ 
            X    \n
         ======= \n
            I    \n
            I    \n
           x x   \n
        __x___x__\n
        """

        ]

currentHangman = hangmanSteps[0]

computerAnswer = "dog"
userAnswer = ""
wrongChar = []

while userAnswer !=  computerAnswer and len(wrongChar) != len(hangmanSteps) - 1:
    for i in list(computerAnswer):
        userInput = input("Try to guess the character: \n")
        if userInput is i:
            userAnswer += userInput
            print(currentHangman)
            print(userAnswer)
        else:
            wrongChar.append(userInput)
            currentHangman = hangmanSteps[len(wrongChar)]
            print("wrong\n")
            print(currentHangman)

            # while loop if they get it incorrect again
            #while userInput != i and len(wrongChar) >= len(hangmanSteps) - 2:
            #    if userInput == i:
            #        break
            #    wrongChar.append(userInput)
            #    userInput = input("Wrong. Try again: \n")
            #    currentHangman = hangmanSteps[len(wrongChar)]
            #    print(currentHangman)
        if userAnswer == computerAnswer:
            break
        if len(wrongChar) == len(hangmanSteps) - 1:
            currentHangman = hangmanSteps[-1]
            print("Loser!")
            break


if userAnswer == computerAnswer and len(wrongChar) < len(hangmanSteps):
    print("You are a winner!\n")
    print("Your Hangman:\n")
    print(currentHangman)










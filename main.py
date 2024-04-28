#This function sets the background for the trivia questions and the introduction.
def background():
    rect = Rectangle(500, 500)
    rect.set_position(0, 0)
    rect.set_color(Color.red)
    add(rect)
    rect = Rectangle(360, 150)
    rect.set_position(20, 200)
    rect.set_color(Color.white)
    add(rect)


background()

#This function creates the text for the name of the game in a fancy font.
def text(text, x, y):
    txt = Text(text)
    txt.set_position(x, y)
    txt.set_color(Color.black)
    txt.set_font("25pt times")
    add(txt)


text("Are You Smarter Than", 40, 260)
text("A Middle Schooler?", 60, 300)


#This function creates the text for what this game was inspired by and gives credit.
def text2(text, x, y):
    txt = Text(text)
    txt.set_position(x, y)
    txt.set_color(Color.black)
    txt.set_font("8pt Arial")
    add(txt)


text2("Inspired by the 2007 game show: Are you smarter than a 5th grader?", 35, 340)

player_ready = input("Are you ready? ")
#This takes in whether the player is ready to play or not
if player_ready == "Yes":
    print("Click to start!")
else:
    print("Come back next time!")


#This is the text for the questions
def text3(text, x, y):
    txt = Text(text)
    txt.set_position(x, y)
    txt.set_color(Color.black)
    txt.set_font("12pt Arial")
    add(txt)


#This function displays the background, but also the question
def question1():
    background()
    text3("There are 50 cupcakes at the table. Fiona ate", 30, 230)
    text3("10 cupcakes. What percent of the cupcakes ", 30, 250)
    text3("did Fiona eat? ", 30, 270)

#This function is to check the user's answer and their number of attempts
def answer1(question1):
    guesses = 0
    answer1 = input("What is the answer? (Make sure to add a percentage sign!)")
    if answer1 == "20%":
        print("Correct! You got the 1st question!")
    else:
        for i in range(2):
            guess = input("Try again!")
            guesses += 1
            if guess == "20%":
                print("You got it!")
                break
        if guess != "20%":
            print("You have reached 3 attempts.")
            print("The answer was 20%.")

def question2():
    background()
    text3("What is the periodic table symbol of oxygen?", 30, 230)

def answer2(question2):
    guesses = 0
    answer2 = input("What is the answer?")
    if answer2 == "O":
        print("Great job on the 2nd question! Click for the next question.")
    else:
        for i in range(2):
            guess = input("Incorrect. Try again!")
            guesses += 1
            if guess == "O":
                print("Terrific Job!")
                break
        if guess != "O":
            print("You have reached the maximum number of attempts.")
            print("The answer was O.")

def question3():
    background()
    text3("What is the process of changing a liquid to a ", 30, 230)
    text3("solid? Type in A, B, C or D from the ", 30, 250)
    text3("choices below in the list.", 30, 270)
    print(" ")
    mc1 = ["A. Freezing", "B. Melting", "C. Condensation", "D. Vaporization"]
    print(mc1)

def answer3(question3):
    guesses = 0
    answer3 = input("What is the answer? (Type in A, B, C or D)")
    if answer3 == "A":
        print("That's right!")
    else:
        for i in range(2):
            guess = input("Incorrect. Try again")
            guesses += 1
            if guess == "A":
                print("Hurray! On to the next one!")
                break
        if guess != "A":
            print("You have reached the max number of attempts.")
            print("The answer was A. Freezing.")

def question4():
    background()
    text3("At a clearance sale, the price of the PS5 has ", 30, 230)
    text3("a discount of 20%. The discount price is $350. ", 30, 250)
    text3("What was the original price of the PS5? ", 30, 270)

def answer4(question4):
    guesses = 0
    answer4 = input("What is the answer? (Be sure to include the money sign!)")
    if answer4 == "$420":
        print("You're a natural at this!")
    else:
        for i in range(2):
            guess = input("Not quite the right answer. Try again!")
            guesses += 1
            if guess == "$420":
                print("Good Job!")
                break
        if guess != "$420":
            print("You have reached 3 attempts.")
            print("The answer was $420.")

def question5():
    background()
    text3("The area of the rectangular paper is 40cm. ", 30, 230)
    text3("The perimeter is 26cm. What are the dimensions ", 30, 250)
    text3("of the rectangle? (Type in A, B, C or D) ", 30, 270)
    print(" ")
    mc2 = ["A. 5cm x 10cm", "B. 5cm x 8cm", "C. 8cm x 5cm", "D. 10cm x 5cm"]
    print(mc2)

def answer5(question5):
    guesses = 0
    answer5 = input("Which answer from the list below is the answer?")
    if answer5 == "B":
        print("You're a math magician! Great Job!")
    else:
        for i in range(2):
            guess = input("It's a hard one, but try again!")
            guesses += 1
            if guess == "B":
                print("You did it!")
                break
        if guess != "B":
            print("You have reached 3 attempts!")
            print("The answer is B. 5cm x 8cm.")

def question6():
    background()
    text3("Who was the 4th president of the USA?", 30, 230)

def answer6(question6):
    guesses = 0
    answer6 = input("What's the answer?")
    if answer6 == "James Madison":
        print("You know your presidents! Good job.")
    else:
        for i in range(2):
            guess = input("Incorrect. Try again.")
            guesses += 1
            if guess == "James Madison":
                print("Good job!")
                break
        if guess != "James Madison":
            print("You have reached the maximum amount of attempts.")
            print("The answer was James Madison.")

def question7():
    background()
    text3("The 19th Amendment guarantees who the right ", 30, 230)
    text3("to vote? ", 30, 250)
    print(" ")
    mc3 = ["A. Animals", "B. Children", "C. Men", "D. Women"]
    print(mc3)

def answer7(question7):
    guesses = 0
    answer7 = input("What is the answer? Pick from the list of answer choices.")
    if answer7 == "D":
        print("Correct Answer!")
    else:
        for i in range(2):
            guess = input("No quite right, try again!")
            guesses += 1
            if guess == "D":
                print("You know your rights!")
                break
        if guess != "D":
            print("You have reached 3 attempts.")
            print("The answer was D. Women.")

def question8():
    background()
    text3("What is the proper noun in the sentence: ", 30, 230)
    text3("My favorite place to eat at is Chipotle.", 30, 250)

def answer8(question8):
    guesses = 0
    answer8 = input("What is the answer?")
    if answer8 == "Chipotle":
        print("That's right! You know your grammar rules.")
    else:
        for i in range(2):
            guess = input("Not quite right, try again.")
            guesses += 1
            if guess == "Chipotle":
                print("Great job! You know your grammar rules.")
                break
        if guess != "Chipotle":
            print("You have reached the maximum number of attempts.")
            print("The answer was Chipotle.")

def question9():
    background()
    text3("Who was the physicist who discovered the ", 30, 230)
    text3("three laws of motion? Type A,B,C or D.", 30, 250)
    print(" ")
    mc4 = ["A. Albert Einstein", "B. Stephen Hawking", "C. Isaac Newton", "D. Galileo Galilei"]
    print(mc4)

def answer9(question9):
    guesses = 0
    answer9 = input("Which answer from the list below is the answer? Type A, B, C, or D.")
    if answer9 == "C":
        print("Correct! You're really smart!")
    else:
        for i in range(2):
            guess = input("It's a hard one, but try again!")
            guesses += 1
            if guess == "C":
                print("You did it!")
                break
        if guess != "C":
            print("You have reached 3 attempts!")
            print("The answer is C. Isaac Newton.")

def question10():
    background()
    text3("Who lead the American Slave Rebellion in the ", 30, 230)
    text3("year 1831? ", 30, 250)
    print(" ")
    mc5 = ["A. William Lloyd Garrison", "B. Fredrick Douglas", "C. Nat Turner", "D. John Brown"]
    print(mc5)

def answer10(question10):
    guesses = 0
    answer10 = input("What is the answer? (Pick A, B, C, or D) ")
    if answer10 == "C":
        print("Correct Answer!")
    else:
        for i in range(2):
            guess = input("No quite right, try again!")
            guesses += 1
            if guess == "C":
                print("Your history is on point!")
                break
        if guess != "C":
            print("You have reached 3 attempts.")
            print("The answer was C. Nat Turner.")

#This function sets the background for the end of the game.
def background2():
    rect = Rectangle(500, 500)
    rect.set_position(0, 0)
    rect.set_color(Color.blue)
    add(rect)
    rect = Rectangle(360, 150)
    rect.set_position(20,200)
    rect.set_color(Color.white)
    add(rect)

#This function creates the ending of the game and how it looks.
def ending():
    background2()
    text("Congratulations! ", 40, 250)
    text("You finished the game!", 60, 290)
    text("And you're a genius!", 80, 330)

scene_counter = 0

#This function allows for the mouse clicks to move to the next question
#This function is from CodeHS,with alterations made to suite our program
def next_question(x, y):
    global scene_counter
    scene_counter += 1
    if scene_counter == 1:
        question1()
    elif scene_counter == 2:
        answer1(question1)
        question2()
    elif scene_counter == 3:
        answer2(question2)
        question3()
    elif scene_counter == 4:
        answer3(question3)
        question4()
    elif scene_counter == 5:
        answer4(question4)
        question5()
    elif scene_counter == 6:
        answer5(question5)
        question6()
    elif scene_counter == 7:
        answer6(question6)
        question7()
    elif scene_counter == 8:
        answer7(question7)
        question8()
    elif scene_counter == 9:
        answer8(question8)
        question9()
    elif scene_counter == 10:
        answer9(question9)
        question10()
    elif scene_counter == 11:
        answer10(question10)
        ending()

add_mouse_click_handler(next_question)
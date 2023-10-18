# here I am getting the user inputs for test score and class rank
studentName = input("Type your name here")
questionOne = input("What is 1 + 2?")

# then I am converting the string to integer with the int function
answerOne = int(questionOne)

# The rest of the code checks the admissions acceptance
# if the score is greater than or equal to 90, and the classrank is greater or equal to 25
if answerOne == 3:
    score1 = 0
    print("True")
else:
    print("False")
    score1 = 1

scoreOne = str(score1)

print("Chris's Score is " + scoreOne + " Out of 10")
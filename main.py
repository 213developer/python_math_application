#Here I'm importing the random function
#This enables me to call the function later
import random

#Here I'm generating 10 random numbers and assigning them as variables
random1 = random.randint(0, 10)
random2 = random.randint(0, 10)
random3 = random.randint(0, 10)
random4 = random.randint(0, 10)
random5 = random.randint(0, 10)
random6 = random.randint(0, 10)
random7 = random.randint(0, 10)
random8 = random.randint(0, 10)
random9 = random.randint(0, 10)
random10 = random.randint(0, 10)

print(random1)
# print(random.randint(0, 10))

#Here I'm getting the student to input their name
studentName = input("Type your name here")

random1 = random.randint(0, 10)

#Now I'm going to get the student tp input the answers
questionOne = input("What is 1 + 2?")
questionTwo = input("What is 2 + 2?")


# then I am converting the string to integer with the int function
answerOne = int(questionOne)
answerTwo = int(questionTwo)


#Question 1 Logic
if answerOne == 3:
    score1 = 1
    print("answerOne is True")
else:
    print("answerOne is False")
    score1 = 0

#Question 2 Logic

if answerTwo == 4:
    score2 = 1
    print("answerTwo is True")
else:
    print("answerTwo is False")
    score2 = 0


# Here I'm going to total up the score from each answers
totalScore = score1 + score2
# The convert the integer to a string
totalScoreString = str(totalScore)
#crate a decimal score
decimalScore = totalScore/10
#convert to string
decimalScoreString = str(decimalScore)
#convert a percentage score
percentageScore = (totalScore/10)*100
percentageScoreString = str(percentageScore)
# Then concatenate the string to print the students score
print("Chris scored " + totalScoreString + " Out of 10 correct, with a decimal score of " + decimalScoreString + " and a percentage score of " + percentageScoreString + "%")

print("Welcome to Quiz!")

text = "Program is NOT case sensitive!"
print(text.lower())
print(text.upper())

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print ("Okay! Let's play! ")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SQL stands for? ")
if answer.lower() == "structured query language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does OOP stands for? ").lower()
if answer == "object oriented programming":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPP stands for? ").lower()
if answer == "c plus plus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/7)*100) + "% questions correct!")

if ((score/7)*100) >= 5:
    print("Keep it up!")
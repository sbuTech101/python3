print("Welcome to my computer game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay! lets play :)")
score = 0

answer = input("When was windows first developed? ")
if answer.lower() == "windows was first developed in 1992":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the developer of linux? ")
if answer.lower() == "linus torvalds":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what are the 3 different types of hackers? ")
if answer.lower() == "white hat hackers":
    if answer.upper() == "Grey hat hackers":
        if answer.upper() == "black hat hackers":
            if answer.upper() == "blue hat hackers":
                print('correct!')
                score += 3
else:
    print("Incorrect!")

answer = input("what programming language has a blue and yellow logo? ")
if answer.lower() == "python":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What allocates address to machines? ")
if answer.lower() == "dhcp":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what is the NAC ?")
if answer.lower() == "network access controller":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

print("You got" + str (score) + "questions correct!")
print("you got" + str ((score / 6)*100) + "%")

import random
import sys
from tabulate import tabulate

animals = {
     1 : {"animal": "monkey", "temp": "hot", "level": "land", "diet" : "herbivore", "type" : "mammal"},
     2 : {"animal": "whale", "temp": "cold", "level": "sea", "diet" : "herbivore", "type" : "fish"},
     3 : {"animal": "lion", "temp": "hot", "level": "land", "diet" : "carnivore", "type" : "mammal"},
     4 : {"animal": "elephant", "temp": "hot", "level": "land", "diet": "herbivore", "type": "mammal"},
     5 : {"animal": "shark", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "fish"},
     6 : {"animal": "penguin", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "bird"},
     7 : {"animal": "eagle", "temp": "hot", "level": "air", "diet": "carnivore", "type": "bird"},
     8 : {"animal": "frog", "temp": "cold", "level": "land", "diet": "carnivore", "type": "amphibian"},
     9 : {"animal": "snake", "temp": "hot", "level": "land", "diet": "carnivore", "type": "reptile"},
     10 : {"animal": "crocodile", "temp": "hot", "level": "sea", "diet": "carnivore", "type": "reptile"},
     11 : {"animal": "bee", "temp": "hot", "level": "air", "diet": "herbivore", "type": "insect"},
     12 : {"animal": "zebra", "temp": "hot", "level": "land", "diet": "herbivore", "type": "mammal"},
     13 : {"animal": "polar bear", "temp": "cold", "level": "land", "diet": "carnivore", "type": "mammal"},
     14 : {"animal": "dolphin", "temp": "hot", "level": "sea", "diet": "carnivore", "type": "mammal"},
     15 : {"animal": "tiger", "temp": "hot", "level": "land", "diet": "carnivore", "type": "mammal"},
     16 : {"animal": "octopus", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "invertebrate"},
     17 : {"animal": "ant", "temp": "hot", "level": "land", "diet": "omnivore", "type": "insect"},
     18 : {"animal": "owl", "temp": "cold", "level": "air", "diet": "carnivore", "type": "bird"},
     19 : {"animal": "turtle", "temp": "cold", "level": "sea", "diet": "herbivore", "type": "reptile"},
     20 : {"animal": "kangaroo", "temp": "hot", "level": "land", "diet": "herbivore", "type": "mammal"},
     21 : {"animal": "salmon", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "fish"},
     22 : {"animal": "flamingo", "temp": "hot", "level": "land", "diet": "omnivore", "type": "bird"},
     23 : {"animal": "giraffe", "temp": "hot", "level": "land", "diet": "herbivore", "type": "mammal"},
     24 : {"animal": "chameleon", "temp": "hot", "level": "land", "diet": "carnivore", "type": "reptile"},
     25 : {"animal": "butterfly", "temp": "hot", "level": "air", "diet": "herbivore", "type": "insect"},
     26 : {"animal": "seal", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "mammal"},
     27 : {"animal": "parrot", "temp": "hot", "level": "air", "diet": "omnivore", "type": "bird"},
     28 : {"animal": "spider", "temp": "hot", "level": "land", "diet": "carnivore", "type": "invertebrate"},
     29 : {"animal": "hedgehog", "temp": "cold", "level": "land", "diet": "omnivore", "type": "mammal"},
     30 : {"animal": "jellyfish", "temp": "cold", "level": "sea", "diet": "carnivore", "type": "invertebrate"}
}


def get_username():
#lets a user input a username
    try:
        username = sys.argv[2]
        print(f"Username confirmed as {username}\n")
    except IndexError:
        print("No name entered, username will be 'Unknown' ")
        username = "Unknown"
    return username
    

def get_difficulty():
#gives a random animal based on a given difficulty
    answer_value = random.randint(1,20)
    difficulty = "medium"
    try:
        level = sys.argv[1]
        if level == "easy":
            answer_value = random.randint(1,10)
            print("Difficulty set to easy.\n")
            difficulty = "easy"
        elif level == "medium":
            answer_value = random.randint(1,20)
            print("Difficulty set to medium.\n")
            difficulty = "medium"
        elif level == "hard":
            answer_value = random.randint(1,30)
            print("Difficulty set to hard.\n")
            difficulty = "hard"
        else:
            print("Not a difficulty level, automatically set to medium.\n")
    except IndexError:
        print("No difficulty level provided, automatically set to medium.\n")
    return answer_value, difficulty


def high_scores(guesses, username, difficulty):
#outputs the 5 best scores
    headers = ["Username","Guesses","Difficulty"]
    scores = [
    ]
    with open("board.csv", "a") as file:
        file.write(f"{username},{guesses},{difficulty}\n")
    with open("board.csv") as file:
        scoreboard = file.readlines()
        for line in scoreboard:
            scores.append([line[:line.find(",")],int(line[line.find(",")+1:line.rfind(",")]),line[line.rfind(",")+1:]])
    scores = sorted(scores, key=lambda x: x[1])
    scores = scores[:5]
    print(tabulate(scores, headers, tablefmt="grid"))


def main():
#defines necessary variables
    result = get_difficulty()
    answer_value = result[0]
    difficulty = result[1]
    username = get_username()
    answer = animals[answer_value]["animal"]
    guesses = 1
#prints rules
    print("Rules:\nAn animal will be generated at random from the list of animals")
    print("You will 6 guesses to guess the animal\nCorrect and incorrect attributes will be shown")
    print("Have Fun!")
    while guesses <= 6:
        try:
#prints list of possible animals based on difficulty
            guess = input("Guess an animal: ").strip().lower()
            if guess == "list":
                if difficulty == "easy":
                    animal_amount = 10
                if difficulty == "medium":
                    animal_amount = 20
                if difficulty == "hard":
                    animal_amount = 30
                print("Here is the list of animals at your difficulty level")
                for i in range(animal_amount):
                    print(animals[i + 1]["animal"])
#output if guess is correct
            else:
                try:
                    if guess == answer:
                        if guesses == 1:
                            print("You got it right on the first guess wow!! 🎉🎉")
                        else: 
                            print(f"You got it right in {guesses} guesses!! 🎉🎉")
                        
                        high_scores(guesses, username, difficulty)
                        break
#prints whether animal characteristics match
                    else: 
                        result1 = matches(get_value(guess),answer_value)
                        print(f"{result1[0]}\n{result1[1]}\n{result1[2]}\n{result1[3]}\n")
                        guesses += 1
                except KeyError:
                    print("Not an animal in the database ⚠️")
#give up function
        except EOFError:
            print(f"Good try, the chosen animal was the {answer}")
#loss if too many guesses
    if guesses > 6:
        high_scores(guesses, username, difficulty)
        print(f"You ran out of tries. The chosen animal was the {answer}")

        
def get_value(guess):
#finds respective number in list of animal
    for name, attributes in animals.items():
        if guess == attributes["animal"]:
            return name


def matches(guess_value, answer_value):
#compares guess stats to answer stats returns emojis
    if animals[guess_value]["temp"] == animals[answer_value]["temp"]:
        temp = "🌡️  ✅"
    else: temp = "🌡️  ❌"
    if animals[guess_value]["level"] == animals[answer_value]["level"]:
        level = "⛰️  ✅"
    else: level = "⛰️  ❌"
    if animals[guess_value]["diet"] == animals[answer_value]["diet"]:
        diet = "🍽️  ✅"
    else: diet = "🍽️  ❌"
    if animals[guess_value]["type"] == animals[answer_value]["type"]:
        type = "👤  ✅"
    else: type = "👤  ❌"
    return temp, level, diet, type


if __name__ == "__main__":
    main()


        



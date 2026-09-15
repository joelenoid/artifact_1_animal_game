from animal_game import matches, get_value

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

def test_matches():
    assert matches(4, 12) == ("🌡️  ✅","⛰️  ✅","🍽️  ✅","👤  ✅")
    assert matches(4, 9) == ("🌡️  ✅","⛰️  ✅","🍽️  ❌","👤  ❌")
    assert matches(30, 27) == ("🌡️  ❌","⛰️  ❌","🍽️  ❌","👤  ❌")
    temp, level, diet, type_ = matches(1, 20)
    assert temp == "🌡️  ✅"
    assert level == "⛰️  ✅"
    assert diet == "🍽️  ✅"
    assert type_ == "👤  ✅"

def test_get_value():
    assert get_value("monkey") == 1
    assert get_value("zebra") == 12
    assert get_value("spider") == 28
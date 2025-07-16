import random

print("\nlets play a version of 20 question\n")

#                  MAIN VARIABLES

possible_guesses = [
    "tree","grass","river","mountain","flower",   
    "elephant","tiger","giraffe","monkey","hawk",
    "paris","school","zoo","italy","park",
    "burger","cracker","banana","pizza","carrot"
    ]

facts = {
#                       animals
    "elephant":{"is_animal": True, "is_nature": True, "is_place": False,
                 "is_food":False, "is_alive":True,"can_fly":False,
                 "has_legs": True
                 },
    "tiger":{"is_animal": True, "is_nature": True, "is_place": False,
              "is_food":False, "is_alive":True,"can_fly":False,
              "has_legs": True
              },
    "giraffe":{"is_animal": True, "is_nature": True,"is_place": False,
                "is_food":False, "is_alive":True,"can_fly":False,
                "has_legs": True
                },
    "monkey":{"is_animal": True, "is_nature": True,"is_place": False,
               "is_food":False, "is_alive":True,"can_fly":False,
               "has_legs": True
               },
    "hawk":{"is_animal": True, "is_nature": True, "is_place": False,
             "is_food":False, "is_alive":True,"can_fly":True,
             "has_legs": False
             },
#                         nature
    "tree": {"is_animal": False, "is_nature": True, "is_place": False,
              "is_food": False, "is_alive": True,"can_fly":False,
              "has_legs": False
              },
    "grass": {"is_animal": False, "is_nature": True, "is_place": False,
               "is_food": False, "is_alive": True,"can_fly":False,
               "has_legs": False
               },
    "river": {"is_animal": False, "is_nature": True, "is_place": False,
               "is_food": False, "is_alive": False,"can_fly":False,
               "has_legs": False
               },
    "mountain": {"is_animal": False, "is_nature": True, "is_place": False,
                  "is_food": False, "is_alive": False,"can_fly":False,
                  "has_legs": False
                  },
    "flower": {"is_animal": False, "is_nature": True, "is_place": False,
                "is_food": False, "is_alive": True,"can_fly":False,
                "has_legs": False
                },
#                          places
    "paris": {"is_animal": False, "is_nature": False, "is_place": True,
               "is_food": False, "is_alive": False,"can_fly":False,
               "has_legs": False
               },
    "school": {"is_animal": False, "is_nature": False, "is_place": True,
                "is_food": False, "is_alive": False,"can_fly":False,
                "has_legs": False
                },
    "zoo": {"is_animal": False, "is_nature": False, "is_place": True,
             "is_food": False, "is_alive": False,"can_fly":False,
             "has_legs": False
             },
    "italy": {"is_animal": False, "is_nature": False, "is_place": True,
               "is_food": False, "is_alive": False,"can_fly":False,
               "has_legs": False
               },
    "park": {"is_animal": False, "is_nature": True, "is_place": True,
              "is_food": False, "is_alive": False,"can_fly":False,
              "has_legs": False
              },
#                           food
    "burger": {"is_animal": False, "is_nature": False, "is_place": False,
                "is_food": True, "is_alive": False,"can_fly":False,
                "has_legs": False
                },
    "cracker": {"is_animal": False, "is_nature": False, "is_place": False,
                 "is_food": True, "is_alive": False,"can_fly":False,
                 "has_legs": False
                 },
    "banana": {"is_animal": False, "is_nature": True, "is_place": False,
                "is_food": True, "is_alive": True,"can_fly":False,
                "has_legs": False
                },
    "pizza": {"is_animal": False, "is_nature": False, "is_place": False,
               "is_food": True, "is_alive": False,"can_fly":False,
               "has_legs": False
               },
    "carrot": {"is_animal": False, "is_nature": True, "is_place": False,
                "is_food": True, "is_alive": True,"can_fly":False,
                "has_legs": False
                }

    }

secret_answer = random.choice(possible_guesses)

questions_asked = 0

max_questions = 20

#               FUNCTIONS!!

def answer_question(fact_key):
#               checks if the answers applys and creating responces for the player
    if facts[secret_answer][fact_key]:
        print("yes")
    else:
        print("no")
    
    global questions_asked
    questions_asked += 1
    print("remaining questions:", max_questions - questions_asked)
#               MAIN GAME LOOP

while questions_asked < max_questions:
    question = input("\nAsk a yes or no question or type 'guess':\n").lower()
    if question == "guess":
        guess = input("\nwhat is your guess\n")
        if guess == secret_answer:
            print("\ncongradulations you have guessed the answer;",secret_answer+",great job\n")
            break
        else:
            print("\nsorry thats not it\n")
            questions_asked += 1
            print("remaining questions:", max_questions - questions_asked)
            continue
    
    elif "animal" in question:
        answer_question("is_animal")

    elif "nature" in question:
        answer_question("is_nature")

    elif "place" in question:
        answer_question("is_place")
   
    elif "food" in question:
        answer_question("is_food")
    
    elif "alive" in question:
        answer_question("is_alive")
    
    elif "fly" in question:
        answer_question("can_fly")
    
    elif "leg" in question:
        answer_question("has_legs")
    
    else:
        print("sorry thats not in the database")
        questions_asked += 1
        print("remaining questsions:",max_questions - questions_asked)

if questions_asked >= max_questions:
    print("\n🛑 Game over! You used all your questions.")
    print("The correct answer was:", secret_answer)
    







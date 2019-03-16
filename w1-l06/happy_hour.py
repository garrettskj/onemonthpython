import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Arthur Friend",
          "Samuel L. Jackson"]

random_bar = random.choice(bars)
random_personA = random.choice(people)
random_personB = random.choice(people)

print(f"How about you go to {random_bar} with {random_personA} and {random_personB}")

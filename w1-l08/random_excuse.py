import random

activity = ["Fishing",
        "Flying",
        "Fighting",
        "Free-falling",
        "Farming",
        "Farting",
        "Fapping"]

excuse = ["Sneezing",
          "Sleeping",
          "Snacking",
          "Slurping",
          "Sighing",
          "Snoring"]

companion = ["Michael",
          "Mark",
          "Maddie",
          "Michelle",
          "Morgan",
          "Mickey"]

random_friend = random.choice(companion)
random_activity = random.choice(activity)
random_excuse = random.choice(excuse)

print(f"Sorry, I can\'t go {random_activity} because I am busy {random_excuse} with {random_friend}.")

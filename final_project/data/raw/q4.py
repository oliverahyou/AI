#q4='Please share your thoughts on coffee (q3)' answer=Open-End

import random
import csv

random.seed(42)

emojis = [
    "", "", "", "", "☕", "😊", "😍", "👍", "😕", "🤔",
    "😅", "❤️", "😋", "👌", "👎"
]

typos = {
    "coffee": ["cofee", "coffe"],
    "definitely": ["definately", "definetly"],
    "recommend": ["reccomend", "recomend"],
    "flavor": ["flavour", "flavourr"],
    "because": ["becuase", "becoz"],
    "really": ["realy", "rly"],
    "great": ["gr8"],
    "quality": ["qualty"],
    "package": ["pakage"],
    "fresh": ["fesh"]
}

positive = [
    "Love this coffee",
    "Really enjoying Coffee X",
    "Best coffee I've had in a while",
    "Super smooth taste",
    "Amazing aroma",
    "Worth every penny",
    "My morning feels incomplete without it",
    "Very balanced flavour",
    "The beans smell fantastic",
    "I'll definitely buy again"
]

negative = [
    "Too bitter for me",
    "Didn't enjoy the aftertaste",
    "Expected better",
    "Way too expensive",
    "Packaging could be better",
    "Coffee arrived stale",
    "Not as fresh as expected",
    "Taste is kinda weak",
    "Bit disappointed",
    "Wouldn't buy again"
]

mixed = [
    "Taste is nice but it's a bit pricey.",
    "Love the aroma, not a fan of the aftertaste.",
    "Packaging looks premium but freshness could improve.",
    "Pretty good overall although I expected a stronger roast.",
    "Works great with milk but black coffee isn't my favourite."
]

extras = [
    "",
    "",
    "",
    "Would recommend it to friends.",
    "Hope you keep the quality consistent.",
    "Please introduce more roast options.",
    "Would love a decaf version.",
    "Customer service was great too.",
    "Delivery was really fast.",
    "I drink it every morning.",
    "Not bad at all tbh.",
    "imo it's one of the better brands.",
    "ngl I expected more."
]

short = [
    "Love it ☕",
    "Pretty good!",
    "Not bad.",
    "Amazing 😍",
    "Could be better.",
    "Meh.",
    "10/10 ❤️",
    "Too expensive 😕",
    "Yumm 😋",
    "It's okay."
]

def typo(sentence):
    words = sentence.split()
    for i, w in enumerate(words):
        key = w.lower().strip(".,!")
        if key in typos and random.random() < 0.12:
            words[i] = random.choice(typos[key])
    return " ".join(words)

responses = set()

while len(responses) < 250:

    style = random.random()

    if style < 0.15:
        text = random.choice(short)

    elif style < 0.55:
        text = random.choice(positive)
        if random.random() < 0.8:
            text += ". " + random.choice(extras)

    elif style < 0.80:
        text = random.choice(negative)
        if random.random() < 0.8:
            text += ". " + random.choice(extras)

    else:
        text = random.choice(mixed)
        if random.random() < 0.7:
            text += " " + random.choice(extras)

    text = typo(text)

    if random.random() < 0.45:
        text += " " + random.choice(emojis)

    responses.add(text.strip())

with open("feedback_data.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["RespondentID","Feedback"])

    for i, r in enumerate(responses, start=1):
        writer.writerow([i, r])

print("Generated", len(responses), "responses.")
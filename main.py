import json
import random

with open("data.json", "r") as file:
    data = json.load(file)

def get_tag(message):
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if message.lower() == pattern.lower():
                return intent["tag"]
    return None

def get_resp(tag):
    for intent in data["intents"]:
        if tag == intent["tag"]:
            return random.choice(intent["responses"])
    return None

if __name__ == "__main__":
    is_running = True
    while is_running:
        message = input("You: ")

        if message.lower() == "quit":
            is_running = False
            break
        tag = get_tag(message)
        resp = get_resp(tag)
        if resp is not None:
            print(f"Croan: {resp}")
        else:
            print("Croan: I don't know how to respond.")

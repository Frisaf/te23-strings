print("You wake up after a long night's sleep...")
print("Strangely enough, you find yourself in a hamster's body where you run across a field hunting for a golden dandelion.")
print("You flinch and freeze in your thoughts. Do you look at the [dandelion] or your mysterious [hamster] body?")

inventory = []

options = [
    "Look at the dandelion",
    "Look at your mysterious hamster body",
    "Stare out into nothing",
]

while True:
    for index, option in enumerate(options):
        print(f"[{index + 1}] {option}")
    
    answer = int(input("> "))

    if 1 <= answer <= len(options):
        choice = options[answer - 1]

        if choice == "Look at the dandelion":
            print("You scream inside like the allergic person you are.")

            inventory.append("dandelion")
            break
        
        elif choice == "Look at the mysterious hamster body.":
            print("In dream-like slow motion, you admire the amazing fluffyness. You sense wheat and dust.")
            break

        elif choice == "Stare out into nothing":
            print("You stare into nothing")

            options.pop(2)

print("You suddenly feel very drawn to the dandelion, as if you are becoming one with it. Reach out and touch the dandelion? (yes/no)")

while True:
    answer = input("> ")

    if answer.startswith("y") and answer.endswith("es"): # Egentligen ett superdummt sätt att skriva if answer == "yes", men du ville att vi skulle använda olika operatorer så liksom... (shrug emoji)
        print("You suddenly feel taller, and a lot less fluffy and a lot slimmer. You also realise that you can't see anything. Just feel. You have become the dandelion.")
        break

    elif answer.startswith("n") and answer.endswith("o"):
        print("You resist the urge and continue your way forwards, across the field, continuing your life as a happy hamster.")
        break
    
    else:
        print("Please provide a valid answer (yes or no)")
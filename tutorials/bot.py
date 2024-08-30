name = input("Hi, what is your name?: ")
print(f"\nHello, {name}! It's nice to meet you.\n")


while True:
    roboat_response = input("Do you love being a part of the Ro-boats? (yes or no): ")

    if roboat_response.lower() == "yes":
        print(f"\nAwesome, {name}! We're happy you're here!")
        break
    elif roboat_response.lower() == "no":
        print(f"\nI'm sorry to hear that, {name}. More fun for us, I guess.")
        break
    else:
        print(
            f"\nAre you okay, {name}? I'm not quite sure I understand. Let's try again.\n"
        )

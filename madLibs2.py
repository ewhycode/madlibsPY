def mad_libs():
    #oneliner storey creater
    #ask user input
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")
    verb2 = input("Enter another verb: ")
    noun3 = input("Enter one more noun: ")

    #template line
    story = f"Once upon a time, there was a {adjective1} {noun1}. "
    story += f"It loved to {verb1} every day. "
    story += f"One day, it met a {adjective2} {noun2}. "
    story += f"They decided to {verb2} together. "
    story += f"As they were {verb2}ing, they found a {noun3}. "
    story += f"The {noun1} and the {noun2} became best friends and lived happily ever after."

    #print
    print("\nHere's your Mad Libs story:")
    print(story)

# Run the Mad Libs Generator
mad_libs()
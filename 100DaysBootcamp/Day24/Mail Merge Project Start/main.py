# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

name_list = []
search_text = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    d_name_list = names.readlines()

for name in d_name_list:
    name_list.append(name.translate({ord('\n'): None}))
    # name_list.append(name.strip())  // Used method in solution

for name in name_list:
    with open("./Input/Letters/starting_letter.txt") as start_letter:
        data = start_letter.read()
        data = data.replace(search_text, name)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as finished_letter:
        finished_letter.write(data)

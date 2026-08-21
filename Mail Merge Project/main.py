
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()

for name in names:
    name = name.strip()
    my_letter = letter_content.replace("[name]", name)

    with open("Output/ReadyToSend/" + "letter_for_" + name + ".txt","w") as letter_file:
        letter_file.write(my_letter)


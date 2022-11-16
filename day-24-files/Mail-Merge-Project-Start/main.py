PLACEHOLDER = '[name]'

with open(file='Input/Names/invited_names.txt', mode='r') as inv_names:
    names = inv_names.readlines()

with open(file='Input/Letters/starting_letter.txt') as letter_blueprint:
    blueprint_contents = letter_blueprint.read()
    for name in names:
        stripped_name = name.strip()
        letter = blueprint_contents.replace(PLACEHOLDER, stripped_name)
        with open(file=f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as new_letter:
            new_letter.write(letter)



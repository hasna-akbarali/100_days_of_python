with open('Input/Names/invited_names.txt', 'r') as names:
    for name in names:
        with open('Input/Letters/starting_letter.txt', 'r') as letters:
            with open(f'Input/Names/letter_for_{name.strip()}.txt','w') as letter_for_name :
                for lines in letters:
                    letter_for_name.write(lines.replace('[name],', f'{name.strip()},'))


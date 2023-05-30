def get_user_choice(options):    # get_user_choice takes one argument, a list of strings (menu options)
    while True:
        s = input(f'Enter one of {options}: ').strip()

        if s in options:             # did the user choose an option that was in options?  Return it!
            return s

        print('Bad choice; try again')
    
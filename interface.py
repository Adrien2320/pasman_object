def show_main_menu() -> None:
    """affiche le principale de l'application"""

    # initiate the show of main menu.
    print("enregistrement de mots de passe".center(100, "_"),
          "\n"
          "\n1. connexion"
          "\n2. creation nouvelle utilisateur"
          "\n"
          "\n0. quitter"
          )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            exit()
            print("Au revoir")
        case 1:
            # todo function connexion
        case 2:
            # todo function create new user()
        case _:
            print("Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 2.")
            show_main_menu()


def number_by_user() -> int:
    """Demande un nombre à l'utilisateur et return le nombre """
    # type and assign.
    prompt: str = ""
    # check if the enter number is a number or not.
    while not prompt.isdigit():
        prompt = input("choix:")
    # return the select number by user.
    return int(prompt)
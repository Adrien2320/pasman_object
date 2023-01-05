import metier
def show_main_menu() -> None:
    """affiche le principale de l'application"""

    # type and assign
    answer : tuple
    login : str
    password : str

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
            pass
            # todo function connexion
        case 2:
            answer = request_name_and_password()
            login = answer[0]
            password = answer[1]
            metier.create_new_user(login,password)
            # todo interface choix entre menu user ou menu coffre
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

def request_name_and_password()->tuple:
    """Demande à l'user un nom et un mot de passe et return un tuple (login,password)"""
    # initiate show
    print("formulaire demande pseudo et mot de passe".center(100,"-"))
    # type and assign
    login : str = input("pseudo:")
    password : str = input("mot de passe:")
    return login,password
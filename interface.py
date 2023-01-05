import data
import metier


def show_main_menu() -> None:
    """affiche le principale de l'application"""

    # type and assign
    answer: tuple
    login: str
    password: str
    user: data.User

    # initiate the show of main menu.
    print(
        "Passman".center(100, "_"),
        "\n" "\n1. connexion" "\n2. creation nouvelle utilisateur" "\n" "\n0. quitter",
    )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            exit()
            print("Au revoir")
        case 1:
            answer = request_name_and_password()
            login = answer[0]
            password = answer[1]
            user = metier.connection_user(login, password)
            show_access_menu(user)
        case 2:
            answer = request_name_and_password()
            login = answer[0]
            password = answer[1]
            metier.create_new_user(login, password)
        case _:
            print(
                "Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 2."
            )
            show_main_menu()


def number_by_user() -> int:
    """Demande un nombre à l'utilisateur et return le nombre"""
    # type and assign.
    prompt: str = ""
    # check if the enter number is a number or not.
    while not prompt.isdigit():
        prompt = input("choix:")
    # return the select number by user.
    return int(prompt)


def request_name_and_password() -> tuple:
    """Demande à l'user un nom et un mot de passe et return un tuple (login,password)"""
    # initiate show
    print("formulaire demande pseudo et mot de passe".center(100, "-"))
    # type and assign
    login: str = input("pseudo:")
    password: str = input("mot de passe:")
    return login, password


def show_access_menu(user: data.User)->None:
    """ Affiche le menu pour choisir entre modifier les données user ou coffre"""
    # initiate the show of main menu.
    print(
        "Menu Access".center(100, "_"),
        "\n" "\n1. Accéder au données utilisateur" "\n2. Accéder au coffre" "\n" "\n0. Revenir au menu principal",
    )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            show_main_menu()
        case 1:
            pass
            #todo menu utilisateur
        case 2:
            pass
            # todo menu coffre
        case _:
            print(
                "Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 2."
            )
            show_access_menu()
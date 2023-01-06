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
        "\n" "\n1. connexion" "\n2. nouvelle utilisateur" "\n" "\n0. quitter",
    )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            print("Au revoir")
            exit()
        case 1:
            answer = request_login_and_password()
            login = answer[0]
            password = answer[1]
            user = metier.connection_user(login, password)
            show_access_menu(user)
        case 2:
            answer = request_login_and_password()
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


def request_login_and_password() -> tuple:
    """Demande à l'user un nom et un mot de passe et return un tuple (login,password)"""
    # initiate show
    print("formulaire demande pseudo et mot de passe".center(100, "-"))
    # type and assign
    login: str = input("pseudo:")
    password: str = input("mot de passe:")
    return login, password


def show_user_menu(user: data.User) -> None:
    """Affiche le menu utilisateur"""
    # type and assign
    item_index: int
    # initiate the show of main menu.
    print(
        "Menu utilisateur".center(100, "_"),
        "\n"
        "\n1. Modification des données"
        "\n2. Supprimer mon compte"
        "\n"
        "\n0. Revenir au menu precedent",
    )
    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            show_access_menu(user)
        case 1:
            metier.change_data_user(user)
        case 2:
            metier.remove_user(user)
            show_main_menu()
        case _:
            print(
                "Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 2."
            )
            show_user_menu(user)


def show_vault_menu(user: data.User) -> None:
    """Affiche le menu du coffre"""
    # initiate the show of main menu.
    print(
        "Menu Coffre".center(100, "_"),
        "\n"
        "\n1. ajouter"
        "\n2. modifier"
        "\n3. supprimer"
        "\n4. chercher"
        "\n"
        "\n0. Revenir au menu précédent",
    )
    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            show_access_menu(user)
        case 1:
            metier.add_item_in_vault(user)
        case 2:
            pass
            # todo modifie un élément dans le coffre
        case 3:
            pass
            # todo supprime un élément dans le coffre
        case 4:
            pass
            # todo cherche un élément dans le coffre
        case _:
            print(
                "Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 4."
            )
            show_vault_menu(user)


def show_access_menu(user: data.User) -> None:
    """Affiche le menu pour choisir entre modifier les données user ou coffre"""
    # initiate the show of main menu.
    print(
        "Menu Access".center(100, "_"),
        "\n"
        "\n1. Accéder au données utilisateur"
        "\n2. Accéder au coffre"
        "\n"
        "\n0. Revenir au menu principal",
    )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            show_main_menu()
        case 1:
            show_user_menu(user)
        case 2:
            show_vault_menu(user)
        case _:
            print(
                "Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 2."
            )
            show_access_menu(user)


def request_name_login_and_password() -> tuple:
    """Demande à l'utilisateur un nom, un pseudo et un mot de passe et le return sous un tuple (name,login,password)"""
    # initiate show
    print("formulaire demande nom,pseudo et mot de passe".center(100, "-"))
    # type and assign
    name: str = input("nom:")
    login: str = input("pseudo:")
    password: str = input("mot de passe:")
    return name, login, password

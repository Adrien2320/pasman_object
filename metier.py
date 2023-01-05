import data
import interface
import storage


def check_user_exist(user: data.User) -> bool:
    """Vérifie si l'utilisateur n'existe pas"""
    # type and assign
    list_user: list = storage.recover_file_data()
    i: int = 0
    # vérifie si le login de l'utilisateur existe déjà
    for i in range(len(list_user)):
        login: data.User = list_user[i]
        if login.login == user.login:
            return True
            exit()
        else:
            return False


def create_new_user(login: str, password: str) -> None:
    """Créer un nouvel utilisateur"""
    # assign and type
    list_user: list = storage.recover_file_data()
    user: data.User = data.User(login, password)
    # vérifie si cet utilisateur n'existe déjà pas
    if check_user_exist(user):
        print(
            "Malheureusement un utilisateur porte déjà ce pseudo, Veuillez réessayer avec un autre pseudo! ".center(
                100, "-"
            )
        )
        interface.show_main_menu()
    else:
        list_user.append(user)
        storage.record_file_data(list_user)
        interface.show_access_menu(user)


def connection_user(login: str, password: str) -> data.User:
    """Function qui permet de connecter l'user à son compte"""
    # type and assign
    list_user = storage.recover_file_data()
    i: int = 0
    user_test: data.User
    # check si les données entrées sont présentes dans le fichier "register.txt" ou non
    for i in range(len(list_user)):
        user_test = list_user[i]
        if user_test.login == login and user_test.password == password:
            return data.User(login, password)
            exit()

    print("Les données que vous avez entré sont incorrect, veuillez réessayer!")
    interface.show_main_menu()


def search_index_user(user: data.User) -> int:
    """cherche l'index de l'user dans liste du fichier ("register.txt")"""
    # type and assign
    list_user: list = storage.recover_file_data()
    i: int = 0
    test_user: data.User
    #
    for i in range(len(list_user)):
        test_user = list_user[i]
        if test_user.login == user.login:
            return i
            exit()


def change_data_user(user: data.User) -> None:
    """Modifie les données de l'utilisateur"""
    # type and assign
    item_index: int = search_index_user(user)
    old_list: list = storage.recover_file_data()
    new_list: list = old_list
    data_user: data.User = old_list[item_index]
    login: str
    password: str
    # supprimer l'ancien utilisateur de ma liste
    del new_list[item_index]
    # initiate show
    print(
        "modification données utilisateur".center(100, "-"),
        "\n !!! attention si vous ne voulez pas modifier cette donnée, laisser là vide et appuyer sur ENTER !!!",
    )
    # assign login and password
    login = input("pseudo:") or data_user.login
    password = input("mot de passe:") or data_user.password
    # création du nouvel utilisateur
    data_user.change_data_user(login, password)
    # ajout du nouvel utilisateur dans la liste
    new_list.append(data_user)
    # confirmation pour la modification
    if input("Confirmation pour la modification, oui ou non:") == "oui":
        storage.record_file_data(new_list)
        print("Les données ont bien été modifié!")
        interface.show_user_menu(user)
    else:
        print("Les données non pas été modifié!")
        interface.show_user_menu(user)


def remove_user(user: data.User) -> None:
    """Supprime l'utilisateur du fichier ("register.txt")"""

    # type and assign
    number: int = search_index_user(user)
    old_user_list: list = storage.recover_file_data()
    new_user_list: list = old_user_list
    # supprime l'utilisateur de la liste
    del new_user_list[number]
    # confirmation pour la modification
    if input("Confirmation pour la modification, oui ou non:") == "oui":
        storage.record_file_data(new_user_list)
        print("Les données ont bien été modifié!")
    else:
        print("Les données non pas été modifié!")

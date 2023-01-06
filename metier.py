import data
import interface
import storage

def check_if_element_exist(name : str, item_index : int )->bool:
    """Vérifie si l'élément exist déjà dans le vault"""
    # type and assign
    data_vault : data.VaultItem
    user_list : list = storage.recover_file_data()
    data_user : data.User = user_list[item_index]
    # boucle vérifie chaque donnée(name) dans la liste vault
    for i in range(len(data_user.vault)):
        data_vault = data_user.vault[i]
        if data_vault.name == name:
            return True
            exit()
        else:
            return False

def check_user_exist(user: data.User) -> bool:
    """Vérifie si l'utilisateur n'existe pas"""
    # type and assign
    list_user: list = storage.recover_file_data()
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


def add_item_in_vault(user: data.User) -> None:
    """Ajout un élément dans le coffre"""
    # type and assign
    old_list: list = storage.recover_file_data()
    new_list: list = old_list
    answer: tuple = interface.request_name_login_and_password()
    name: str = answer[0]
    login: str = answer[1]
    password: str = answer[2]
    data_user: data.User
    number: int = search_index_user(user)
    # récupère les données de l'utilisateur
    data_user = new_list[number]
    # supprimer les données de l'utilisateur
    del new_list[number]
    # vérifie si les données n'existe pas
    if check_if_element_exist(name,number ):
        print("L'élément exist déjà dans votre coffre")
        interface.show_vault_menu(user)
    # ajouté les données dans le coffre de l'utilisateur
    data_user.add_data_vault(name, login, password)
    # ajout donné de l'utilisateur dans la liste
    new_list.append(data_user)
    # confirmation pour la modification
    if input("Confirmation pour l'enregistrement, oui ou non:") == "oui":
        storage.record_file_data(new_list)
        print("Les données ont bien été enregistré!")
        interface.show_vault_menu(user)
    else:
        print("Les données non pas été enregistré!")
        interface.show_vault_menu(user)
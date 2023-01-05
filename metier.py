import data
import interface
import storage


def check_user_exist(user : data.User)->bool:
    """ Vérifie si l'utilisateur n'existe pas """
    # type and assign
    list_user : list = storage.recover_file_data()
    i : int = 0
    # vérifie si le login de l'utilisateur existe déjà
    for i in range(len(list_user)):
        login : data.User = list_user[i]
        if login.login == user.login:
            return True
            exit()
        else:
            return False

def create_new_user(login: str, password: str) -> None:
    """Créer un nouvel utilisateur"""
    # assign and type
    list_user: list = storage.recover_file_data()
    user : data.User = data.User(login,password)
    # vérifie si cet utilisateur n'existe déjà pas
    if check_user_exist(user) :
        print("Malheureusement un utilisateur porte déjà ce pseudo, Veuillez réessayer avec un autre pseudo! ".center(100,"-"))
        interface.show_main_menu()
    else:
        list_user.append(user)
        storage.record_file_data(list_user)
        # todo interface choix entre menu user ou menu coffre

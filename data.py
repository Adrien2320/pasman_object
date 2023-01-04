class VaultItem:
    """Class data Vault"""

    def __init__(self, name: str, login: str, password: str) -> None:
        """
        Constructor of VaultItem
        :param name:
        :param login:
        :param password:
        """
        self.name = name
        self.login = login
        self.password = password

    def __str__(self) -> str:
        """
        name the object
        :return: string
        """
        return self.name


class User:
    """class data user"""

    def __init__(self, login: str, password: str) -> None:
        """
        Constructor of User
        :param login:
        :param password:
        """
        self.login = login
        self.password = password
        self.vault = []

    def __str__(self) -> str:
        """
        name the object
        :return: string
        """
        return self.login

    def change_data_user(self, new_login: str, new_password: str) -> None:
        """
        Modifie les données de User
        :return: bool
        """
        self.login = new_login
        self.password = new_password

    def add_data_vault(self, name: str, login: str, password: str) -> None:
        """
        Methode qui ajoute des données dans vault via la class VaultItem
        :param name:
        :param login:
        :param password:
        """
        self.vault.append(VaultItem(name, login, password))

    def remove_data_vault(self, item_index: int) -> None:
        """
        Methode qui permet de supprimer un élément de Vault via le numéro d'index
        :param item_index:
        """
        del self.vault[item_index]

    def change_data_vault(
        self, item_index: int, name: str, login: str, password: str
    ) -> None:
        """
        Supprime un élément de la liste via le numéro d'index et créer un nouvel élément
        :param item_index:
        :param name:
        :param login:
        :param password:
        """
        User.remove_data_vault(self, item_index)
        User.add_data_vault(self, name, login, password)

    def search_data_vault(self, item_index: int) -> VaultItem:
        """
        Méthode qui permet de récupérer un object (VaultItem) dans Vault via l'index
        :param item_index:
        :return: object : VaultItem
        """
        return self.vault[item_index]

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

    def change_data_vaultitem(self, name: str, login: str, password: str) -> None:
        """
        Modifier les données de VaultItem
        :param name:
        :param login:
        :param password:
        """
        self.name = name
        self.login = login
        self.password = password


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

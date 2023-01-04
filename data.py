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
        self.vault = VaultItem

    def __str__(self) -> str:
        """
        name the object
        :return: string
        """
        return self.login

from models.file_system import FileSystem


class Credentials(FileSystem):
    """Credentials class.

    Attributes:
        username (str): User name
        password (str): Password
        domain (str): Domain name
    """

    def __init__(self, username, password, domain):
        assert isinstance(username, str)
        assert isinstance(password, str)
        assert isinstance(domain, str)

        if username is None or password is None:
            raise Exception('Username or Password should not be None')
        self.username = username
        self.password = password
        self.domain = domain

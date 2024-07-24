class UserDetails:

    """
    This class manages generating new user details and returning a dictionary of these details.
    """
    def __init__(self, user_id, username, firstname, lastname, user_status):
        self._user_id = user_id
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._user_status = user_status

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        self._firstname = value

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value


    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value


    def to_dict(self):
        """
        This function returns a dictionary of user details.
        """
        return {

                    "id": self._user_id,
                    "username": self._username,
                    "firstName": self._firstname,
                    "lastName": self._lastname,
                    "userStatus": self._user_status

                }

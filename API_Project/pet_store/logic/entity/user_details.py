class UserDetails:
    def __init__(self, user_id, username, firstname, lastname, userStatus):
        self._user_id = user_id
        self._username = username
        self._firstname = firstname
        self._lastname = lastname
        self._userStatus = userStatus

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
        return self.firstname

    @firstname.setter
    def firstname(self, value):
        self.firstname = value

    @property
    def lastname(self):
        return self.lastname

    @lastname.setter
    def lastname(self, value):
        self.lastname = value


    @property
    def userstatus(self):
        return self.userstatus

    @userstatus.setter
    def userstatus(self, value):
        self._userStatus = value


    def to_dict(self):
        return {

                    "id": self._user_id,
                    "username": self._username,
                    "firstName": self._firstname,
                    "lastName": self._lastname,
                    "userStatus": self._userStatus

                }

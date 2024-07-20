class UserDetails:
    def __init__(self, user_id, username, firstname, lastname):
        self._user_id = user_id
        self._username = username
        self._firstname = firstname
        self._lastname = lastname

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

    def to_dict(self):
        return [
                  {
                    "id": 0,
                    "username": "string",
                    "firstName": "string",
                    "lastName": "string",
                    "email": "string",
                    "password": "string",
                    "phone": "string",
                    "userStatus": 0
                  },
                  {
                    "id": self._user_id,
                    "username": self._username,
                    "firstName": self._firstname,
                    "lastName": self._lastname

                  }
                ]
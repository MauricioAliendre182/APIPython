from dataclasses import dataclass


@dataclass(init=False)
class User:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    def __init__(self,
                 id_user=0,
                 username="Carlos123",
                 firstName="Carlos",
                 lastName="Garcia",
                 email="carlos@gmail.com",
                 password="123456789",
                 phone="+5917323545",
                 userStatus=0
                 ):
        self.id = id_user
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus
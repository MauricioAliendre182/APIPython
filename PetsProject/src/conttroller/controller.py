from requests import Response


class Controller:
    _response = None
    _id = None
    _username = None
    _userId = None
    _userIds = []

    # _self = None
    #
    # def __new__(cls):
    #     if cls._self is None:
    #         cls._self = super().__new__(cls)
    #     return cls._self
    #
    # def __init__(self):
    #     self.globalResponse = None
    #     self.id = None

    @staticmethod
    def setResponse(response):
        Controller._response = response

    @staticmethod
    def getResponse() -> Response:
        return Controller._response

    @staticmethod
    def setId(id_pet):
        Controller._id = id_pet

    @staticmethod
    def getId():
        return Controller._id

    @staticmethod
    def setUserName(username):
        Controller._username = username

    @staticmethod
    def getUserName():
        return Controller._username

    @staticmethod
    def setUserId(userId):
        Controller._userId = userId
    @staticmethod
    def getUserId():
        return Controller._userId

    @staticmethod
    def setArrayUsernames(arrayUsernames):
        Controller._userIds = arrayUsernames

    @staticmethod
    def getArrayUsernames():
        return Controller._userIds


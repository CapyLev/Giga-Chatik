from src.modules.core.IException import IException


class ServerNotFound(IException):
    def __init__(self) -> None:
        super().__init__("Could not find server. Check your server id.")


class ServerPasswordRequired(IException):
    def __init__(
        self,
    ) -> None:
        super().__init__("Password is required for this server.")


class ServerPasswordInvalid(IException):
    def __init__(self) -> None:
        super().__init__("Wrong server password provided.")


class UserAlreadyExistsOnThisServer(IException):
    def __init__(self) -> None:
        super().__init__("You are already a member of this server.")


class UserIsNotAdminException(IException):
    def __init__(self) -> None:
        super().__init__("You are not allowed to edit this server")

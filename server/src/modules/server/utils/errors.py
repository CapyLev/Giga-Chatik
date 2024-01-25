class ServerNotFoundException(Exception):
    def __init__(self) -> None:
        super().__init__("Could not find server. Check your server id.")


class ServerPasswordRequiredException(Exception):
    def __init__(
        self,
    ) -> None:
        super().__init__("Password is required for this server.")


class ServerPasswordInvalidException(Exception):
    def __init__(self) -> None:
        super().__init__("Wrong server password provided.")


class UserAlreadyExistsOnThisServerException(Exception):
    def __init__(self) -> None:
        super().__init__("You are already a member of this server.")


class UserIsNotAdminExceptionException(Exception):
    def __init__(self) -> None:
        super().__init__("You are not allowed to edit this server")


class PasswordIsRequiredException(Exception):
    def __init__(self) -> None:
        super().__init__("For private server please provide password.")

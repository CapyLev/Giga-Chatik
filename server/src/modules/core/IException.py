class IException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

    def __str__(self) -> str:
        return self.args[0]

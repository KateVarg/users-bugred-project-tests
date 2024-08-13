import dataclasses


@dataclasses.dataclass
class UserForRegistration:
    name: str
    email: str
    password: str


@dataclasses.dataclass
class UserForLogin:
    email: str
    password: str

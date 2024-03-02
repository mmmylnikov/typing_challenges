from constants import ___
from typing import Callable


class User():
    user_id: int
    pass


def create_user(
        user_name: str, user_age: int,
        after_created: Callable[[int], None]
        ) -> User | None:  # не уверен на счет User (обявил его сам), как альтернатива использовал бы "bool | None"
    pass


def send_test_email(user_id: int) -> None:
    pass


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None

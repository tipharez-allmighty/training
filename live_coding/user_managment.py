from dataclasses import dataclass

@dataclass
class User():
    name: str
    password: str

users: list[User] = []

def get_user(user: User) -> User | None:
    for existing_user in users:
        if existing_user.name == user.name:
            return existing_user
    return None

def get_or_create_user(user: User) -> User:
    if not get_user(user):
        users.append(user)
    return user

def delete_user(user: User) -> None:
    users.remove(user)


test_user_1 = User(name="Alice", password='1111')
test_user_2 = User(name="John", password='2222')

def test_get_user():
    assert get_user(test_user_1) is None
    get_or_create_user(test_user_1)
    assert get_user(test_user_1) == test_user_1
    delete_user(test_user_1)

def test_get_or_create_user():
    initial_amount = len(users)
    assert get_or_create_user(test_user_1) == test_user_1
    assert len(users) == initial_amount + 1
    delete_user(test_user_1)
    assert len(users) == initial_amount

def test_delete_user():
    initial_amount = len(users)
    get_or_create_user(test_user_1)
    assert len(users) == initial_amount + 1
    assert delete_user(test_user_1) is None
    assert len(users) == initial_amount
    try:
        delete_user(test_user_2)
    except ValueError:
        pass
    else:
        raise AssertionError

if __name__ == "__main__":
    test_get_user()
    test_get_or_create_user()
    test_delete_user()

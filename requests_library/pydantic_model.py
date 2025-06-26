from pydantic import BaseModel


class UserModel(BaseModel):
    uuid: str
    email: str
    name: str
    age: int
    is_student: bool


response = {
    'uuid': '12he-13sr-fsrw-3123',
    'email': 'example@gmail.com',
    'name': 'Alex',
    'age': 28,
    'is_student': False,
}

user = UserModel(**response)
print(
    f'Pydantic model:\n{user}\n\n'
    f'Some model data:\n{user.email}\n\n'
    f'JSON from Pydantic model:\n{user.model_dump_json()}'
)

import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru-Ru')
Faker.seed()


def generator_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(5000, 20000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )

def generator_file():
    path = rf'C:\Users\Тол\PycharmProjects\test_site\test_file_{random.randint(0, 100)}.txt'
    file = open(path, 'w+')
    file.write(f'hello word {random.randint(0, 100)}')
    file.close()
    return file.name, path

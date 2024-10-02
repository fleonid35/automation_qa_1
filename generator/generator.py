import email

from data.data import Person
from faker import Faker
ru_faker = Faker("ru_RU")
def generated_person():
    yield Person(
        full_name=ru_faker.first_name() + " " + ru_faker.last_name() + " "+ ru_faker.middle_name(),
        email=ru_faker.email(),
        current_address=ru_faker.address(),
        permanent_address=ru_faker.address()

    )

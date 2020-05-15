from faker import Faker
import numpy.random as npr

from data_structures import SIZES

fake = Faker('ru_RU')
Faker.seed(0)
npr.seed(0)


def generate():
    for size in SIZES:
        with open(f'databases/unsorted/unsorted{size}.txt', 'w') as file:
            for _ in range(size):
                file.write('{} {} {} {} {} {} {} {} {} {}\n'.format(
                    fake.last_name_male(),
                    fake.first_name_male(),
                    fake.middle_name_male(),
                    str(fake.date_of_birth(minimum_age=25, maximum_age=35)),
                    fake.last_name_female(),
                    fake.first_name_female(),
                    fake.middle_name_female(),
                    str(fake.date_of_birth(minimum_age=25, maximum_age=35)),
                    str(fake.date_this_decade()),
                    str(npr.randint(1, 1000))
                ))
            print(f'Размер = {size}: генерация завершена')

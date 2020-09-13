import pandas as pd
import faker
import random


def sex_det_fn():
    rand_it = random.randint(1, 100)/100

    if rand_it > 0.45:
        sex_det = 'M'
    elif rand_it < 0.9:
        sex_det = 'F'
    else:
        sex_det = 'NB'

    return sex_det


def result_det_fn():
    rand_it = random.randint(1, 100)/100

    if rand_it > 0.88:
        res_det = 'P'
    elif rand_it > 0.98:
        res_det = 'E'
    else:
        res_det = 'N'

    return res_det


profiles = {}

n_profiles = 10000

fake = faker.Faker('es_ES')

for i in range(0, n_profiles):

    profiles[i] = {
        'name': fake.name(),
        'dob': fake.date_of_birth(),
        'sample_date': fake.date_this_month(),  # Date of Sample Collection
        'sample_time': fake.time(),  # Hour of Sample Collection
        'result_date': fake.date_this_month(),  # Date of Result
        'sex': sex_det_fn(),
        'sample_result': result_det_fn()
    }


profiles = pd.DataFrame.from_dict(profiles, orient='index').sample(frac=1)

profiles.to_csv('health_data/covid_19_results.csv')

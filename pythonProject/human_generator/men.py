import random
import datetime


human_id = random.randint(1, 900000)


def get_datetime():
    return datetime.datetime.now()


def get_hair_men():
    file_data = open("data/mens_hair.txt")
    get_data = file_data.readlines()
    hair = []
    for i in get_data:
        hair.append(i.strip())

    file_data.close()
    return random.choice(hair)


def get_moustache():
    file_data = open("data/moustache.txt")
    get_data = file_data.readlines()
    moustache = []
    for i in get_data:
        moustache.append(i.strip())

    return random.choice(moustache)


def get_body_type():
    file_data = open("data/body_type.txt")
    get_data = file_data.readlines()
    body_type = []
    for i in get_data:
        body_type.append(i.strip())

    return random.choice(body_type)


def get_country():
    file_data = open("data/country.txt")
    get_data = file_data.readlines()
    country = []
    for i in get_data:
        country.append(i.strip())

    return format(random.choice(country))

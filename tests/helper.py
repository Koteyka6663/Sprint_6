
import random


def generate_phone():
    simbols = "0123456789"
    phone = ''.join(random.sample(simbols, random.randint(9, 9)))
    return "+79" + phone


def random_name():
    names = ["Котя", "Саня", "Иван", "Маша"]
    name = random.choice(names)
    return name


def random_surname():
    surnames = ["Котечкин", "Травкин", "Отравкин", "Мешко"]
    surname = random.choice(surnames)
    return surname


def random_address():
    addreses = [
        "Сосновая дом 5",
        "Травкина 19",
        "Открытое шоссе 9"]
    addres = random.choice(addreses)
    return addres

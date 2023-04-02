import os, django
from faker import Faker
from validate_docbr import CPF
import random
from escola.models import Aluno

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'escola_api.settings')
django.setup()


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))
        data_nascimento = "{}-{}-{}".format(random.randrange(1995, 2015), random.randrange(1, 12), random.randrange(1, 30))
        p = Aluno(nome=nome, cpf=cpf, rg=rg, data_nascimento=data_nascimento)
        p.save()


criando_pessoas(50)
print('Sucesso!')

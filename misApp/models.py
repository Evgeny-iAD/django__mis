from django.db import models

#БД пациентов
class Pacient(models.Model):
    code = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birth_date = models.DateField()
    sex = models.CharField(max_length=10)
    snils = models.CharField(max_length=100)
    polis = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    attachment = models.CharField(max_length=100)
    fluorography = models.CharField(max_length=100)
    d_accounting = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return f'Pacient: {self.last_name} {self.first_name} {self.patronymic}, СНИЛС: {self.snils}'





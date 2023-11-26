from django.core.management.base import BaseCommand
from misApp.models import Pacient

class Command(BaseCommand):
    help = "Добавить пользователя"
    def handle(self, *args, **kwargs):
        # pacient = Pacient(
        #     code='5038231',
        #     last_name = 'Поповский',
        #     first_name = 'Евгений',
        #     patronymic = 'Леонидович',
        #     birth_date = '1987-05-19',
        #     sex = 'М',
        #     snils = '164-037-096 51',
        #     polis = '2354210830001494',
        #     address = '354200 , Краснодарский край, Сочи г, Сочинское шоссе ул, Д. 2, к. 10',
        #     document = 'ПАСПОРТ РФ 03 06 458917 Кем выдан: ОУФМС Кон подразделения: 000-000',
        #     telephone = '+7(988) 168-56-55',
        #     attachment = 'в базе ТФОМС данные отсутствуют',
        #     fluorography = '04.09.2023',
        #     d_accounting = 'Болезни, характеризующиеся повышенным кровяным давлением',
        #     notes = 'Необходимо взять согласие на обработку перс. данных'
        # )
        # pacient = Pacient(
        #     code='3031121',
        #     last_name = 'Поликарпов',
        #     first_name = 'Сергей',
        #     patronymic = 'Кужугетович',
        #     birth_date = '1981-11-11',
        #     sex = 'М',
        #     snils = '135-027-044 21',
        #     polis = '2354350830001333',
        #     address = '354200 , Краснодарский край, Сочи г, Партизанская, д.5',
        #     document = 'ПАСПОРТ РФ 11 07 555917 Кем выдан: ОУФМС Код подразделения: 234-120',
        #     telephone = '+7(988) 56-76-88',
        #     attachment = 'Прикреплен к участку 001 (Согласно данных ТФОМС)',
        #     fluorography = 'не делалась',
        #     d_accounting = '',
        #     notes = 'Необходимо взять согласие на обработку перс. данных'
        # )
        pacient = Pacient(
            code='1052222',
            last_name = 'Вязовская',
            first_name = 'Екатерина',
            patronymic = 'Сергеевна',
            birth_date = '1975-12-05',
            sex = 'Ж',
            snils = '144-033-011 10',
            polis = '2354334530001555',
            address = '354200 , Краснодарский край, Сочи г, Ленина, д.33 кв. 6',
            document = '',
            telephone = '+7(988) 36-22-11',
            attachment = 'Прикреплен к участку 012 (Согласно данных ТФОМС)',
            fluorography = '11.08.2023',
            d_accounting = '',
            notes = 'Необходимо взять согласие на обработку перс. данных'
        )
        pacient.save()
        self.stdout.write(f'{pacient}')

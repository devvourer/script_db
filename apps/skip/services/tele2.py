from django.conf import settings

from ..models import Tele2File, Tele2

import csv


class Service:

    def get_data_from_csv(self):
        file: Tele2File = Tele2File.objects.first()

        with open(f'{file.file.path}', 'r') as f:
            csv_reader = csv.reader(f)

            for i in csv_reader:
                data = i[0].split(';')
                fio = data[1].split(' ')
                fio_len = len(fio)

                if fio_len > 1:
                    if fio_len != 3:
                        fio.append('')
                    yield [data[0], fio]

    def get_objects(self):
        data = []
        count = 0
        for i in self.get_data_from_csv():
            if count > 1000:
                Tele2.objects.bulk_create(data)
                data = []
                count = 0

            data.append(Tele2(phone=i[0], name=i[1][1], surname=i[1][0], patronymic=i[1][2], act_date='2022-08-08'))

            count += 1

        Tele2.objects.bulk_create(data)

    def test(self):
        with open(f'{settings.BASE_DIR}/pochta_orders1', 'r', encoding='utf-8') as f:
            lines = f.readlines(30000)
            with open(f"{settings.BASE_DIR}/new_data.txt", 'w', encoding='UTF-8') as new:
                for line in lines:

                    new.write(line + '\n')

            for line in lines:
                print(line)



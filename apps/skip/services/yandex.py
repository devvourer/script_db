from ..models import YandexFile, Yandex, YandexBad

from typing import Union, Tuple
from transliterate import translit

import csv
import re


class Service:

    @staticmethod
    def get_full_name(data: list) -> Tuple[list, bool]:
        """Булево значение обозначает валидность данных"""
        if re.match(r'^[А-Яа-яЁё ]+$', data[0]) and re.match(r'^[А-Яа-яЁё ]+$', data[1]):

            data = [translit(s.lower().capitalize(), 'ru') for s in data]

            return data, True
        return data, False

    def get_data_from_csv(self, file: YandexFile):
        with open(f'{file.file.path}', 'r', encoding='CP1251') as f:
            csv_reader = csv.reader(f)

            count = 0
            for i in csv_reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    # if count < 1000:
                    try:
                        obj = []
                        data = i[0].split(';')

                        obj.append(data[0])  # y_id
                        obj.append(data[1])  # first_name
                        obj.append(data[2])  # email
                        obj.append(data[3])  # phone_number
                        obj.append(data[4])  # address_city
                        obj.append(data[5])  # address_street
                        obj.append(data[6])  # address_house

                        obj.append('2022-10-21')  # act_date

                        fio, valid = self.get_full_name(data[11:14])

                        obj.append(fio)
                        obj.append(valid)  # Валидность данных

                        count += 1

                        yield obj
                    except IndexError:
                        continue

                    # else:
                    #     break

    def get_content(self, file: YandexFile):
        objs = []
        bad_objs = []

        objs_count = 0
        bad_objs_count = 0
        for i in self.get_data_from_csv(file):
            if i[-1]:

                if objs_count > 1000:
                    Yandex.objects.bulk_create(objs)
                    objs = []

                objs.append(Yandex(
                    y_id=i[0],
                    first_name=i[8][2],
                    email=i[2],
                    phone_number=i[3],
                    address_city=i[4],
                    address_street=i[5],
                    address_house=i[6],
                    surname=i[8][1],
                    patronymic=i[8][0],
                    act_date=i[7]
                ))

                objs_count += 1
            else:
                if bad_objs_count > 1000:
                    YandexBad.objects.bulk_create(bad_objs)
                    bad_objs = []

                bad_objs.append(YandexBad(
                    y_id=i[0],
                    first_name=i[8][0],
                    email=i[2],
                    phone_number=i[3],
                    address_city=i[4],
                    address_street=i[5],
                    address_house=i[6],
                    surname=i[8][1],
                    patronymic=i[8][2],
                    act_date=i[7]
                ))

                bad_objs_count += 1

        Yandex.objects.bulk_create(objs)
        YandexBad.objects.bulk_create(bad_objs)


class ServiceNoAddress:

    @staticmethod
    def get_data_from_csv(self):
        pass


    def get_content(self, file: YandexFile):

        pass
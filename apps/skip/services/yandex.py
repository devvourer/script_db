from django.conf import settings

from ..models import YandexFile, Yandex, YandexBad
from ..utils import format_and_translit_str, translit, get_digits

from typing import Tuple

import csv
import re


class YandexService:

    @staticmethod
    def _get_full_name(data: list, str_name: str) -> Tuple[list, bool]:
        """ Булево значение обозначает валидность данных
            data это ФИО в списке, в data должно быть 3 записи,
            str_name это Имя, бывают случаи когда в str_name попадает Имя Фамилия, а в список нет,
            в таком случае данные валидны но возьмем мы их с str_name
        """

        data = [format_and_translit_str(s).strip(' ') for s in data]
        if re.match(r'^[А-Яа-яЁё ]+$', data[0]) and re.match(r'^[А-Яа-яЁё ]+$', data[1]):

            return data, True
        name = [format_and_translit_str(s) for s in str_name.split(' ')]

        if len(name) > 1 and len(name[0]) > 2 and len(name[1]) > 2\
                and re.match(r'^[А-Яа-яЁё ]+$', name[0]) and re.match(r'^[А-Яа-яЁё ]+$', name[1]):
            if not len(name) == 3:
                name.append('')  # добавили 3 запись
            return name, True

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
                    try:
                        obj = []
                        data = i[0].split(';')

                        obj.append(data[0])  # y_id
                        obj.append(data[1])  # first_name
                        obj.append(data[2])  # email
                        obj.append(data[3])  # phone_number
                        obj.append(translit(data[4], 'ru'))  # address_city
                        obj.append(translit(data[5], 'ru'))  # address_street
                        obj.append(data[6])  # address_house

                        obj.append(file.act_date)  # act_date

                        fio, valid = self._get_full_name(data[11:14], data[1])

                        obj.append(fio)
                        obj.append(valid)  # Валидность данных

                        count += 1

                        yield obj
                    except IndexError:
                        continue

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
                    first_name=i[8][1],
                    email=i[2],
                    phone_number=i[3],
                    address_city=i[4],
                    address_street=i[5],
                    address_house=i[6],
                    surname=i[8][0],
                    patronymic=i[8][2],
                    act_date=i[7]
                ))

                objs_count += 1
            else:
                if bad_objs_count > 1000:
                    YandexBad.objects.bulk_create(bad_objs)
                    bad_objs = []

                bad_objs.append(YandexBad(
                    y_id=i[0],
                    first_name=i[8][1],
                    email=i[2],
                    phone_number=i[3],
                    address_city=i[4],
                    address_street=i[5],
                    address_house=i[6],
                    surname=i[8][0],
                    patronymic=i[8][2],
                    act_date=i[7]
                ))

                bad_objs_count += 1

        Yandex.objects.bulk_create(objs)
        YandexBad.objects.bulk_create(bad_objs)


class YandexServiceNoAddress:
    @staticmethod
    def _get_full_name(string: str) -> Tuple[list, bool]:
        fio = [format_and_translit_str(s) for s in string.split(' ')]

        if len(fio) > 1 and re.match(r'^[А-Яа-яЁё ]+$', fio[0]) and re.match(r'^[А-Яа-яЁё ]+$', fio[1]):
            if not len(fio) == 3:
                fio.append('')
            return fio, True
        if not len(fio) == 3:
            fio.append('')
            fio.append('')
        return fio, False

    def get_data_from_csv(self, file: YandexFile):
        with open(f'{file.file.path}', 'r') as f:
            csv_reader = csv.reader(f)

            count = 0
            for i in csv_reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    fio, valid = self._get_full_name(i[1])
                    obj = []
                    obj.append(i[0])  # y_id
                    obj.append(fio)  # fio
                    obj.append(i[2])  # email
                    obj.append(get_digits(i[3]))  # phone
                    obj.append(valid)  # Валидность данных

                    yield obj

    def get_content(self, file: YandexFile):
        bad_objs = []
        objs = []

        objs_count = 0
        bad_objs_count = 0

        for i in self.get_data_from_csv(file):
            if i[4]:
                if objs_count > 1000:
                    Yandex.objects.bulk_create(objs)
                    objs = []

                objs.append(Yandex(
                    y_id=i[0],
                    first_name=i[1][1],
                    email=i[2],
                    phone_number=i[3],
                    surname=i[1][0],
                    patronymic=i[1][2],
                    act_date=file.act_date
                ))
                objs_count += 1

            else:
                if bad_objs_count > 1000:
                    YandexBad.objects.bulk_create(bad_objs)
                    bad_objs = []

                bad_objs.append(YandexBad(
                    y_id=i[0],
                    first_name=i[1][1],
                    email=i[2],
                    phone_number=i[3],
                    surname=i[1][0],
                    patronymic=i[1][2],
                    act_date=file.act_date
                ))

                bad_objs_count += 1

        Yandex.objects.bulk_create(objs)
        YandexBad.objects.bulk_create(bad_objs)

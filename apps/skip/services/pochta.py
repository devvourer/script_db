from django.conf import settings

from ..utils import get_digits, format_and_translit_str
from ..models import Pochta


class PochtaService:

    @staticmethod
    def get_full_name(name: str):
        data = [format_and_translit_str(s) for s in name.split(' ')]
        if len(data) < 3:
            data.append('')
            data.append('')

        return data

    def get_data_from_file(self):

        with open(f'{settings.BASE_DIR}/new_SASA.xlsx', 'r') as f:
            count = 0
            skip_first_iteration = 0
            for i in f:
                if skip_first_iteration == 0:
                    skip_first_iteration += 1
                    continue

                if count > 400000:
                    break

                data = i.split('\t')
                obj = (
                        self.get_full_name(data[13]),  # FIO
                        data[9].replace('"', ''),  # index_to_ccode
                        get_digits(data[14]),  # phone number
                        data[75].replace('\n', '').split(' ')[0]  # date
                       )

                print(count)
                count += 1
                yield obj


    def get_content(self):
        objs = []
        count = 0
        for i in self.get_data_from_file():
            if count > 5000:
                Pochta.objects.bulk_create(objs)
                objs = []

            objs.append(
                Pochta(
                    name=i[0][0],
                    surname=i[0][1],
                    patronymic=i[0][2],
                    address=i[1],
                    home_phone=i[2],
                    arrival_local_dts=i[3],
                )
            )

            count += 1

        Pochta.objects.bulk_create(objs)

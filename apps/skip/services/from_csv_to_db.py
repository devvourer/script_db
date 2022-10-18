from ..models import CsvData, Contact

import csv


class Service:

    def get_data_from_csv(self):
        file: CsvData = CsvData.objects.first()

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
                Contact.objects.bulk_create(data)
                data = []
                count = 0

            data.append(Contact(phone=i[0], name=i[1][1], surname=i[1][0], patronymic=i[1][2]))

            count += 1

        Contact.objects.bulk_create(data)

import datetime


class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_to_int(cls, date_str):
        date_list = str(date_str).split("-")
        if cls.is_valid_date(date_str):
            for el in date_list:
                item = int(el)
                print("Type: " + str(type(item)) + " Value: " + str(item))

    @staticmethod
    def is_valid_date(date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
            return True
        except ValueError:
            print("Некорректный формат даты: " + date + " , должен быть DD-MM-YYYY")
            return False

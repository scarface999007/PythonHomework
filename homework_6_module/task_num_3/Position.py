from homework_6_module.task_num_3.Worker import Worker


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return " ".join(self.name + self.surname)

    def get_total_income(self):
        income = dict(self._income).values()
        return sum(income)

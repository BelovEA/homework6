class Worker:
    def __init__(self, name, surname, position, prof, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": prof, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


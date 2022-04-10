class Staff:  # Рабочие
    def __init__(self, id, name, surname, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.salary = salary

    def getSalary(self):
        return self.salary

    def showAll(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Salary:", self.salary)
        print()


class HRManagers:  # Отдел кадров
    def __init__(self, id, fullName, salary):
        self.id = id
        self.fullName = fullName
        self.salary = salary

    def getSalary(self):
        return self.salary

    def showAll(self):
        print("ID:", self.id)
        print("Fullname:", self.fullName)
        print("Salary:", self.salary)
        print()


class Programmers:  # Программисты
    def __init__(self, id, nickname, salary, bonusSalary, KPIValue):
        self.id = id
        self.nickname = nickname
        self.salary = salary
        self.bonusSalary = bonusSalary
        self.KPIValue = KPIValue  # коэффициент объема работы его значение от 0 до 1 включительно.

    def setSalary(self):
        self.salary = self.KPIValue * self.bonusSalary

    def getSalary(self):
        return self.salary

    def showAll(self):
        print("ID:", self.id)
        print("Nickname:", self.nickname)
        print("Salary:", self.salary)
        print("BonusSalary:", self.bonusSalary)
        print("KPIValue:", self.KPIValue)
        print()


employees = [
    Programmers(1264978, 'asemalik', 250000, 50000, 0.75),
    Programmers(5164786, 'jaindhh', 220000, 50000, 0.5),
    HRManagers(1458647, "Ilyas Zhuanyshev", 200000),
    HRManagers(1564793, "Erbol Assanbek", 223500),
    Staff(4672593, "Jhon", "Kali", 175000)
]


def max_salary(a):
    print("\nДанные рабочего, у которого самая высокая зарплата:")

    max = 0
    showAll = 0

    for i in a:
        if i.salary > max:
            max = i.salary
            showAll = i

    return showAll.showAll()


def sort_salary(a):
    print("Сортировка сотрудников по убыванию их зарплат:")

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i].salary > a[j].salary:
                a[i], a[j] = a[j], a[i]

    return a

max_salary(employees)

for i in sort_salary(employees):
    i.showAll()

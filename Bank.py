class CityBankAccount:
    def __init__(self, fullName, balance, accountNumber, pinCode):
        self.fullName = fullName
        self.balance = balance
        self.accountNumber = accountNumber
        self.pinCode = pinCode

    def get_fullName(self):
        return self.fullName

    def get_balance(self):
        return self.balance

    def creditBalance(self, credit_Balance):
        self.balance -= credit_Balance

    def debetBalance(self, debet_Balance):
        self.balance += debet_Balance

    def get_accountNumber(self):
        return self.accountNumber

    def set_pinCode(self, new_pinCode):
        new_pinCode2 = input("Введите пин-код еще раз:")
        if new_pinCode == new_pinCode2:
            self.pinCode = new_pinCode
        else:
            print("Ошибка! Повторите запрос позднее...")

    def get_pinCode(self):
        return self.pinCode

    def accountData(self):
        print("Fullname:", self.fullName)
        print("Account number:", self.accountNumber)
        print("Balance:", self.balance)
        print("pinCode:", self.pinCode)


class NationalBankAccount:
    def __init__(self, fullName, balance, accountNumber, pinCode):
        self.fullName = fullName
        self.balance = balance
        self.accountNumber = accountNumber
        self.pinCode = pinCode

    def get_fullName(self):
        return self.fullName

    def get_balance(self):
        return self.balance

    def creditBalance(self, credit_Balance):
        self.balance -= credit_Balance

    def debetBalance(self, debet_Balance):
        self.balance += debet_Balance

    def get_accountNumber(self):
        return self.accountNumber

    def set_pinCode(self, new_pinCode):
        self.pinCode = new_pinCode

    def get_pinCode(self):
        return self.pinCode

    def accountData(self):
        print("\n:")
        print("Fullname:", self.fullName)
        print("Account number:", self.accountNumber)
        print("pinCode:", self.pinCode)
        print("Balance:", self.balance)


class Database:
    allAccounts = [
        CityBankAccount("Ilyas Zhuanyshev", 200000, "KZ010322312", "0102"),
        CityBankAccount("Erbol Assanbek", 100000, "KZ010322313", "0101"),
        NationalBankAccount("Ilyas Zhuanyshev", 512556, "KZ0101112", "0102")
    ]
def CityBankATM(a):
    k = input("Здравствуйте! Введите счет банковской карты:")

    def proverka_accountNumber(a, number, count=1):
        if count < 3:
            count += 1
            for i in range(len(a.allAccounts)):
                if number == a.allAccounts[i].accountNumber:
                    proverka_pinCode(input("Введите пин код:"), a.allAccounts[i])
                    return
                else:
                    continue
            number = input("По данному счету не найдена карта. \nВведите счет банковской карты еще раз!")
            return proverka_accountNumber(a, number, count)
        else:
            print("Количество запросов исчерпано. Повторите запрос позднее!")
            return

    def proverka_pinCode(n, a, count=1):
        if n == a.pinCode:
            return proverka_banka(a)
        else:
            count += 1
            if count <= 3:
                n = input("Ошибка! Повторите запрос:")
                return proverka_pinCode(n, a, count)
            else:
                print("Количество запросов исчерпано. Повторите запрос позднее!")
                return

    def proverka_banka(a):
        print("Выберите операцию:")
        if type(a) == CityBankAccount:
            print("\nPRESS [1] TO CASH WITHDRAWAL",

                  "\nPRESS [2] TO VIEW BALANCE",

                  "\nPRESS [3] TO CHANGE PIN CODE",

                  "\nPRESS [4] TO CASH IN ACCOUNT",

                  "\nPRESS [5] TO VIEW ACCOUNT DATA",

                  "\nPRESS [6] TO EXIT\n"
                  )
            press = int(input())
            if press == 1:
                a.creditBalance(int(input("Введите сумму:")))
            elif press == 2:
                print(a.get_balance())
            elif press == 3:
                a.set_pinCode(input("Введите новый пин код:"))
            elif press == 4:
                a.debetBalance(int(input()))
            elif press == 5:
                a.accountData()
            elif press == 6:
                print("Выход...")
                return
            return proverka_banka(a)
        else:
            print("PRESS [1] TO CASH WITHDRAWAL",

                  "\nPRESS [2] TO VIEW BALANCE",

                  "\nPRESS [0] TO EXIT"
                  )
            press = int(input())
            if press == 1:
                a.creditBalance(int(input("Введите сумму:")) + 200)
            elif press == 2:
                print(a.get_balance())
            elif press == 0:
                print("Выход...")
                return
            return proverka_banka(a)




    proverka_accountNumber(a, k)


CityBankATM(Database)

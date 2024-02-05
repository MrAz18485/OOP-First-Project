import random
import string

account_database_file = open("account_database.txt", "r")
data = account_database_file.readlines()
account_database_file.close()
lowercase_letters = string.ascii_lowercase

def random_name_generator():
    name = ""
    #name
    for i in range(random.randint(3,6)):
        name += lowercase_letters[random.randint(0,25)]
    return name

def random_surname_generator():
    surname = ""
    #surname
    for i in range(random.randint(3,6)):
        surname += lowercase_letters[random.randint(0,25)]
    return surname



class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Bank(Person):
    def __init__(self, name, surname):
        Person.__init__(self, name, surname)
        self.name_and_surname = name + "_" + surname

    def get_user_info(self):
        for line in data:
            if self.name_and_surname in line:
                return line
        print("User does not exist in database!")

    def create_account(self):
        for line in data:
            if self.name_and_surname in line:
                print("User already exists in database!")
                return False
        data.append(self.name_and_surname+":0")
        print("Account created successfully!")

    def check_balance(self):
        for line in data:
            line = line.split(":")
            if line[0] == self.name_and_surname:
                balance = line[1]
                return balance

    def update_balance(self, integer, action):
        for line in data:
            if self.name_and_surname in line:
                idx = data.index(line)
                data.remove(line)
                line = line.split(":")
                value = int(line[1])
                if action == "deposit":
                    value += integer
                elif action == "withdraw":
                    value -= integer
                updated_line = line[0] + ":" + str(value)
                data.insert(idx, updated_line)
                print("Balance updated!")
                return True
        return False

    def deposit_money(self, integer):
        return self.update_balance(integer, "deposit")

    def withdraw_money(self, integer):
        return self.update_balance(integer, "withdraw")

    def close_and_update_file(self):
        file = open("account_database.txt", "w")
        file.truncate(0)
        for line in data:
            if "\n" in line:
                file.write(line)
            else:
                file.write(line+"\n")
        print("Account database file successfully updated and closed!")
        file.close()


bank_account = Bank(random_name_generator(), random_surname_generator())
bank_account.create_account() #creates account
print(bank_account.get_user_info())
print(bank_account.update_balance(50, "deposit"))
print(data)
#print(bank_account.get_user_info())
bank_account.close_and_update_file()



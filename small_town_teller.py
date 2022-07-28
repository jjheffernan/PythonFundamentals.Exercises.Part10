"""
small town teller example for zip code wilmington

"""


class Person:
    id_count = 1

    def __init__(self, name):
        #  id_num: int, first_name: str, last_name: str
        self.name = name
        # person_id = id_num
        Person.id_count += 1
        self.person_id = Person.id_count
        # self.first_name = first_name
        # self.last_name = last_name


class Account:

    def __init__(self):
        # id_num: int, type: str, owner: Person
        # account_num = id_num
        # account_type = type
        # account_owner = owner
        self.account_owner = None
        self.account_num = 0
        self.account_type = None
        self.balance = 0.0

    def create_account(self, account_id: int, type: str, name: Person):
        self.account_num = account_id
        self.account_type = type
        self.account_owner = name
        # pass  # escape pass

    def add_account(self):
        pass

    def get_id(self, id_num):

        return
        pass


class Bank:
    """
    this might end us as an interface
    """
    #
    customers = {}
    accounts = {}
    def __init__(self):
        self.name = name
        self.account_id = account_id

    def add_customer(self, customer_id: Account):
        if Person.id in self.customers:
            print("")
        else:
            self.person[Person.id] = Person
        pass

    def add_account(self, account_id: int):
        if account.owner.id

        pass

    def remove_account(self, account_id: int) -> None:
        return None

    def deposit_funds(self, account_id: int, deposit: float):
        Account = Account.get_id(account_id)
        Account.balance += deposit
        print("Deposit Amount: ", deposit)
        # pass  # escape return

    def withdraw_funds(self, account_id: int, withdraw: float):
        if Account.balance >= withdraw:
            Account.balance -= withdraw
            print(f"You withdrew: ${withdraw} \n")
        else:
            print("insufficient funds. ")
        # pass  # escape return

    def get_balance(self, account_id: int):
        if account_id in self.account:
            balance = self.account.get(account_id).balance
            return balance
        else:
            print('')
        pass  # escape return

"""
small town teller example for zip code wilmington

"""


class Person:

    def __init__(self, name):
        #  id_num: int, first_name: str, last_name: str
        self.name = name
        # person_id = id_num
        # first_name = first_name
        # last_name = last_name


class Account:

    def __init__(self):
        # id_num: int, type: str, owner: Person
        # account_num = id_num
        # account_type = type
        # account_owner = owner
        self.balance = 0.0


class Bank:
    """
    this might end us as an interface
    """
    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id


    def add_customer(self, customer_id: Person):


    def add_account(self, account_id: int):
        pass

    def remove_account(self, account_id: int) -> None:
        return None

    def deposit_funds(self, account_id: int, deposit: float):

        Account.balance += deposit
        # pass  # escape return

    def withdraw_funds(self, account_id: int, withdraw: float):
        if Account.balance >= withdraw:
            Account.balance -= withdraw
            print(f"You withdrew: ${withdraw} \n")
        else:
            print("insufficient funds. ")
        # pass  # escape return

    def get_balance(self, account_id: int):

        pass  # escape return

"""
small town teller example for zip code wilmington

"""


class Person:
    id = 0
    first_name = ''
    last_name = ''


class Account:
    number = 0
    type = ''
    owner = 0
    balance = 0.0


class Bank:
    """
    this might end us as an interface
    """
    def add_customer(self, customer_id: int):
        pass

    def add_account(self, account_id: int):
        pass

    def remove_account(self, account_id: int) -> None:
        return None

    def deposit_funds(self, account_id: int, deposit: float):
        pass

    def withdraw_funds(self, account_id: int, withdraw: float):
        pass

    def get_balance(self, account_id: int):
        pass

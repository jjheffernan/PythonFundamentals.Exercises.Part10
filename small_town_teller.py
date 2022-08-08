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

    def create_person(self, id_num, first_name, last_name):
        self.person_id = id_num
        self.name = first_name + last_name


class Account:
    # dict of account information and Owner ID
    acc_dict = {'number': [], 'type': [], 'owner': [], 'balance': []}

    def __init__(self):
        # id_num: int, type: str, owner: Person
        # account_num = id_num
        # account_type = type
        # account_owner = owner

        # add owner name string to accoutn dictionary
        self.account_owner = None

        # add personal ID string to account dictionary
        self.account_num = 0

        # declare account type
        self.account_type = None

        # declare starting balance, default set to 0
        self.balance = 0.0

    def get_account_owner(self):
        # return Account Owner Name
        return self.account_owner
        # pass

    def get_id(self, id_num):
        # return Account ID number
        return self.account_num
        # pass

    def get_type(self, id_num):
        # return Account type String
        return self.account_type

    def get_balance(self, id_num):
        # return Account Numerical Balance
        return self.balance


class Bank:
    """
    this might end up as an interface
    """
    # dict of customers/ customer ID/ Account IDs
    customers = {'Person': [], 'Banker_ID': [], 'Accounts': []}
    # dict of account information and Owner ID
    accounts = {'number': [], 'type': [], 'owner': [], 'balance': []}

    def __init__(self):
        # self.name = bank_name
        # self.account_id = account_id
        pass

    def add_customer(self, customer_id: Account):
        if Person.id in self.customers:
            print("")
        else:
            self.person[Person.id] = Person
        pass

    def create_account(self, account_id: int, ac_type: str, name: Person):
        Account.account_num = account_id
        Account.account_type = ac_type
        Account.account_owner = name
        # pass  # escape pass

    def add_account(self, account_id: int):
        # if account.owner.id
        owner_id = account_id
        # add call to get owner name
        self.accounts['number'].append(owner_id)
        print(f'added account #{owner_id} to {account_id}')
        # above is incorrect, need to call variable for owner separately
        # pass # escape pass

    def remove_account(self, account_id: int) -> None:
        owner_id = account_id
        self.accounts['number'].remove(owner_id)
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



class BankAccount:
    """
    A class to represent a bank account with an account holder and balance.

    :param account_holder: The name of the account holder.
    :type account_holder: str
    :param balance: The initial balance of the account, defaults to 0.0.
    :type balance: float, optional
    """

    def __init__(self, account_holder, balance=0.0):
        """
        Initialize a BankAccount with an account holder and an optional initial balance.

        :param account_holder: The name of the account holder.
        :type account_holder: str
        :param balance: The initial balance of the account, defaults to 0.0.
        :type balance: float, optional
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: The amount to deposit. Must be positive.
        :type amount: float
        :raises ValueError: If the amount is negative.
        :return: None
        :rtype: None
        """
        if amount < 0:
            print("You cannot deposit a negative amount.")
            return
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: The amount to withdraw. Must be positive and less than or equal to the balance.
        :type amount: float
        :raises ValueError: If the amount is negative or exceeds the balance.
        :return: None
        :rtype: None
        """
        if amount < 0:
            print("You cannot withdraw a negative amount.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount

    def display_balance(self):
        """
        Display the account holder's name and the current balance.

        :return: None
        :rtype: None
        """
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")

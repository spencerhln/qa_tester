import unittest
from sample_account import Customer

## Global variables used to set up basic accounts that can be referenced for testing ##

# Both names and balances can be increased in length to cover more test cases #
names = ["alllower", # List of names with varying composition to verify methods work with different string compositions
         "ALLUPPER",
         "1234567890",
         "!@#$%^&*()_+{}",
         "Combination_str1ng!",
         "String" + "Addition",
         1]
balances = [0, -15.0, 35.2, 91, -3, 4, 5.0] # List of varying balance values used to verify methods work with different number values


## Helper Functions to assist in test case generation ##

def sample_account_generator(with_balances=False):
    '''
    Creates and returns a list of Customers with names from the global variable 'names'
    If with_balances == True, sets balances for the Customers
    '''
    result = [Customer(name) for name in names]
    if with_balances:
        [accout.set_balance(bal) for accout, bal in zip(result, balances)]
    return result


## Unit Tests for each Function ##

class sample_account_init_tests(unittest.TestCase):
    '''
    Executes test cases for the __init__ method in sample_account
    '''
    def test_init_record_access(self):
        '''
        Checks that the __init__ method creates new Customer objects and stores the provided name
        '''
        sample_accounts = sample_account_generator() # Generates sample accounts
        self.assertTrue(all([name_string == account.name for name_string, account in zip(names, sample_accounts)]),
                        "__init__ failed; incorrect name recorded") # Asserts that the names in the generated customers can be accessed and match the names they were generated with
    def test_init_empty(self):
        '''
        Checks that the __init__ method raises an error when no name is provided
        '''
        with self.assertRaises(TypeError):
            Customer()
    def test_init_modify(self):
        '''
        Checks that the __init__ method allows for modification of the name attribute
        '''
        sample_accounts = sample_account_generator() # Generates sample accounts
        new_names = ["Jim", "Bob", "Karen", "Janet", "Michael", "Sarah", "Aubrey"] # New names for Customer modification
        sample_accounts = sample_account_generator() # Generates new sample accounts
        [Customer.__init__(account, new_name) for account, new_name in zip(sample_accounts, new_names)] # Modifies and updates Customer names
        self.assertTrue(all([name_string == account.name for name_string, account in zip(new_names, sample_accounts)]),
                        "__init__ failed; names could not be modified") # Checks to see that the updated names match the names they were generated with
        
class sample_account_set_balance_tests(unittest.TestCase):
    '''
    Executes test cases for the set_balance method in sample_account
    '''
    def test_set_balance_record_access(self):
        '''
        Checks that we can set and access a balance using the set_balance method
        '''
        sample_accounts = sample_account_generator(True) # Generates new accounts to be modified within this test
        self.assertTrue(all([balance == account.balance for balance, account in zip(balances, sample_accounts)]),
                        "set_balance failed; incorrect balance recorded") # Checks to see that the balances are set properly and can be accessed
    def test_set_balance_empty(self):
        '''
        Checks that the set_balance method sets a value of 0.0 when left empty
        '''
        my_account = Customer("Spencer") # Creates new customer
        my_account.set_balance() # Sets balance with no amount set
        self.assertEqual(my_account.balance, 0.0) # Checks that the stored balance is equal to 0.0
    def test_set_balance_modify(self):
        '''
        Checks that the set_balance method will reset the balance, even after balance modification
        '''
        new_balances = [12.0 for x in range(0, len(balances))] # Creates a list of new balances to replace the default balance set
        sample_accounts = sample_account_generator(True) # Generates new accounts to be modified within this test
        self.assertTrue(all([balance == account.balance for balance, account in zip(balances, sample_accounts)]),
                        "set_balance failed; incorrect balance recorded")
        [account.set_balance(bal) for account, bal in zip(sample_accounts, new_balances)]
        self.assertTrue(all([balance == account.balance for balance, account in zip(new_balances, sample_accounts)]),
                        "set_balance failed; incorrect balance set")
        
class sample_account_withdraw_tests(unittest.TestCase):
    '''
    Executes test cases for the withdraw method in sample_account
    '''
    def test_withdraw_function(self):
        '''
        Checks that withdraw, when given a proper amount value, functions correctly
        Checks both the modified balance within class and the returned value by withdraw
        '''
        balance_amounts = [1.0, 5.0, 10.0, 1000.0] # Realistic balance amounts that are set here so they can be easily modified in-line 
        withdrawl_amounts = [1, 2, 5, -4] # Withdraw amounts based off the balance amounts set here so they can be modified in-line
        sample_accounts = sample_account_generator() # Generates new accounts to be modified within this test
        [account.set_balance(bal) for account, bal in zip(sample_accounts, balance_amounts)] # Sets account balances to the amounts above
        new_balances = [account.withdraw(amount) for account, amount in zip(sample_accounts, withdrawl_amounts)] # Withdraws amounts from above
        self.assertTrue(all([balance == (balance_amounts[x] - withdrawl_amounts[x]) for balance, x in zip(new_balances, range(0, len(withdrawl_amounts)))])) # Checks that the stored balances are the same as the difference between the balance and the withdrawl
        self.assertTrue(all([account.balance == (balance_amounts[x] - withdrawl_amounts[x]) for account, x in zip(sample_accounts, range(0, len(withdrawl_amounts)))])) # Checks that the returned values are the same as the difference between the balance and the withdrawl
    def test_withdraw_insufficient_funds(self):
        '''
        Checks that the withdraw method will raise an exception when given a value less than the current balance
        '''
        balance_amounts = [1.0, 5.0, 10.0, 1000.0] # Realistic balance amounts that are set here so they can be easily modified in-line
        withdrawl_amounts = [1001, 1002, 5647, 9456] # Withdraw amounts based off the balance amounts set here so they can be modified in-line
        sample_accounts = sample_account_generator() # Generates new accounts to be modified within this test
        for balance in balance_amounts:
            with self.subTest(balance=balance):
                this_account = Customer('sample')
                this_account.set_balance(balance)
                for amount in withdrawl_amounts:
                    with self.subTest(amount=amount):
                        with self.assertRaises(RuntimeError):
                            this_account.withdraw(amount)
    def test_withdraw_empty(self):
        '''
        Checks that withdraw raises an error when no amount is provided
        '''
        with self.assertRaises(TypeError):
            my_account = Customer("Spencer")
            my_account.set_balance()
            my_account.withdraw()
    def test_withdraw_unexpected_input(self):
        '''
        Checks that the withdraw function behaves properly when given an improper input (non int/float)
        '''
        improper_amount_types = ['a', ('tuple'), ['list']] # List of improper amount types
        sample_accounts = sample_account_generator(True) # Generates new accounts to be modified within this test
        for account in sample_accounts: # Iterates over accounts in sample_accounts to make sure they're all considered
            with self.subTest(account=account): # Executes subtest so we see all error messages
                for amount in improper_amount_types: # Iterates over imporoper amount types to make sure they're all considered
                    with self.subTest(amount=amount): # Executes subtest so we see all error messages
                        with self.assertRaises(TypeError): #Checks to see if a TypeError was raised from an improper comparison
                            account.withdraw(amount)
                 
class sample_account_deposit_tests(unittest.TestCase):
    '''
    Executes test cases for the deposit method in sample_account
    '''
    def test_deposit_function(self):
        '''
        Checks that deposit, when given a proper amount value, functions correctly
        Checks both the modified balance within class and the returned value by deposit
        '''
        deposit_amounts = [(-1**x) * x**2 for x in range(0, len(balances))] # Generates deposit values to be added to 
        sample_accounts = sample_account_generator() # Generates new accounts to be modified within this test
        [account.set_balance(bal) for account, bal in zip(sample_accounts, balances)] # Sets account balances to the amounts above
        new_balances = [account.deposit(amount) for account, amount in zip(sample_accounts, deposit_amounts)] # Deposits amounts from above
        self.assertTrue(all([balance == (balances[x] + deposit_amounts[x]) for balance, x in zip(new_balances, range(0, len(balances)))])) # Checks that the stored balances are the deposit added to the balance
        self.assertTrue(all([account.balance == (balances[x] + deposit_amounts[x]) for account, x in zip(sample_accounts, range(0, len(balances)))])) # Checks that the returned values are the deposit added to the balance
    def test_deposit_empty(self):
        '''
        Checks that deposit raises an error when no amount is provided
        '''
        with self.assertRaises(TypeError):
            my_account = Customer("Spencer")
            my_account.set_balance()
            my_account.deposit()
    def test_deposit_unexpected_input(self):
        '''
        Checks that the deposit function behaves properly when given an improper input (non int/float)
        '''
        improper_amount_types = ['a', ('tuple'), ['list']] # List of improper amount types
        sample_accounts = sample_account_generator(True) # Generates new accounts to be modified within this test
        for account in sample_accounts: # Iterates over accounts in sample_accounts to make sure they're all considered
            with self.subTest(account=account): # Executes subtest so we see all error messages
                for amount in improper_amount_types: # Iterates over imporoper amount types to make sure they're all considered
                    with self.subTest(amount=amount): # Executes subtest so we see all error messages
                        with self.assertRaises(TypeError): #Checks to see if a TypeError was raised from an improper comparison
                            account.deposit(amount)
            

## Executes test cases ##
                            
test_cases = (sample_account_init_tests,
              sample_account_set_balance_tests,
              sample_account_withdraw_tests,
              sample_account_deposit_tests)

def test_case_loader(test_case_class):
    '''
    Loads the test cases from each separate class to allow them to be executed
    '''
    return unittest.TestLoader().loadTestsFromTestCase(test_case_class)
        
if __name__ == '__main__':
    '''
    Executes all the test cases
    '''
    for index in range(0, len(test_cases)):
        unittest.TextTestRunner().run(test_case_loader(test_cases[index]))
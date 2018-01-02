import unittest
from sample_account import Customer

## Unit Tests for each Function ##

class sample_account_init_tests(unittest.TestCase):
    '''
    Executes test cases for the __init__ method in sample_account
    '''
    def test_init_record_access(self):
        '''
        Checks that the __init__ method creates new Customer objects and stores the provided name
        '''
        customer_name = "Brad"
        sample_account = Customer(customer_name)
        self.assertEqual(customer_name, sample_account.name)
    def test_init_empty(self):
        '''
        Checks that the __init__ method raises an error when no name is provided
        '''
        with self.assertRaises(TypeError):
            Customer()
    def test_init_modify(self):
        '''
        Checks that the name attribute can be modified
        '''
        customer_name1 = "Brad"
        customer_name2 = "Steven"
        sample_account = Customer(customer_name1)
        self.assertEqual(customer_name1, sample_account.name)
        sample_account.name = customer_name2
        self.assertEqual(customer_name2, sample_account.name)
        
class sample_account_set_balance_tests(unittest.TestCase):
    '''
    Executes test cases for the set_balance method in sample_account
    '''
    def test_set_balance_record_access(self):
        '''
        Checks that we can set and access a balance using the set_balance method
        '''
        sample_account = Customer("Steven")
        this_balance = 15.0
        sample_account.set_balance(this_balance)
        self.assertEqual(sample_account.balance, this_balance)
    def test_set_balance_empty(self):
        '''
        Checks that the set_balance method sets a value of 0.0 when left empty
        '''
        sample_account = Customer("Spencer") # Creates new customer
        sample_account.set_balance() # Sets balance with no amount set
        self.assertEqual(sample_account.balance, 0.0) # Checks that the stored balance is equal to 0.0
    def test_set_balance_modify(self):
        '''
        Checks that the set_balance method will reset/allow for modification of the balance attribute
        '''
        balance1 = 12.5
        balance2 = 14.7
        sample_account = Customer("Sarah")
        sample_account.set_balance(balance1)
        self.assertEqual(sample_account.balance, balance1)
        sample_account.set_balance(balance2)
        self.assertEqual(sample_account.balance, balance2)
        
class sample_account_withdraw_tests(unittest.TestCase):
    '''
    Executes test cases for the withdraw method in sample_account
    '''
    def test_withdraw(self):
        '''
        Checks that withdraw, when given a proper amount value, functions correctly
        Checks both the modified balance within class and the returned value by withdraw
        '''
        this_balance = 13.7
        withdrawal = 8.5
        sample_account = Customer("Jessie")
        sample_account.set_balance(this_balance)
        self.assertEqual(sample_account.withdraw(withdrawal), this_balance - withdrawal)
        self.assertEqual(sample_account.balance, this_balance - withdrawal)
    def test_withdraw_insufficient_funds(self):
        '''
        Checks that the withdraw method will raise an exception when given a value less than the current balance
        '''
        this_balance = 250.53
        withdrawal = 999.99
        sample_account = Customer("Taylor")
        sample_account.set_balance(this_balance)
        with self.assertRaises(RuntimeError):
            sample_account.withdraw(withdrawal)
    def test_withdraw_empty(self):
        '''
        Checks that withdraw raises an error when no amount is provided
        '''
        with self.assertRaises(TypeError):
            this_account = Customer("James")
            this_account.set_balance()
            this_account.withdraw()
    def test_withdraw_no_balance(self):
        '''
        Checks that an error is raised if the balance attribute is not set
        '''
        with self.assertRaises(AttributeError):
            this_account = Customer("Lynn")
            this_account.withdraw(15)
                 
class sample_account_deposit_tests(unittest.TestCase):
    '''
    Executes test cases for the deposit method in sample_account
    '''
    def test_deposit_function(self):
        '''
        Checks that deposit, when given a proper amount value, functions correctly
        Checks both the modified balance within class and the returned value by deposit
        '''
        this_balance = 19.53
        this_deposit = 3.2
        sample_account = Customer("Michael")
        sample_account.set_balance(this_balance)
        self.assertEqual(sample_account.deposit(this_deposit), this_balance + this_deposit)
        self.assertEqual(sample_account.balance, this_balance + this_deposit)
    def test_deposit_empty(self):
        '''
        Checks that deposit raises an error when no amount is provided
        '''
        with self.assertRaises(TypeError):
            my_account = Customer("Spencer")
            my_account.set_balance()
            my_account.deposit()          

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
    for index in range(len(test_cases)):
        unittest.TextTestRunner().run(test_case_loader(test_cases[index]))
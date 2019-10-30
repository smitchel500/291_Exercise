# cashRegister.py
# Assignment 2
# CMSC 291, Fall 2019

class CashRegister:
    # Placement of money in the register
    __ONES = 0
    __FIVES = 1
    __TENS = 2
    __TWENTIES = 3

    # Constructor
    def __init__(self):
        self.__money = []   # self.__money = [0,0,0,0]
        for i in range(0, 4):
            self.__money.append(0)
        self.__locked = True

    def lock(self):
        self.__locked = True

    def unlock(self):
        self.__locked = False

    def __is_locked(self):
        return self.__locked

    """
    Precondition: money must contain amounts > 0
    """
    def add_money(self, money):
        # test if register is locked
        if self.__is_locked():
            print("Register is locked -- cannot add money")
        # add money
        else:
            self.__money[self.__ONES] += money[self.__ONES]
            self.__money[self.__FIVES] += money[self.__FIVES]
            self.__money[self.__TENS] += money[self.__TENS]
            self.__money[self.__TWENTIES] += money[self.__TWENTIES]

    """
    Precondition: money must contain amounts > 0
    """
    def remove_money(self, money):
        # test if register is locked
        if self.__is_locked():
            print("Register is locked -- cannot remove money")
        # test if enough money in register to remove
        elif \
            (self.__money[self.__ONES] < money[self.__ONES] or self.__money[self.__FIVES] < money[self.__FIVES] or \
             self.__money[self.__TENS] < money[self.__TENS] or self.__money[self.__TWENTIES] < money[self.__TWENTIES]):
            print("Not enough money in register -- cannot remove money")
        # remove money
        else:
            self.__money[self.__ONES] -= money[self.__ONES]
            self.__money[self.__FIVES] -= money[self.__FIVES]
            self.__money[self.__TENS] -= money[self.__TENS]
            self.__money[self.__TWENTIES] -= money[self.__TWENTIES]

    """
    Precondition: money must contain amounts > 0
    """
    def transfer_money(self, to_register, money):
        # test if from-register is locked
        if self.__is_locked():
            print("From register is locked -- cannot transfer money")
        # test if to-register is locked
        elif to_register.__is_locked():
            print("To register is locked -- cannot transfer money")
        # test if enough money in from-register to transfer
        elif \
            (self.__money[self.__ONES] < money[self.__ONES] or self.__money[self.__FIVES] < money[self.__FIVES] or \
             self.__money[self.__TENS] < money[self.__TENS] or self.__money[self.__TWENTIES] < money[self.__TWENTIES]):
            print("Not enough money in from register -- cannot transfer money")
        # transfer money
        else:
            self.remove_money(money)
            to_register.add_money(money)

    def _total_money(self):
        return (self.__money[self.__ONES]) + (self.__money[self.__FIVES] * 5) + \
            (self.__money[self.__TENS] * 10) + (self.__money[self.__TWENTIES] * 20)

    def clear_register(self):
        self.__locked = False
        total = self._total_money()
        for i in range(len(self.__money)):
            self.__money[i] = 0

        return (total)

    def status(self):
        locked_str =  "locked." if self.__locked else "unlocked."

        return "Register is " + locked_str + "\nOnes: " + str(self.__money[self.__ONES]) + '\n' \
            + "Fives: " + str(self.__money[self.__FIVES]) + '\n' \
            + "Tens: " + str(self.__money[self.__TENS]) + '\n' \
            + "Twenties: " + str(self.__money[self.__TWENTIES]) + '\n' \
            + "Total in register: $ " + str(self._total_money())

    # Unit Testing
"""
if __name__ == '__main__':
    # Testing constructor and status()
    print("***Testing constructor() and status()***")
    cr1 = CashRegister()
    print(cr1.status())
    print()

    # Testing unlock() and lock()
    print("***Testing lock() and unlock()***")
    cr2 = CashRegister()
    print(cr2.status())  # register is locked
    print()
    cr2.unlock()
    print(cr2.status())  # register is now unlocked
    print()
    cr2.lock()
    print(cr2.status())  # register is locked again
    print()

    # Testing total_money()
    print("***Testing total_money()***")
    cr3 = CashRegister()
    print("Drawer total: $" + str(cr3._total_money()))
    print()

    # Testing add_money()
    print("***Testing add_money()***")
    cr4 = CashRegister()
    print(cr4.status()) # register is locked
    print("Success = " + str(cr4.add_money(money))) # fail
    cr4.unlock() # unlock register
    print(cr4.status())
    print("Success = " + str(cr4.add_money(money))) # success
    print(cr4.status())
    print("Success = " + str(cr4.add_money(money))) # negative $
    print(cr4.status()) # fail
    print()

    # Testing remove_money()
    print("***Testing remove_money()***")
    cr5 = CashRegister()
    print(cr5.status()) # register is locked
    cr5.unlock() # unlock register
    print(cr5.status()) # register is unlocked
    print("Success = " + str(cr5.add_money(money))) # add money
    print(cr5.status()) # success
    print("Success = " + str(cr5.remove_money(money))) # negative $
    print(cr5.status()) # fail
    print("Success = " + str(cr5.remove_money(money)) # good $
    print(cr5.status()) # success
    print("Success = " + str(cr5.remove_money(money))) # too much $
    print(cr5.status()) # fail
    cr5.lock() # lock register
    print("Success = " + str(cr5.remove_money(money))) # locked
    print(cr5.status()) # fail
    print()
"""
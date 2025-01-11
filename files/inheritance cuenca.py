class BancAcc:
    def __init__(self,acc_holder,acc_num,acc_balance):
        self.acc_holder = acc_holder
        self.num = acc_num
        self.acc_balance = acc_balance

    def deposit(self,add):
        newbal = self.acc_balance + add
        self.acc_balance = newbal

    def withdraw(self,minus):
        if self.acc_balance >= minus:
            newbal = self.acc_balance - minus
            self.acc_balance = newbal
        else:
            print("Not enough funds\nBalance stays the same")

    def dispinfo(self):
        print(f"Account Holder Name: {self.acc_holder} \nAccount Number: {self.acc_num} \nAccount Balance = {self.acc_balance}")


class SaveAcc(BancAcc):
    def __init__(self,int_r,acc_holder,acc_num,acc_balance):
        self.int_r = int_r
        self.acc_holder = acc_holder
        self.acc_num = acc_num
        self.acc_balance = acc_balance

    def dispinfo(self):
        super().dispinfo()
        print(f"Account Interest Rate: {self.int_r}%")


bank1 = SaveAcc(14,"Janus",5001,25000)
bank1.deposit(500)
bank1.dispinfo()

bank2 = SaveAcc(12,"Jake",5002,50000)
bank2.withdraw(20000)
bank2.dispinfo()


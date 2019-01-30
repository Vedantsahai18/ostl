class Bank:
    clsid = 0 
    def __init__(self):
        self.name = " "
        self.depo = 0
        self.__cls__.clsid+=1
        self.eid = eid
    def createAcc(self,eid):
        self.name = input("Enter name: ")
        self.depo = int(input("Enter initial deposit: "))
        print("Your id is " , self.eid )
    def addBalance(self , dep):
        self.depo=self.depo+dep
        print("Updated Balance is " , self.depo)
    def withdraw(self , wit):
        if self.depo==0:
            print(" Insufficient Balance ")
        else:    
            self.depo=self.depo-wit
            print("Current Balance is " , self.depo)
    def dispBal(self):
        print(self.eid , " Balance is "  , self.depo)
    def showCount(cls):
        print("Number of employees " , cls.clsid )

blist = list()
exit  = False
count=0
eid=10
while not exit:
    print("Enter 1: Create New Acc")
    print("Enter 2: To Make Transactions")
    print("Enter 3: To Display Balance")
    print("Enter 4: To know the total number of employess")
    print("Enter 0: To Exit")
    ch = int(input())
    if ch == 1:
        eid=eid+1   
        b = Bank()
        b.createAcc(eid)
        blist.append(b)
        count+=1
    elif ch == 2:
        cid = int(input("Enter id "))
        tid = input("Enter 1: To Deposite 2: To Withdraw")
        amt = int(input("Enter Amount "))
        if tid == 1:
            blist[cid-11].addBalance(amt)
        else:
            blist[cid-11].withdraw(amt)
    elif ch == 3:
        cid = int(input("Enter id "))
        blist[cid-11].dispBal()
    elif ch == 4:
        Bank.showCount()
    else:
        exit = True

import filepost

def postbank():
    print ("Информационная система банка. Мы всегда открыты\n")
    prompt=int(input("""Завести счет с помощью работников банка, нажмите 1\n"""+
                        """Если вы пользователь, нажмите 2\n"""))
    if prompt==1:
        cus=BankAccount()#creates a new customer profile
        cus.cashofcustomers()
    elif prompt==2:
        cus=ReturnCustomer()#checks for existing customer
        cus.cashofcustomer()

    else:
        print("Выберите дальнейшее действие:")
        postbank()


class BankAccount():
    #maybe def createuser-?
    def __init__(self):
        ##calls functions in the module filestore
        self.last_name=input("Введите фамилию:")
        self.first_name=input("Введите имя:")
        self.money = input("Количество денег на счете в рублях:")
        self.bank_id,self.account_id=filepost.check(self.last_name,self.first_name)
        self.activate()

        # print(
        #     "Thank you %s, your account is set up and ready to use,\n a 100 pounds has been credited to your account" % self.username)
        #self.userfunctions()

    #activation of account. for this case it's adding to csv file
    def activate(self):
        filepost.activate(self.last_name,self.first_name,self.bank_id,self.account_id,self.money)
    #gets cash of all customers

    def cashofcustomers(self):
        print(filepost.getallcash())
    #gets list of all accounts

    def listofcustomers(self):
        print(filepost.listofaccounts())
        #how to pretty write it?


#working with customer class
class ReturnCustomer():
    def __init__(self):
        self.account_id=input("Введите номер аккаунта:")
        self.last_name,self.first_name,self.bank_id,self.money = filepost.checkuser(self.account_id)
        #self.transate()
        #self.userfunctions()

    def cashofcustomer(self):
        print(self.money)

    def transate(self):
        self.post_account=input("Введите номер аккаунта на который деньги положить:")
        self.money_send=input("Введите количество денег:")
        print(filepost.transate(self.account_id,self.post_account,self.money_send))

    def history_transate(self):
        self.history=filepost.history(self.account_id)
        print(self.history)


postbank()
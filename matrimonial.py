import logging
import pickle
import sys
import random
import string

#############################Custom Logger###############################
#loggger object
logger= logging.getLogger('getCustomLogger')
logger.setLevel(logging.DEBUG)
#consol handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
#formattor object
formatter=logging.Formatter('%(asctime)s --%(levelname)s --%(message)s',datefmt= '%d/%m/%Y %I:%M:%S')
consoleHandler.setFormatter(formatter)
#file handler
fileHandler=logging.FileHandler('matrimonialException.log',mode='a')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)
#add handler
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
#############################End of Custom Logger###############################
#Custom User_Exception
class User_Exception(Exception):
    def __init__(self,msg):
        self.msg=msg

class User:
    def __init__(self,name,sex,age,mobNo):
        self.name=name
        self.age=age
        self.sex=sex
        self.mobNo=mobNo

class Customer:
    def __init__(self,name,uid,sex,age,mobNo):
        self.name=name
        self.uid=uid
        self.age=age
        self.sex=sex
        self.mobNo=mobNo

    def display(self):
        print(f'Name : {self.name} \nUsername : {self.uid} \nAge : {self.age} \nSex : {self.sex} \nMobile : {self.mobNo} \n')

def addUser():
    uList=[]
    try:
        name=input("Enter Your Name :").title()
        try:
            age=int(input("Enter age 18-30 :"))
            if age <18:
                raise User_Exception('*** Age is below 18!!!.{}'.format(name))
            elif age>30:
                raise User_Exception('*** Age is a above 30!!!.{}'.format(name))
        except User_Exception as msg:
            logger.info(msg)
            sys.exit(0)
        sex=input("Male or Female : ").title()
        try:
            if sex != 'Male' and sex != 'Female':
                raise User_Exception('* No Other Gender Excepted!!!')
        except User_Exception as msg:
            logger.info(msg)
            sys.exit(0)
        mobNo=int(input("Mobile Number: "))
        x=User(name,sex,age,mobNo)
        try:
            with open('userdata.pkl','rb') as f:
                uList=pickle.load(f)
            with open('userdata.pkl','wb') as f:
                uList.append(x)
                pickle.dump(uList,f)
            logger.info('User Deatil Entered : {} - {} - {}'.format(name,sex,age))
        except FileNotFoundError:
            with open('userdata.pkl','wb') as f:
                uList.append(x)
                pickle.dump(uList,f)
                logger.info('User Deatil Entered : {} - {} - {}'.format(name,sex,age))
    except BaseException as msg:
        logger.error('Invalid Format Error Code : {}'.format(msg))

def randomString(stringLength=10):
    lettersAndDigits = string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength)) 
        
def addCustomer():
    uList=[]
    try:
        name=input("Enter Your Name :").title()
        uid=name+randomString(3)
        try:
            age=int(input("Enter age 18-30 :"))
            if age <18:
                raise User_Exception('*** Age is below 18!.{}'.format(name))
            elif age>30:
                raise User_Exception('Age is above 30!.{}'.format(name))
        except User_Exception as msg:
            logger.info(msg)
            sys.exit(0)
        sex=input("Male or Female : ").title()
        try:
            if sex != 'Male' and sex != 'Female':
                raise User_Exception('\n* No Other Gender Excepted\n!!!')
        except User_Exception as msg:
            logger.info(msg)
            sys.exit(0)
        mobNo=int(input("Mobile Number: "))
        x=Customer(name,uid,sex,age,mobNo)
        try:
            with open('customerdata.pkl','rb') as f:
                uList=pickle.load(f)
            with open('customerdata.pkl','wb') as f:
                uList.append(x)
                pickle.dump(uList,f)
            logger.info('Customer Deatil Entered : {} - {} - {} - {}'.format(name,uid,sex,age))
        except BaseException:
            with open('customerdata.pkl','wb') as f:
                uList.append(x)
                pickle.dump(uList,f)
                logger.info('Customer Deatil Entered : {} -  {} - {} - {}'.format(name,uid,sex,age))
    except BaseException as msg:
        logger.error('Invalid Format Error Code : {}'.format(msg))

def delUser(delstring):
    s=delstring.title()
    try:
        with open('userdata.pkl','rb') as f:
            uList=pickle.load(f)
            c=0
            len_uList=len(uList)
            for i in uList:
                if s==i.name:
                    del uList[c]
                    logger.info('User Deleted: {}'.format(s))
                c=c+1
            len_newuList=len(uList)
            if len_uList==len_newuList:
                #print('\n* No Data Found\n')
                raise User_Exception('\n* while deleting {} : User data not found\n'.format(s))
        with open('userdata.pkl','wb') as f:
            pickle.dump(uList,f)                  
    except BaseException as msg:
        logger.error(msg)

def delCustomer(delstring):
    s=delstring.title()
    try:
        with open('customerdata.pkl','rb') as f:
            uList=pickle.load(f)
            c=0
            len_uList=len(uList)
            for i in uList:
                if s==i.uid:
                    del uList[c]
                    logger.info('Customer Deleted: {}'.format(s))
                c=c+1
            len_newuList=len(uList)
            if len_uList==len_newuList:
                raise User_Exception('* while deleting {} : Customer data not found'.format(s))
        with open('customerdata.pkl','wb') as f:
            pickle.dump(uList,f) 
    except User_Exception as msg:
        logger.error(msg)
    except BaseException as msg:
        logger.error(msg) 
        sys.exit(0)   

def viewUsers():
    try:
        sys.exit(0)
    except SystemExit:
        with open('userdata.pkl','rb') as f:
            print('\t--------------------------------\n\t|-------Discover Users-------|\n\t--------------------------------')
            while True:
                try:
                    loadedobj=pickle.load(f)
                    for i in loadedobj:
                        print(f'|{i.name}\t{i.age}\t{i.sex}\t{i.mobNo}|')
                except EOFError:
                    logger.info('User Data View')
                    break
        print('-------------------------------------------')

def viewCustomer():
    try:
        sys.exit(0)
    except SystemExit:
        with open('customerdata.pkl','rb') as f:
            print('\t--------------------------------\n\t|-------Discover Partner-------|\n\t--------------------------------')
            while True:
                try:
                    loadedobj=pickle.load(f)
                    for i in loadedobj:
                        print(f'|{i.name}\t{i.uid}\t{i.age}\t{i.sex}\t{i.mobNo}|')
                except EOFError:
                    logger.info('Customer Data View')
                    break
        print('-------------------------------------------')

def AdminMain():
    while 1:
        try:
            choice=int(input("1. Add User Detail \n2. Discover User Partner \n3. Delete User's Detail \n4. Add Customer Detail \n5. Discover Customer Partner \n6. Delete Customer's Detail\n0. Exit \n::::::::->  "))
            if choice == 1:
                addUser()
            elif choice == 2:
                viewUsers()
            elif choice == 3:
                delstring = input('Enter Name to delete : ')
                delUser(delstring)
            elif choice == 4:
                addCustomer()
            elif choice == 5:
                viewCustomer()
            elif choice == 6:
                delstring = input('Enter Uid to delete : ')
                delCustomer(delstring)
            elif choice == 0:
                sys.exit(0)
            else:
                print("!!! Invalid Choice !!!")
        except SystemExit as msg :
            logger.info('Successfully Admin returned with {}'.format(msg))
            break
def CustomerMain():
    uList = []
    cList = []
    while True:
        print("\n\tCustomer Panel\n")
        choice=int(input("1.Sign Up \t2.Sign In \n3.Delete Data \t0.Exit : "))
        if choice == 1:
            addCustomer()
        elif choice == 2:
            username=input("Enter Your Username : ")
            try:
                with open('Customerdata.pkl','rb') as f:
                    cList=pickle.load(f)
                    for i in cList:
                        if username==i.uid:
                            sexID=i.sex
                            if sexID == 'Male':
                                x='Male'
                            else:
                                x='Female'
                            logger.info("Welcome {} : {}".format(i.name,x))
                            print('1. Find Match \t2. Exit :')
                            with open('userdata.pkl','rb') as f:
                                uList=pickle.load(f)
                            list1 = [i for i in uList if i in cList]
                            list2 = [i for i in uList if i not in cList]
                            list3 = [i for i in cList if i not in uList]
                            newList = list1+list2+list3
                            opt=int(input('Enter Option : '))
                            if opt==1:
                                for j in newList:
                                    if x=='Male':
                                        if j.sex=='Female':
                                            print(f'|{j.name}\t{j.age}\t{j.sex}\t{j.mobNo}|')
                                    elif x=='Female':
                                        if j.sex=='Male':
                                            print(f'|{j.name}\t{j.age}\t{j.sex}\t{j.mobNo}|')
                            elif  opt==2:
                                calling()
            except BaseException as msg:
                logger.info(msg)
                break
        elif choice == 3:
            username=input("Enter Your Username : ")
            delCustomer(username)
        elif choice == 0:
            calling()

def UserMain():
    try:
        addUser()
        sys.exit(0)
    except SystemExit:
        logger.info('User Exits successfully')

def calling():
    try:
        sys.exit(0)
    except:
        while True:
            try:
                c=int(input("1.User\n2.Customer\n3.Admin\n0.Exit\n:::::::::->"))
                if c==1:
                    UserMain()
                elif c==2:
                    CustomerMain()
                elif c==3:
                    AdminMain()
                elif c==0:
                    sys.exit(0)
                else:
                    print('Invalid option')
            except SystemExit as msg:
                logger.error(msg)
                sys.exit(0)
calling()

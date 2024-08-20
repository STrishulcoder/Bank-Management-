import mysql.connector as s
m=s.connect(host='localhost',user='root',passwd='sai',database='Bank')
c=m.cursor()
print('='*80)
print(' '*29,end='')
print('| BANK MANAGEMENT SYSTEM |')
print('='*80)
ac=10001
while True:
    print('1.OPEN NEW ACCOUNT')
    print('2.ACCOUNT DETAILS')
    print('3.MONEY WITHDRAWAL')
    print('4.MONEY DEPOSIT')
    print('5.ACCOUNT STATEMENT')
    print('6.EXIT')
    choice=int(input('Enter Your Choice:'))
    if choice==1:
        uname=input('Enter Username:')
        passwd=input('Enter Password:')
        b=int(input('Enter Opening Balance:'))
        no=input('Enter Mobile Number:')
        a=input('Enter Nationality:')
        mail=input('Enter E-Mail:')
        des=input('Enter Designation:')
        dob=input('Enter Your Date of Birth(D.O.B):')
        query2="select max(Accountno) from details"
        c.execute(query2)
        data=c.fetchone()
        data2=data[0]
        acc=data2+7
        print("Your Account Number is:",acc)
        query="insert into details values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(acc,uname,passwd,b,no,a,mail,des,dob)
        c.execute(query)
        m.commit()
        from datetime import date
        today=date.today()
        print('Account Opened Successfully on',today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==2:
        account=int(input('Enter account number:'))
        passwd=input('Enter Your Password:')
        query="select*from details where Accountno={} and Password='{}'".format(account,passwd)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==3:
        account=input('Enter Account Number:')
        passwd=input('Enter Your Password:')
        withdraw=int(input('Enter Withdraw Amount:'))
        query="update details set Balance=Balance-{} where Password='{}'".format(withdraw,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+account
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Withdrawal of Rs.",withdraw,"is completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==4:
        account=int(input('Enter Account Number:'))
        passwd=input('Enter Your Password:')
        deposit=int(input('Enter Deposit Amount:'))
        query="update details set Balance=Balance+{} where Password='{}'".format(deposit,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+str(account)
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Deposit of Rs.",deposit,"is successfully completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==5:
        account=int(input('Enter Account Number:'))
        query="select Accountno,Username,Balance from details where Accountno="+str(account)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Account Statement")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[2])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==6:
        break
        
        
        
        
        
    







'''import mysql.connector as s
m=s.connect(host='localhost',user='root',passwd='sai',database='Bank')
c=m.cursor()
print('='*80)
print(' '*29,end='')
print('| BANK MANAGEMENT SYSTEM |')
print('='*80)
ac=10001
while True:
    print('1.OPEN NEW ACCOUNT')
    print('2.ACCOUNT DETAILS')
    print('3.MONEY WITHDRAWAL')
    print('4.MONEY DEPOSIT')
    print('5.ACCOUNT STATEMENT')
    print('6.EXIT')
    choice=int(input('Enter Your Choice:'))
    if choice==1:
        uname=input('Enter Username:')
        passwd=input('Enter Password:')
        b=int(input('Enter Opening Balance:'))
        no=input('Enter Mobile Number:')
        a=input('Enter Nationality:')
        mail=input('Enter E-Mail:')
        des=input('Enter Designation:')
        dob=input('Enter Your Date of Birth(D.O.B):')
        query2="select max(Accountno) from details"
        c.execute(query2)
        data=c.fetchone()
        print(data)
        if len(data)>1:
            query2="select max(Accountno) from details"
            c.execute(query2)
            data=c.fetchone()
            data2=data[0]
            acc=data2+7
            print("Your Account Number is:",acc)
            query="insert into details values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(acc,uname,passwd,b,no,a,mail,des,dob)
            c.execute(query)
            m.commit()
        else:
            ac=10001
            print("Your Account Number is:",ac)
            query="insert into details values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(ac,uname,passwd,b,no,a,mail,des,dob)
            c.execute(query)
            m.commit()
        from datetime import date
        today=date.today()
        print('Account Opened Successfully on',today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==2:
        account=int(input('Enter account number:'))
        passwd=input('Enter Your Password:')
        query="select*from details where Accountno={} and Password='{}'".format(account,passwd)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==3:
        account=input('Enter Account Number:')
        passwd=input('Enter Your Password:')
        withdraw=int(input('Enter Withdraw Amount:'))
        query="update details set Balance=Balance-{} where Password='{}'".format(withdraw,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+account
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Withdrawal of Rs.",withdraw,"is completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==4:
        account=int(input('Enter Account Number:'))
        passwd=input('Enter Your Password:')
        deposit=int(input('Enter Deposit Amount:'))
        query="update details set Balance=Balance+{} where Password='{}'".format(deposit,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+str(account)
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Deposit of Rs.",deposit,"is successfully completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==5:
        account=int(input('Enter Account Number:'))
        query="select Accountno,Username,Balance from details where Accountno="+str(account)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Account Statement")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[2])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==6:
        break'''













        
        
        
        
'''import mysql.connector as s
m=s.connect(host='localhost',user='root',passwd='sai',database='Bank')
c=m.cursor()
print('='*80)
print(' '*29,end='')
print('| BANK MANAGEMENT SYSTEM |')
print('='*80)
ac=10001
while True:
    print('1.OPEN NEW ACCOUNT')
    print('2.ACCOUNT DETAILS')
    print('3.MONEY WITHDRAWAL')
    print('4.MONEY DEPOSIT')
    print('5.ACCOUNT STATEMENT')
    print('6.EXIT')
    choice=int(input('Enter Your Choice:'))
    if choice==1:
        uname=input('Enter Username:')
        passwd=input('Enter Password:')
        b=int(input('Enter Opening Balance:'))
        no=input('Enter Mobile Number:')
        a=input('Enter Nationality:')
        mail=input('Enter E-Mail:')
        des=input('Enter Designation:')
        dob=input('Enter Your Date of Birth(D.O.B):')
        query2="select max(Accountno) from details"
        c.execute(query2)
        data=c.fetchone()
        
        if len(data)==None:
            ac=10001
            print("Your Account Number is:",ac)
            query="insert into details values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(ac,uname,passwd,b,no,a,mail,des,dob)
            c.execute(query)
            m.commit()
            query2="select max(Accountno) from details"
            c.execute(query2)
            
        elif len(data)>1:
            data=c.fetchone()
            data2=data[0]
            acc=data2+7
            print("Your Account Number is:",acc)
            query="insert into details values({},'{}','{}',{},'{}','{}','{}','{}','{}')".format(acc,uname,passwd,b,no,a,mail,des,dob)
            c.execute(query)
            m.commit()
            
        from datetime import date
        today=date.today()
        print('Account Opened Successfully on',today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==2:
        account=int(input('Enter account number:'))
        passwd=input('Enter Your Password:')
        query="select*from details where Accountno={} and Password='{}'".format(account,passwd)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==3:
        account=input('Enter Account Number:')
        passwd=input('Enter Your Password:')
        withdraw=int(input('Enter Withdraw Amount:'))
        query="update details set Balance=Balance-{} where Password='{}'".format(withdraw,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+account
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Withdrawal of Rs.",withdraw,"is completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==4:
        account=int(input('Enter Account Number:'))
        passwd=input('Enter Your Password:')
        deposit=int(input('Enter Deposit Amount:'))
        query="update details set Balance=Balance+{} where Password='{}'".format(deposit,passwd)
        c.execute(query)
        m.commit()
        query2="select*from details where Accountno="+str(account)
        c.execute(query2)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Bank Account Details\n")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[3])
        print("Registered Mobile Number:",data[4])
        print("Nationality             :",data[5])
        print("E-Mail Address          :",data[6])
        print("Designation             :",data[7])
        print("Date of Birth           :",data[8])
        from datetime import date
        today=date.today()
        print("Deposit of Rs.",deposit,"is successfully completed on",today)
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==5:
        account=int(input('Enter Account Number:'))
        query="select Accountno,Username,Balance from details where Accountno="+str(account)
        c.execute(query)
        data=c.fetchone()
        print(' '*29,end='')
        print("Your Account Statement")
        print("Account Number          :",data[0])
        print("User Name               :",data[1])
        print("Account Balance         : Rs.",data[2])
        print('='*80)
        print(' '*80)
        print('='*80)
    elif choice==6:
        break'''
    

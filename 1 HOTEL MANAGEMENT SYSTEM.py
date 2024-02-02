import mysql.connector
pass_word=input("Enter your sql password: ") 
db=input("Enter your database name: ")
my_database=mysql.connector.connect(host='localhost',database=db,user='root',password=pass_word,autocommit=True)
c=my_database.cursor()

if my_database.is_connected():
    print('successfully connected')

print('......WELCOME......')


def menu():
    print('HOTEL MANAGEMENT SYSTEM')
    print()
    print('1. employ column')
    print('2. customer column')
    print('3. room department')
    print('4. restaurant department')
    print('5. laundary department')
    print('6. game department')
    print('7. Total bill') # to evaluate overall bill from all the departments

# employs...............................................................................
# sub-functions--------------------------------------------------------------
def show_employ():
    print('SHOWING EMPLOYES DETAILS')
    print()
    g=('ID','name','department','salary','contactno')
    print(g)
    c.execute('select* from employs')
    for i in c:
        print(i)
def add_employ():
     n=input('enter name')
     a=input('enter ID')
     no=input('mobile no')
     cin=input(' enter salary')
     t=input(' enter department')
     R=[a,n,t,cin,no]
     c=my_database.cursor()
     c.execute("insert into employs values(%s,%s,%s,%s,%s)",R)
     print('......details added successfully......')
def update_employdetails():
    u=input('what do you want to update?(department/mobile no/salary)')
    if u=='department':
          print('updating department')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          c.execute("update employs set department = %s where employname =%s ",y)
    elif u=='mobile no':
          print('updating number')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          c.execute("update employs set contactno = %s where employname =%s ",y)
    elif u=='salary':
          print('updating salary')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          c.execute("update employs set salary = %s where employname =%s ",y)
    else:
         print(u,'cannot be updated....')
    print('....update completed........')
#-----------------------------------------------------------------------------------
# main-function
def employ_column():
    print('-------welcome to employ column------------')
    print('1. show employ details')
    print('2. add new employ details')
    print('3. update employ details')
    while True:
          o=input('enter your choice')
          if o=='1':
               show_employ()
          elif o=='2':
               add_employ()
          elif o=='3':
               update_employdetails()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('##############exit employ column###################')


#....................................................................................................



#customer........................................................................................
#sub-functions-----------------------------------------------------------------
def show_customer():
    print('SHOWING CUSTOMER DETAILS')
    print()
    a=('name','address','mobile no','checkin','checkout')
    print(a)
    c.execute('select* from customerdetails')
    for i in c:
        print(i)
def add_customer():
     n=input('enter name')
     a=input('enter address')
     no=input('mobile no')
     cin=input(' enter checkin date(yy-mm-dd)')
     cout=input(' enter checkout date(yy-mm-dd)')
     R=[n,a,no,cin,cout]
     c=my_database.cursor()
     c.execute("insert into customerdetails(name,address,mobileno,checkin,checkout)values(%s,%s,%s,%s,%s)",R)
     print('..........details added successfully...........')
                
def update_customerdetails():
    u=input('what do you want to update?(address/mobile no/checkout)')
    if u=='address':
          print('updating address')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          print(y)
          c.execute("update customerdetails set address = %s where name =%s ",y)

    elif u=='mobile no':
          print('updating mobile no')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          c.execute("update customerdetails set mobileno = %s where name=%s ",y)
    elif u=='checkout':
          print('updating checkout')
          b=input ('enter update')
          n=input('enter name ')
          y=(b,n)
          c.execute("update customerdetails set checkout = %s where name=%s ",y)

    else:
         print(u,'cannot be updated....')
    print('......update conmplete.........')

#----------------------------------------------------------------------------------------------
# main-function
def customer_column():
    print('-------welcome to customer column------------')
    print('1. show customer details')
    print('2. add new customer details')
    print('3. update customer details')
    while True:
          o=input('enter your choice')
          if o=='1':
               show_customer()
          elif o=='2':
               add_customer()
          elif o=='3':
               update_customerdetails()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('##############exit customer column##################')

#.....................................................................................................
#........................................................................................................



#room department...................................................................................
#................................................................................................
#sub-functions--------------------------------------------------------
def rooms():
    print('--------SHOWING room menu----------')
    print()
    a=('sno','type','rent','total rooms','availability')
    print(a)
    c.execute('select * from roomtype')
    for i in c:
        print(i)
def room_availability():
    c.execute('select*from roomtype')
    a=input('enter room type')
    for i in c:
             if i[1]==a:
                x=i[4]
                print(x,'rooms availabe')
                return x
def room_bill():
    print('----processing room bill------')
    b=0
    while True:
           c=my_database.cursor()
           c.execute('select* from roomtype')
           u= input('type')
           j=int(input('no of days you will stay'))
           p=0
           for i in c:
               if i[1]==u:
                      s=i[2]
                      p=p+s
                      o=j*p
           b=b+o
           q=input('add more rooms (y/n)')
           if q=='n' or q=='N':
               break
           
    print('room bill=',b)
    return b

def update_room():
     u=input('what do you want to update?(rent/availability)')
     if u=='rent':
          print('updating room charges')
          b=input ('enter updated rate')
          n=input('enter roomtype ')
          y=(b,n)
          c.execute("update roomtype set rent = %s where type =%s ",y)
     elif u=='availability':
          print('updating room availability')
          b=input ('enter update')
          n=input('enter roomtype ')
          y=(b,n)
          c.execute("update roomtype set availability = %s where type=%s ",y)
     else:
         print(u,'cannot be updated....')
     print('......update conmplete.........')

#---------------------------------------------------------------------------------
# main-function
def room_column():
    print('-------welcome to room department------------')
    print('1. show room details')
    print('2. show room availability')
    print('3. show room bill')
    print('4. update room details')
    while True:
          o=input('enter your choice')
          if o=='1':
               rooms()
          elif o=='2':
               room_availability()
          elif o=='3':
               room_bill()
          elif o=='4':
               update_room()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('################exit room column###################')


#...........................................................................................
#..................................................................................................





#restaurant department........................................................................
#...............................................................................................
#sub-functions-------------------------------------------------------------------------
def restaurant_menu():
    a=('sno','item','rate')
    print('--------SHOWING restaurant menu----------')
    print()
    print(a)
    c.execute('select* from restaurant')
    for i in c:
        print(i)
      

def restaurant_bill():
    print('--------processing restaurant bill---------')
    b=0
    while True:
               o=0
               c=my_database.cursor()
               u= input('Item Name:')
               c.execute(f"SELECT * FROM  restaurant WHERE item = '{u}'")
               r=c.fetchall()
               while (r==[]):
                   u= input('Item Name:')
                   c.execute(f"SELECT * FROM  restaurant WHERE item = '{u}'")
                   r=c.fetchall()
               y=int(input('no of items'))
               c.execute('select* from restaurant')
               for i in c.fetchall():
                   if i[1]==u:
                        s=i[2]
                        o=y*(s)
                        
                       
               b=b+o
               q=input('add more item (y/n)')
               if q=='n' or q=='N':
                              break
                                           
    print('restaurant bill =',b)
    return b   

def update_restaurant():
     print('updating rate of resturant items')
     b=input ('enter updated rate')
     n=input('enter itemname')
     y=(b,n)
     print(y)
     c.execute("update restaurant set rate = %s where item=%s ",y)
     print('......update conmplete.........')

#--------------------------------------------------------------------------------
#main-function
def restaurant_column():
    print('-------welcome to restaurant department------------')
    print('1. show restaurant menu')
    print('2. show restaurant bill')
    print('3. update restaurant details')
    while True:
          o=input('enter your choice')
          if o=='1':
               restaurant_menu()
          elif o=='2':
               restaurant_bill()
          elif o=='3':
               update_restaurant()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('###############exit restaurant column######################')

#..................................................................................
#..................................................................................




#laundary department..................................................................
#...................................................................................
#sub_functions----------------------------------------------------
def laundary():
    print('SHOWING laundary DETAILS')
    print()
    a=('sno','itemname','rate')
    print(a)
    c.execute('select* from laundary')
    for i in c:
        print(i)

def laundary_bill():
    print('----processing laundary bill------')
    b=0
    while True:
           c=my_database.cursor()
           c.execute('select* from laundary')
           u= input('item type')
           j=int(input('no of items'))
           p=0
           for i in c:
               if i[1]==u:
                      s=i[2]
                      p=p+s
                      o=j*p
           b=b+o
           q=input('add more items (y/n)')
           if q=='n' or q=='N':
               break
           
    print('laundary bill=',b)
    return b
def update_laundary():
     print('updating rate of laundary items')
     b=input ('enter updated rate')
     n=input('enter itemname')
     y=(b,n)
     print(y)
     c.execute("update laundary set rate = %s where itemname=%s ",y)
     print('......update conmplete.........')
#---------------------------------------------------------------------
#main_function
def laundary_column():
    print('-------welcome to laundary department------------')
    print('1. show laundary menu')
    print('2. show laundary bill')
    print('3. update laundary details')
    while True:
          o=input('enter your choice')
          if o=='1':
               laundary()
          elif o=='2':
               laundary_bill()
          elif o=='3':
               update_laundary()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('##################exit laundary department#########################')

#.......................................................................
           #.......................................................................



#game department........................................................
#......................................................................
#sub-functions----------------------------------------------------
def game():
    print('SHOWING GAMES DETAILS')
    print()
    a=('sno','game name', 'charges')
    print(a)
    c.execute('select* from game')
    for i in c:
        print(i)
def game_bill():
    print('----processing game bill------')
    b=0
    while True:
           c=my_database.cursor()
           c.execute('select* from game')
           u= input('game name')
           j=int(input('no of players'))
           p=0
           for i in c:
               if i[1]==u:
                      s=i[2]
                      p=p+s
                      o=j*p
           b=b+o
           q=input('add more games (y/n)')
           if q=='n' or q=='N':
               break
           
    print('game bill=',b)
    return b
def update_game():
     print('updating game charges')
     b=input ('enter updated rate')
     n=input('enter game name')
     y=(b,n)
     print(y)
     c.execute("update game set charges = %s where gamename=%s ",y)
     print('......update conmplete.........')
#-------------------------------------------------------------
#main-function
def game_column():
    print('-------welcome to game department------------')
    print('1. show game menu')
    print('2. show game bill')
    print('3. update game details')
    while True:
          o=input('enter your choice')
          if o=='1':
               game()
          elif o=='2':
               game_bill()
          elif o=='3':
               update_game()
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N':
               break
    print('#################exit  game  department#######################')
#.......................................................................
    #...............................................................................



#totalbill...............................................................
#...................................................................................
def bill():
    t=0
    p=input('room service?(y/n)')
    if p=='y' or p=='Y':
        a=room_bill()
        t+=a
    q=input('laundary service ?(y/n)')
    if q=='y' or q=='Y':
        b=laundary_bill()
        t+=b
    r=input('restaurant service?(y/n)')
    if r=='y' or r=='Y':
        c=restaurant_bill()
        t+=c
    s=input('game service?(y/n)')
    if s=='y' or s=='Y':
        d=game_bill()
        t+=d
    print('total bill',t)
#........................................................................
    #...................................................................................








#######################  MAIN BODY  #################################

w=input('do you want to see menu? (y/n)')
if w=='y' or w=='Y':
    menu()
    while True:
          o=input('enter your choice or type exit to leave')
          if o=='1':
               employ_column()
          elif o=='2':
               customer_column()
          elif o=='3':
               room_column()
          elif o=='4':
               restaurant_column()
          elif o=='5':
               laundary_column()
          elif o=='6':
               game_column()
          elif o=='7':
               bill()
          elif o=='exit' or o=='EXIT':
               break     
          else:
              print('no such choice available')
          t=input('do you want to enter another choice?(y/n)')
          if t=='n' or t=='N' :
               break
    print('#############  EXIT HOTEL MANAGEMENT SYSTEM   ##############')
    print('####################    THANK YOU    ######################')
    







































    
      
    

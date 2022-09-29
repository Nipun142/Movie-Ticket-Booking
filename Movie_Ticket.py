import pickle
import random
time=['#','10.00 - 12.30','14.30 - 16.00','18.00 - 20.30']
movie=['#','Movie 1','Movie 2','Movie 3','No moive']
combo=['#','combo 1','Combo 2','Combo 3','No combo']
p='No Data'
q='No movie'
s=['a0','a1','a2','a3','a4','a5']
a=['A ','A ','A ','A ','A ','A ']

def go_back():
    pip='wrong'
    while pip not in ['Y','N']:
        pip=input('Would you like to go back to previous page(Y/N): ').upper()
        if pip=='Y':
            pip='Y'
            return True
        elif pip=='N':
            pip='N'
            return False

def seat_refresh():
    f=open('seatpage.dat','wb')
    s=['a0','a1','a2','a3','a4','a5']
    a=['A ','A ','A ','A ','A ','A ']
    pickle.dump(s,f)
    pickle.dump(a,f)
    seat_refresh()
    
    
#name,phone,email,age
def login_page():
    def data_check(data):
        return data==''
    
    name=input('Enter your name: ')
    phone=input('Enter your number: ')
    email=input('Enter your Email: ')
    age=input('Enter your age: ')
    if data_check(name):
        name=p
    if data_check(phone):
        phone=p
    if data_check(email):
        email=p
    if data_check(age):
        age=p
    return name,phone,email,age



            
def movie_page(time,movie):
    #Time slots
    for i in range(1,5):
        print(i,': '+movie[i])
    n=0
    now=False
    while n not in range(1,5) or now==False:
        n = int(input('Select your Movie: '))
        for i in range(1,5):
            if n==i:
                M=movie[i]
                uwu=False
                if n in range(1,4):
                    t=0
                    while t not in range(1,4):
                        for u in range(1,4):
                            print(u,': '+time[u])
                        t=int(input('Select your Time slot: '))
                        for q in range(1,4):
                            if t==q:
                                T=time[q]
                                break
                else:
                    T=p
            now=True
    return M,T
#C
def combo_page(combo):
    wow=False
    while wow==False:
        for t in range(1,5):
            print(t, ': '+ combo[t])
        x = int(input('Choose your combo: '))
        interval= ' will arrive at Interval'
        beginning= ' will arrive at Beginning'
        for i in range(1,5):
            if x==i:
                C=combo[i]
                if i in range(1,4):
                    while i not in ['Y','N']:
                        s=input('Y for combo at interval or N for combo at beginning: ').upper()
                        if s=='Y':
                            print(f'Your Combo {interval}')
                            break
                        elif s=='N':
                            print(f'Your Combo{beginning}')
                            break  
                wow=True
    return C
        
#billing_page
def billing_page(name,phone,email,age,M,T,C,seat):
    print('Here is your Bill')
  # 1 out of 10 customer wins an offer
    def offer():
        off=random.randint(1,10)
        if off==1:
            print('Congratulations! you got a free booking!')
            return True
        else:
            return False
    
    
    def bill_money(M,C):
        bill=0    
        if M==movie[1] or M==movie[2] or M==movie[3]:
            bill+=200
        if C==combo[1] or C==combo[2] or C==combo[3]:
            bill+=100
        return bill
    bill=bill_money(M,C)
    f=open('User_bill.dat','wb')
    pickle.dump(name,f)
    pickle.dump(phone,f)
    pickle.dump(email,f)
    pickle.dump(age,f)
    pickle.dump(M,f)
    pickle.dump(T,f)
    pickle.dump(C,f)
    pickle.dump(seat,f)
    f=open('user_bill.dat','rb')

    print('Name- '+pickle.load(f))
    print('Phone number- '+pickle.load(f))
    print('Email ID- '+pickle.load(f))
    print('Age- '+pickle.load(f))
    print('Movie- '+pickle.load(f))
    print('Time slot- '+pickle.load(f))
    print('Combo- '+pickle.load(f))
    print('Seat selected- '+pickle.load(f))
    if offer():
        print('You Have to pay an amount of Rs 0')
    else:
         print(f'You Have to pay an amount of Rs {bill}')
    z=open('User_info.dat','ab')
    user_info=[]
    user_info.append(name)
    user_info.append(phone)
    user_info.append(email)
    user_info.append(age)
    user_info.append(M)
    user_info.append(T)
    user_info.append(C)
    user_info.append(seat)
    pickle.dump(user_info,z)
    
    


def seat_page():
    def display():
        print('Available seats are')
        f=open('seatpage.dat','rb')
        my=pickle.load(f)
        you=pickle.load(f)
        for i in range(0,6):
            if you[i]=='A ':
                print(my[i])
            else:
                pass
        
        
        
    def seat_check(a,u):
        return a[u]=='B'
        #returns True if seat is already booked


    def full_seat_check(a):
        b=0
        for i in range(len(a)):
            if seat_check(a,i):
                b+=1
        if b==len(a):
            return True
        #Returns True if all the seats are booked 
        #Housefull


    def seat_booked(s,a,u):
        f=open('seatpage.dat','wb')
        a[u]='B'
        pickle.dump(s,f)
        pickle.dump(a,f)
        print('Your seat has been booked')


    def seat_refresh():
        f=open('seatpage.dat','wb')
        s=['a0','a1','a2','a3','a4','a5']
        a=['A ','A ','A ','A ','A ','A ']
        pickle.dump(s,f)
        pickle.dump(a,f)
        seat_refresh()


    f=open('seatpage.dat','rb')
    s=pickle.load(f)
    a=pickle.load(f)
    display()
    z='seat is already booked'
    pop=True
    while pop==True:
        if full_seat_check(a):
            print('Sorry but all the seats are booked!')
            pop=False
            seat='No seat Selected'
        else:
            u=int(input('Select your seat: '))
            for i in range(0,6):
                if u==i:
                    if seat_check(a,u):
                        print(z)
                        display()
                        pop=True
                    else:
                        seat_booked(s,a,u)
                        pop=False
                        seat=s[u]

    return seat
#Main_menu
def main_page():
    zap=False
    while not zap:
        print('1 : Login page''\n'
                '2 : Exit '  )
        u=int(input('Enter: '))
        if u==1:
            rap1=False
            while not rap1:
                name,phone,email,age=login_page()
                if not go_back():
                    rap1=True
                    rap2=False
                    while not rap2:
                        M,T=movie_page(time,movie)
                        if M==movie[4]:
                            zap=True
                            rap2=True
                            print('Thankyou for visiting!')
                        else:
                            if not go_back():
                                rap2=True
                                rap3=False
                                while not rap3:
                                    C=combo_page(combo)
                                    if not go_back():
                                        rap3=True
                                        seat=seat_page()
                                        if seat=='No seat Selected':
                                            zap=True
                                            print('Thankyou for visiting!')
                                        else:
                                            billing_page(name,phone,email,age,M,T,C,seat)
                                            choice=input('Would you like to exit (Y/N): ').upper()
                                            if choice=='Y':
                                                zap=True
                                                print('Thankyou for visiting!')
                                            else:
                                                zap=False

                                    else:
                                        rap3=False
                            else:
                                rap2=False

                else:
                    rap1=False


        elif u==2:
            print('Thankyou for visiting!')
            zap=True
        else:
            print('Error!')
            zap=False


main_page()

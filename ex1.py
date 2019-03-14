secretcode=5555
balance= 1000

def code_check(code):

    global secretcode
    if code==secretcode:
        return  True
    else:
         return  False

def cash_withrawal():
    print("Enter 0 for getting 20 dollar\n"
          "Enter 1 for getting 50 dollar\n"
          "Enter 2 for getting different amount of money\n")
    money=input()
    if money=='0':
            attraction(20)

    if money=='1':
            attraction(50)

    if money=='2':
            attraction(20)


def attraction(amount):
    global balance
    balance-=amount


def code_change():
    global secretcode
    new=int(input("\nEnter the new code\n"))
    secretcode=new

thecode= input("enter the secret code\n")
while int(thecode)==secretcode:
   print("\nEnter 1 for current balance"
         "\nEnter 2 for cash withrawal"
         "\nEnter 3 for changing the secret code"
         "\nEnter 0 for exit")
   case=input()

   if case=='1':
      print(balance)
   elif case=='2':
      cash_withrawal()
   elif case=='3':
       code_change()
   elif case=='0':
       break
   thecode = input("enter the secret code\n")
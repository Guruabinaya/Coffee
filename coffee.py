print("*"*75)
print("\t\t\tWELCOME TO COFFEE WORLD")
print("*"*75)
Name=input("Enter your name:")
class coffee:
    def normal():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75) 
        if b==1:
            print("Rs.",a*30)
            print("-"*75)
            return a*30
        elif b==2:
            print("Rs.",a*60)
            print("-"*75)
            return a*60
        elif b==3:
            print("Rs.",a*90)
            print("-"*75)
            return a*90
        else:
            print("Not Available")     
    def short():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75)
        if b==1:
            print("Rs.",a*40)
            print("-"*75)
            return a*40
        elif b==2:
            print("Rs.",a*70)
            print("-"*75)
            return a*70
        elif b==3:
            print("Rs.",a*100)
            print("-"*75)
            return a*100
        else:
            print("Not Available")
    def doppio():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75)
        if b==1:
            print("Rs.",a*50)
            print("-"*75)
            return a*50
        elif b==2:
            print("Rs.",a*80)
            print("-"*75)
            return a*80
        elif b==3:
            print("Rs.",a*100)
            print("-"*75)
            return a*100
        else:
            print("Not Available")
    def capp():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75)
        if b==1:
            print("Rs.",a*60)
            print("-"*75)
            return a*60
        elif b==2:
            print("Rs.",a*90)
            print("-"*75)
            return a*90
        elif b==3:
            print("Rs.",a*120)
            print("-"*75)
            return a*120
        else:
            print("Not Available")
    def flat():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75)
        if b==1:
            print("Rs.",a*70)
            print("-"*75)
            return a*70
        elif b==2:
            print("Rs.",a*100)
            print("-"*75)
            return a*100
        elif b==3:
            print("Rs.",a*130)
            print("-"*75)
            return a*130
        else:
            print("Not Available")
    def mocha():
        a=int(input("How many coffee do u want? "))
        print("-"*75)
        b=int(input("Enter your cup size:\n1:50ml\n2:70ml\n3:100ml\n"))
        print("-"*75)
        if b==1:
            print("Rs.",a*80)
            print("-"*75)
            return a*80
        elif b==2:
            print("Rs.",a*110)
            print("-"*75)
            return a*110
        elif b==3:
            print("Rs.",a*140)
            print("-"*75)
            return a*140
        else:
            print("Not Available")
co=coffee
choice=1
while choice!=0:
  print("1.Normal Coffee")
  print("2.Short Block")
  print("3.Doppio")
  print("4.Cappuccino")
  print("5.Flat White")
  print("6.Mocha")
  print("7.Exiting")
  print("-"*75)
  choice=int(input("Enter your choice:"))
  print("-"*75)
  if choice==1:
      print("The Total Cost Is Rs.",co.normal())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==2:
      print("The Total Cost Is Rs.",co.short())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==3:
      print("The Total Cost Is Rs.",co.doppio())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==4:
      print("The Total Cost Is Rs.",co.capp())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==5:
      print("The Total Cost Is Rs.",co.flat())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==6:
      print("The Total Cost Is Rs.",co.mocha())
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
  elif choice==7:
      print("Exiting")
      break
  else:
      print("No Results Found")
      print("-"*75)
      key=input("Enter any key to continue")
      print("-"*75)
print("*"*75)    
print("please select your payment method:")
print("*"*75)
print("1.Debitcard")
print("2.GPay")
print("3.Phonepe")
print("4.Exiting")
print("-"*75)
payment=int(input("Enter your payment method:"))
print("-"*75)
if payment==1:
  print("please Enter your PIN number")
  PIN=int(input("Enter your 4 digit PIN no:"))
  str(PIN)
  len(str(PIN))
  while len(str(PIN))!=4:
      print("unavailable,please check the digit")
      dig=int(input("Enter the correct value:"))
      str(dig)
      len(str(dig))
      if len(str(dig))==4:
          print("It is correct value")
          break
      else:
          print("It is wrong value")
  else:
      print("ok,your pin is accepted")
  print("payment successfull")
  print("please keep the correct size on the filling area")
  fill=input("fill or cancel:")
  if fill=="fill":
     i=0
     while i<100:
       i=i+1
       print("[][][][][][][][][][][][][][][][][][][][][][]",i,"%")
  else:
       print("The Money Is Refunded")
elif payment==2:
  print("please Enter your GPay number")
  PIN=int(input("Enter your 10 digit MOB no:"))
  str(PIN)
  len(str(PIN))
  while len(str(PIN))!=10:
      print("unavailable,please check the digit")
      dig=int(input("Enter the correct value:"))
      str(dig)
      len(str(dig))
      if len(str(dig))==10:
          print("It is correct value")
          break
      else:
          print("It is wrong value")
  else:
      print("ok,your pin is accepted")
  print("payment successfull")
  print("please keep the correct size on the filling area")
  fill=input("fill or cancel:")
  if fill=="fill":
     i=0
     while i<100:
       i=i+1
       print("[][][][][][][][][][][][][][][][][][][][][][]",i,"%")
  else:
       print("The Money Is Refunded")       
elif payment==3:
  print("please Enter your Phonepe number")
  PIN=int(input("Enter your 10 digit MOB no:"))
  str(PIN)
  len(str(PIN))
  while len(str(PIN))!=10:
      print("unavailable,please check the digit")
      dig=int(input("Enter the correct value:"))
      str(dig)
      len(str(dig))
      if len(str(dig))==10:
          print("It is correct value")
          break
      else:
          print("It is wrong value")
  else:
      print("ok,your pin is accepted")
  print("payment successfull")
  print("please keep the correct size on the filling area")
  fill=input("fill or cancel:")
  if fill=="fill":
     i=0
     while i<100:
       i=i+1
       print("[][][][][][][][][][][][][][][][][][][][][][]",i,"%")
  else:
       print("The Money Is Refunded")
elif payment==4:
  print("Exiting")
else:
  print("please select another responce")
print("*"*75)      
print("THANKYOU,VISITAGAIN",Name)
print("*"*75)
print("For the further feedback please contact on Email:coffeeworld@gmail.com")    
print("*"*75)      
      
      



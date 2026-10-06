userID = "aman"
userPASS = "aman123"
acc_bal = 1000

print("selet option")
print("1: signup")
print("2: signin")

user_sign = input("Enter your option :")
if user_sign == "1" :
     new_user = input("Enter your username : ")
     new_pass = input("Enter your password : ")
     print("your userid id is :",new_user, "and your password is", new_pass)

elif user_sign == "2":
     user = input("Enter your userID :")
     password = input("Enter your password :")
     if userID == userID and userPASS == userPASS:
         print("selet your option")
         print("1: Check Balance")
         print("2: Do you Transition")
         print("3: Applying for loan")
         print("4: signout")
         user_input = input("Enter your option")

         if user_input == "1":
             print("your current balance is :", acc_bal)

         elif user_input == "2":
             print("Enter your option")
             print("1: Debit")
             print("2: credit")
             deb_cre = input("Enter your option")

             if deb_cre == "1":
                 debit_amount = int(input("Enter your amount"))
                 if debit_amount <= acc_bal:
                     current_bal = acc_bal - debit_amount
                     print("After debited your account balance is :", current_bal)

                 
               

         
         
     

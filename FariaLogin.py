import sys
import random
import time
import math
import csv
import time, sys
score=0
def slow_print(s):
  for c in s:
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()
    time.sleep(0.03)
newaccounts=True
loggedIn=False
yn=True




def loginsys():
  doublecheck=True
  while doublecheck == True:
    verifyRegister = input ("Welcome | Are you a registered user?\n[Y/N]: ")
    print (" ")
    if verifyRegister == "n" or verifyRegister == "N":  #If the user is not already registered
      if newaccounts == True:
        loop=True
        while loop == True:
            username = input ("Please enter a username\n[User]: ")
            print (" ")#Prompts for username
            checkusername = input ("Please retype your username\n[Verify]: ")
            print (" ")#Prompts to verify username
            if checkusername != username:
              print ("Invalid, please try again")
              loop=True
            else:
              loop=False       
              time.sleep(0.5)
              passloop=True
              while passloop == True:
                      password = input ("Please enter a password\n[Password]: ")
                      print (" ")#Prompts for password
                      checkpassword = input ("Please retype your password\n[Verify]: ")
                      print (" ")#Prompts to verify password
                      if checkpassword != password:
                        print ("Invalid, please try again")
                        print (" ")
                        passloop=True
                      else:
                        passloop=False
                        file = open("C_AccountData.txt","a") #Opens the file C_AccountData.txt in write mode/opens connection
                        file.write("USRN:") #Prefix Username to make the file easier to read
                        file.write(username) #Writes the username 
                        file.write("|") #Partition for visual ease to make the file easier to read
                        file.write("PSWD:") #Prefix Password to make the file easier to read
                        file.write(password)#Writes the password
                        file.write("\n") #New line to make the file easier to read
                        file.close() #Closes file/ends connection
                        print ("Your account has been created.") #Verifies that the account has been made to the user
                        time.sleep(2)
                        print ("\n")
                        doublecheck=True


    if verifyRegister == "Y" or verifyRegister == "y":
      loop=True
      if loop == True:
          user = input("[User]: ")
          passw = input("[Password]: ")
          f = open("C_AccountData.txt", "r")
          for line in f.readlines():
            uspwd = line.split("|")
            us = uspwd[0]
            pw = uspwd[1]
            if (user in us) and (passw in pw):
              loop=False
              print("Login successful, welcome",user)
              doublecheck=False
          else:
            if loop == True:
                  print ("\n")
                  print ("Sorry, your account details were not recognised. ")


    else:
      if verifyRegister != "Y" or verifyRegister != "y" or verifyRegister != "N" or verifyRegister != "n" or verifyRegister !="backup":
        print("\n")
        doublecheck=True

loginsys()

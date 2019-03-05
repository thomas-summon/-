#!/usr/local/bin/python

import shelve as s
import os, sys, time
import pyperclip as p

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: \npython3 vaultBytes.py [vault name] [account]\n\nThe defaut vault file is in the same folder of vaultBytes.py, called 'repositoryBytes', please don't change the name, unless you want to use the custom location as the following guide.\n\nIf you want to use your own file, please input the direction like this:\n\npython3 vaultBytes.py [vault name] [account] [file_location]\n")
    sys.exit()
elif len(sys.argv) == 3:
    theSecretFile = os.path.join(sys.path[0], "repositoryBytes")
else:
    theSecretFile = sys.argv[3]
    
if os.path.exists(theSecretFile) == False:
    print(r"It seems that there's no vault file yet. Would you like to creat one?(y|n)")
    if input().lower() != 'y' and input().lower() != 'yes':
        sys.exit()
    
vaults = s.open(theSecretFile)
vaultName = sys.argv[1]
account = sys.argv[2]

if vaultName in list(vaults.keys()):
    if account in vaults[vaultName].keys():
        print(r"The PASSWORD has been copied.")
        p.copy(vaults[vaultName][account])
        sys.exit()

    else:
        print(r"It seems that there is no ACCOUNT you want. Would you like to creat a new one?(y|n)")
        
        if input().lower() == 'y' or input().lower() == 'yes':
            newPassword = input("Please input the PASSWORD: ")
            vaultNameDic = vaults[vaultName]
            vaultNameDic[account] = newPassword
            vaults[vaultName] = vaultNameDic
            print(r"Your new ACCOUNT has been created.")

else:
    print(r"The VAULT you want to visit doesn't exist. Do you want to creat a new one?(y|n)")
   
    if input().lower() == 'y' or input().lower() == 'yes':
        vaults[vaultName] = {"initTime":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
        print(r"Your new VAULT has been created.")

vaults.close()
sys.exit()


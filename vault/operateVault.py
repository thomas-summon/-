#!/usr/local/bin/python

import sys, time
import messagesPrint
import pyperclip as p

def operateVault(vaults, vaultName, account):
    if vaultName in list(vaults.keys()):
        if account in vaults[vaultName].keys():
            p.copy(vaults[vaultName][account])
            print(r"The PASSWORD has been copied.")

        else:
            print(messagesPrint.creatNewAccount)
            
            if input().lower() == 'y' or input().lower() == 'yes':
                newPassword = input("Please input the PASSWORD: ")
                vaultNameDic = vaults[vaultName]
                vaultNameDic[account] = newPassword
                vaults[vaultName] = vaultNameDic
                print(r"Your new ACCOUNT has been created.")

    else:
        print(messagesPrint.creatNewVault)
        
        if input().lower() == 'y' or input().lower() == 'yes':
            vaults[vaultName] = {"initTime":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
            print(r"Your new VAULT has been created.")
            
if __name__ == '__main__':
    sys.exit()
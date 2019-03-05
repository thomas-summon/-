#!/usr/local/bin/python


# A simple Password manager to help manage your passwords.
# Rely on pyperclip, please conform these modules
# have been installed before use.


import os, sys
import shelve as s
import messagesPrint
import pyperclip as p
from operateVault import operateVault

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print(messagesPrint.info)
    sys.exit()
elif len(sys.argv) == 3:
    theSecretFile = os.path.join(sys.path[0], "repositoryBytes")
else:
    theSecretFile = sys.argv[3]
    
if os.path.exists(theSecretFile) == False:
    print(messagesPrint.creatNewVaultFile)
    if input().lower() != 'y' and input().lower() != 'yes':
        sys.exit()
    
vaults = s.open(theSecretFile)
vaultName = sys.argv[1]
account = sys.argv[2]
operateVault(vaults, vaultName, account)
vaults.close()
sys.exit()


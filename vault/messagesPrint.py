#!/usr/local/bin/python3

info = "Usage: \npython3 vaultBytes.py [vault name] [account]\n\nThe defaut vault file is in the same folder of vaultBytes.py, called 'repositoryBytes', please don't change the name, unless you want to use the custom location as the following guide.\n\nIf you want to use your own file, please input the direction like this:\n\npython3 vaultBytes.py [vault name] [account] [file_location]\n"

creatNewVaultFile = r"It seems that there's no VAULT file yet. Would you like to creat one?(y|n)"
creatNewAccount = r"It seems that there is no ACCOUNT you want. Would you like to creat a new one?(y|n)"
creatNewVault = r"The VAULT you want to visit doesn't exist. Do you want to creat a new one?(y|n)"
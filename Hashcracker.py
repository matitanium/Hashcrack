#import library
import hashlib
import sys
import os
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
from platform import platform
#banner design
def baner():
    plat = platform()
    if "Windows" in plat:
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.LIGHTRED_EX+ """
    coded by  : matin nouriyan
    ███╗   ███╗ █████╗ ████████╗██╗████████╗ █████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██║██║   ██║████╗ ████║
    ██╔████╔██║███████║   ██║   ██║   ██║   ███████║██╔██╗ ██║██║██║   ██║██╔████╔██║
    ██║╚██╔╝██║██╔══██║   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝                                                              
                                                                                    """)

    print(Fore.MAGENTA + "Select Your Hash Type: ")
    print(Fore.GREEN + """
    md5    = 1
    sha1   = 2
    sha224 = 3
    sha256 = 4
    sha384 = 5
    sha512 = 6
    +++ Other Hashes Unsuported +++
    If I succeeded Crack Your Hash Tell You In the last line
    """)



# call banner
baner()

#try to get hash type 
try:
    hashtype = int(input(Fore.CYAN  + "Enter Your HashType -- (example 1 / 2 / 3) : ")) 
    while hashtype >= 7:
        print(Fore.RED + "Just Select 1-6 . !!! Try Again :)) ")
        hashtype = int(input(Fore.CYAN  + "Enter Your HashType -- (example 1 / 2 / 3) : "))    
except:
    print(Fore.RED + "Just Select 1-6 . !!! Bye :) ")
    sys.exit()

#get hash
hash = input(Fore.LIGHTMAGENTA_EX+ "Enter Your Hash: ... ")


passlist = input(Fore.LIGHTGREEN_EX + "Enter Your WordList Addres : Example D:\password.txt:... ")
try:
    file = open(passlist,"r").readlines()
except:
    print(Fore.RED+ "i Cant find this wordlist... :{{ ")
    sys.exit()










#cracking hash by wordlist!!! code by matin nouriyan

if hashtype == 1:
    for i in file:
        i = i.strip()
        md5 = hashlib.md5()
        md5.update(i.encode())
        End = md5.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
elif hashtype == 2:
    for i in file:
        i = i.strip()
        sha_1 = hashlib.sha1()
        sha_1.update(i.encode())
        End = sha_1.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
elif hashtype == 3:
    for i in file:
        i = i.strip()
        sha_224 = hashlib.sha224()
        sha_224.update(i.encode())
        End = sha_224.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
elif hashtype == 4:
    for i in file:
        i = i.strip()
        sha_256 = hashlib.sha256()
        sha_256.update(i.encode())
        End = sha_256.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
elif hashtype == 5:
    for i in file:
        i = i.strip()
        sha_384 = hashlib.sha384()
        sha_384.update(i.encode())
        End = sha_384.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
elif hashtype == 6:
    for i in file:
        i = i.strip()
        sha_512 = hashlib.sha512()
        sha_512.update(i.encode())
        End = sha_512.hexdigest()
        print(Fore.LIGHTCYAN_EX +  "checking {u} hash... ++ ".format(u=i))
        if End == hash:
            print(Fore.GREEN + "your hash has been cracked... :)) password is : {a}".format(a=i))
            break
   
print(Fore.LIGHTRED_EX + "Good loock :) see you later :} ")
print( Fore.WHITE +  " ")
#end



#for test owner
# Enter Your Hash: ... 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
# Enter Your WordList Addres : Example D:\password.txt:... D:\matin\my code\python\encrypt\a.txt

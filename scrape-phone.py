
import urllib.request as req
from bs4 import BeautifulSoup as soup
import re
import pyperclip
from time import sleep
from termcolor import colored


def pyper():
    print(colored("\t\tExtracting Email and Numbers : ","yellow"))
    sleep(1)
    emails = re.findall(r'[\w.-]+@[\w-]+[.][\w]+', pyperclip.paste())
    #phones=re.findall(r"\+\d{3}\s?0?\d{6,10})

    phones = re.findall(r"^\+?\d{0,3}\s?[.-]?\(?\d{0,10}?\)?[-.\s]?\d{0,10}?$", pyperclip.paste())


    print(colored("\t==========================","yellow"))
    print("\t\tEmail addresses:")
    print(colored("\t==========================","yellow"))
    with open('email.txt', 'w+') as f:
        for email in emails:
            f.write(email+"\n")
            print(colored("\tEmail :%s"%email,"green"))


    print(colored("\t==========================","yellow"))
    print("\t\tphone numberes:")
    print(colored("\t==========================","yellow"))
    with open('phone.txt', 'w+') as f:
        for phone in phones:
            f.write(phone+"\n")
            print(colored("\tphone  : %s"%phone,"green"))



def web():
	website=str(input("\tEnter the website to be scrapped"))
	while website=="":
		print(colored("\tPlease enter website url :","red"))
		website=str(input("\tEnter the website url :"))
	r=req.urlopen(website).read()
	soupp=soup(r,'lxml')



	emails = re.findall(r'[\w.-]+@[\w-]+[.][\w]+',str(soupp))
	phones = re.findall(r"^\+?\d{0,3}\s?[.-]?\(?\d{0,10}?\)?[-.\s]?\d{0,10}?$", str(soupp))
	print(colored("\t==========================","yellow"))
	print("\t\tEmail addresses:")
	print(colored("\t==========================","yellow"))
	with open('email.txt', 'w+') as f:
	    for email in emails:
	        f.write(email+"\n")
	        print(colored("\tEmail :%s"%email,"green"))


	print(colored("\t==========================","yellow"))
	print("\t\tphone numberes:")
	print(colored("\t==========================","yellow"))
	with open('phone.txt', 'w+') as f:
	    for phone in phones:
	        f.write(phone+"\n")
	        print(colored("\tphone  : %s"%phone,"green"))


def main():
	print(colored("================Menu===============","green"))
	print(colored("===================================", "blue"))
	print(colored("1.Scrap form clipboard\n2.Scrap from the website : ","yellow"))
	choice =int(input(colored("Your Choice : ","yellow")))
	if choice==1:
		pyper()
		main()
	elif choice==2:
		web()
		main()


	else:
		exit()
	



main()

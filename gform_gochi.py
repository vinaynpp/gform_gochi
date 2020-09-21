import os
import urllib.request
import webbrowser
import time
from bs4 import BeautifulSoup
from pip._vendor import requests

print("")
print("WELCOME")
print("")
time.sleep(1)

if not os.path.isdir("temp"):
    os.makedirs("temp")
    print("TEMP FOLDER CREATED")

url = input("COPY PASTE THE GOOGLE FORM URL OVER HERE AND PRESS ENTER \n")
print("")
useremail = str(input("ENTER YOUR EMAIL \n"))
print("")
password = str(input("YOUR PASSWORD PLEASE \n"))
print("")
print("TRYING TO LOGIN")


class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, features="html.parser").find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text


url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, useremail, password)

# print("DOWNLOADING THE FORM.......")
# response = urllib.request.urlopen(url)
# webContent = response.read()
# if not os.path.isdir("temp"):
#    os.makedirs("temp")
# with open('temp/form_source.html', 'wb') as fid:
#    fid.write(webContent)

# print("")
# print("SOURCE DOWNLOADED IN TEMP FOLDER")
# print("")

my_string = session.get(url)

print("")
print("SUCCESSFULLY LOGGED IN")
print("")

localdata = my_string.partition("FB_PUBLIC_LOAD_DATA")

focus = localdata[0]

times = focus.count('role="heading"')

gochi = focus.partition('role="heading"')
gochi = gochi[2].partition(">")
gochi = gochi[2].partition('</div>')
print("YOUR FORM TITLE IS")
print(gochi[0])
print("")

print("WHICH SEARCH ENGINE DO YOU USE?")
print("ENTER '0' FOR DUCK DUCK GO ")
print("OR ANY OTHER NUMBER FOR GOOGLE")
bchoice = int(input("BE QUICK \n"))

if bchoice == 0:
    print("SMORT!!! KEEP USING DUCKDUCKGO")
else:
    print("LEVEL UP DUDE AND START USING DUCK DUCK GO")
    time.sleep(3)
    print("")
    print("")
    print("ANYWAYS")

print("")
print("")
print("HERE ARE YOUR QUESTIONS......")
print("")
print("WAIT WAIT WAIT")
group = int(input("HOW MANY QUESTIONS DO YOU WANT IN ONE GROUP \n"))
print("")
print("")

time.sleep(2)

questiono = int(0)

while times > 1:
    gochi = gochi[2].partition('role="heading"')
    gochi = gochi[2].partition(">")
    gochi = gochi[2].partition('<')
    question = gochi[0]

    print(questiono)
    print(question)
    print("")

    query = question.replace(" ", "+")

    if bchoice == 0:
        openbrow = "https://duckduckgo.com/?q=" + query
    else:
        openbrow = "https://www.google.com/search?q=" + query

    if questiono % 5 == 0:
        reply = int(input("TYPE 0 AND PRESS ENTER FOR NEXT GROUP OF QUESTIONS \n"))
        if reply == 0:
            webbrowser.open(openbrow, new=2)
            questiono = questiono + 1

    else:
        webbrowser.open(openbrow, new=2)
        questiono = questiono + 1

    time.sleep(2)

    times = times - 1

print("  DONE !!!!!")
if bchoice != 0:
    print("BUT  IT'S STILL NOT LATE.... START USING DUCK DUCK GO AND START CARING ABOUT YOUR OWN PRIVACY")
time.sleep(1)
print("")
print("")
print("AND")
time.sleep(1)
print("AND")
time.sleep(1)
print("AND")
time.sleep(1)
print("HAVE SOME MANNERS AND SAY THANKS TO VINAY PANCHAL")
print("http://www.vinaypanchal.com/")
print("")
print("")
time.sleep(5)
print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@$y|=!<<!__:rT35$QQB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QPI!                    =iq#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BRx-                           .<G#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@D",                                 `LB@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#`                                     `vW#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#V|"                                          :G@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@u:`                                             i@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@Z*`                                                 _Q@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#!       `^                                            *@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@B^        *@Qz*`                                        .Q@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@Q`        .B@@@@@OY<(:                                   `B@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*         5@@@@@@@@@@@QPyccGdu! =Vci~' `:_-- .            0@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@!       `M@@@@@@@@@@@@@@@@@@@@@#$Q@@@@BMH@@@#Q#bc).      `#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@!       I@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@x       O@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#`       0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@r       M@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@_       8@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@)      '#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@v      ^@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@c      !@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@c     :#@@@@Qd3hPdQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B`     i@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@$     Q@@O)' `.,!<;*ud@@@@@@@@@@@@@@#Q03L~,.-:^T$@@u     Q@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@`   u@#yTGQ#@@@@@@@@##@@@@@@@@@@@@@8T>rTXIIIIjT^r#O    _@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@i   M@@@@@@@QDE$QB#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##R    v@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@c  )@@@@@BQB$PyV5gB@@@@@@@@@@@@@@@@@@@#Q06dOE#@@@$    D@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@6_~@@@@@BDd)!  !@##@@B@@@@@@@@#@@#8Ov=`.=M$@Q#@@Q   r@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@dPQ(@@@@@@#Q5~_<d#@B#@z@@@@@@@@m@dDQ#}'  =8$$@@@@9  *@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@}BRT@@@@@@@@@@@@@@@@@#c@@@@@@@@$a@@@@@B$$8#@@@@@@O`;g#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@y$Qu#@@@@@@@@@@@@@@@@H#@@@@@@@@@Q0@@@@@@@@@@@@@@@8=B#s@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@$l@}6@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@E|#K8@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@$T#iy@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@XOQI@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@0V@dY@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@xO}#@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@cq@VB@@@@@@@@@@@@@@Z#@@@@@@@@@@@@$R@@@@@@@@@@@@BVB}Q@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@$v$w@@@@@@@@@@@@@QO@#@@@@@@@@@@@Rx@@@@@@@@@@@@yBHZ@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#T)@@@@@@@@@@@@@@@@#B#gQ@@##PHM$@@@@@@@@@@@@@ik#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@w0@@@@@@@@@@@@@Q$#@#8$0Q#@#8QB#@@@@@@@@@@@mk@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@q!@@@@@@@B$r~~`` .`.rMw5V^__`` _!VH@@@@@@B)@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@*u@@@@@@ZD vQQOK9OR9DqDOd688Qgc_`c@@@@@#=Q@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@#<$@@@@@#BxB@8B8$$B@@@@#QQQB@@@QTB@@@@#~H@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@k8@@@@@@@@@@dD@@B8QQQQ#@@B#@@@@@@@@#}Q@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Zm#@@@@@@@@@#$gRQQQBBBB#@@@@@@@@@Qd@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#KO@@@@@@@@@@@g=_!^*8@@@@@@@@@#OQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#H$@@@@@@@@@@#OMMB@@@@@@@@@HO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@E^R@@@@@@@@@@@@@@@@@@#Bl_.#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P _x<}XdBBBBQB#@QWc~'` _0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@r                   `h@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@M^`           ``rVh#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@QhTwTx5PMZQQ@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

""")
print("")
print("")
print(""" THENKS""")
print("")
print("")
print("")
print("")

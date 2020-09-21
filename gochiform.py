import os
import webbrowser
import time

print("")
print("WELCOME")
print("")
time.sleep(1)

if not os.path.isdir("temp"):
    os.makedirs("temp")
    print("TEMP FOLDER CREATED")

print("")
print("RIGHT CLICK ON YOUR GOOGLE FORM WEBPAGE AND SELECT OPTION VIEW PAGE SOURCE")
print("NOW SCROLL DOWN TO END OF THAT RANDOM GIBBERISH YOU WILL SEE A NUMBER ON THE LEFT BOTTOM")
no_of_lines = int(input(" ENTER THAT NUMBER OVER HERE \n"))
print("NOW COPY PASTE ALL OF THAT GIBBERISH AND PRESS ENTER")

webContent = ""
lines = no_of_lines
for i in range(no_of_lines + 1):
    webContent += input() + "\n"

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
print("HERE ARE YOUR QUESTIONS......")
print("")
print("WAIT WAIT WAIT")
group = int(input("HOW MANY QUESTIONS DO YOU WANT IN ONE GROUP \n"))
print("")
print("")

time.sleep(2)
localdata = webContent.partition("FB_PUBLIC_LOAD_DATA")

focus = localdata[2]

times = focus.count('[["')
gochi = focus.partition(',"')
gochi = gochi[2].partition('",')
print("YOUR FORM TITLE IS")
print(gochi[0])
print("")

questiono = int(0)
while times > 1:
    questiono = questiono + 1
    gochi = gochi[2].partition(',"')
    gochi = gochi[2].partition('",')
    question = gochi[0]

    print(questiono)
    print(question)
    print("")

    query = question.replace(" ", "+")

    if bchoice == 0:
        openbrow = "https://duckduckgo.com/?q=" + query
    else:
        openbrow = "https://www.google.com/search?q=" + query

    if questiono % group == 0:
        reply = int(input("TYPE 0 AND PRESS ENTER FOR NEXT GROUP OF QUESTIONS \n"))
        if reply == 0:
            webbrowser.open(openbrow, new=2)
    else:
        webbrowser.open(openbrow, new=2)


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

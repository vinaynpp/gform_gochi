import os
import webbrowser
import time

print("")
print("WELCOME")
print("")
time.sleep(1)

with open("temp/form_source.html", "r") as myfile:
    webContent = myfile.read().replace('\n', '')

print("WHICH SEARCH ENGINE DO YOU USE?")
print("ENTER '0' FOR DUCK DUCK GO ")
print("OR ANY OTHER NUMBER FOR GOOGLE")
bchoice = int(0)

print("")
print("")
print("HERE ARE YOUR QUESTIONS......")
print("")
print("WAIT WAIT WAIT")
group = int(4)
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

questiono = int(1)

while times > 1:

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
    #
    #   if questiono % 4 == 0:
    #        reply = int(input("TYPE 0 AND PRESS ENTER FOR NEXT GROUP OF QUESTIONS \n"))
    #       if reply == 0:
    #           webbrowser.open(openbrow, new=2)
    #
    #
    #    else:
    #        webbrowser.open(openbrow, new=2)

    questiono = questiono + 1
    time.sleep(2)

    times = times - 1

print("  DONE !!!!!")

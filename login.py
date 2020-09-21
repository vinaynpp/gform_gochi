from bs4 import BeautifulSoup
from pip._vendor import requests


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
        print(my_dict)
        my_dict['Email'] = login

        print(my_dict)
        self.ses.post(url_login, data=my_dict)
        print(my_dict)

    def get(self, URL):
        return self.ses.get(URL).text


url_login = "https://docs.google.com/forms/d/e/1FAIpQLSewmNgy7Elr6sI8WZGNUd9cOudI9-e5Z3Nar7RWjtpyGf_EFw/formResponse"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "vinay.panchal@universal.edu.in", "India1947#")
print(session.get("https://docs.google.com/forms/d/e/1FAIpQLSewmNgy7Elr6sI8WZGNUd9cOudI9-e5Z3Nar7RWjtpyGf_EFw/formResponse"))

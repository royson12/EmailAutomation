from exchangelib import Credentials, Account, HTMLBody
import keyring
from bs4 import BeautifulSoup

credentials = Credentials("royson.oliver@igglobal.com",
                          keyring.get_password("email_credentials", "royson.oliver@igglobal.com"))
getaccount = Account("royson.oliver@igglobal.com",
                     credentials=credentials, autodiscover=True)

# for item in getaccount.inbox.all().order_by('-datetime_received')[:100]:
#    print(item.subject, item.sender, item.datetime_received)
# unread = account.inbox.filter(is_read=False)    #returns unread emails
# dog = account.inbox.filter(subject='My new dog!')   #returns email with subject of 'My new dog!'
# mike = account.inbox.filter(author='mike@hamburger.com')    #returns emails from your buddy Mike

for item in getaccount.inbox.filter(is_read=False):
    print(item.subject)
    print(item.sender)
    print(item.datetime_received)
    print(item.text_body)
    # print(item.body)
    #file = open(r"C:\Users\royson.oliver\Desktop\POC\Soup.txt", "w")
    #file.write(BeautifulSoup(item.body,"html.parser").prettify())
    # print(BeautifulSoup(item.body,"html.parser").prettify())
    break

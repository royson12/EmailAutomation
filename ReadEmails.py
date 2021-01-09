from pyews import UserConfiguration
from pyews import GetSearchableMailboxes
from pyews import SearchMailboxes

import keyring

userconfig = UserConfiguration(
    "royson.oliver@igglobal.com", "njvlbjxxzcpmwpsz",exchangeVersion='Office365',autodiscover=True)
# endpoint='https://outlook.office365.com/autodiscover/autodiscover.svc'

# get searchable mailboxes based on your accounts permissions
referenceid_list = []
for mailbox in GetSearchableMailboxes(userconfig).response:
    referenceid_list.append(mailbox['ReferenceId'])

# let's search all the referenceid_list items
count = 0
messages_found = []
for search in SearchMailboxes('subject:account', userconfig, referenceid_list).response:
    messages_found.append(search['MessageId'])
    # we can print the results first if we want
    print(search['Subject'])
    print(search['MessageId'])
    print(search['Sender'])
    print(search['ToRecipients'])
    print(search['CreatedTime'])
    print(search['ReceivedTime'])
    count += 1
    if count == 10:
        break
    # etc.

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

dev_token = "S=s1:U=93dec:E=165511c9460:C=15df96b67c0:P=1cd:A=en-devtoken:V=2:H=fd998b7332362120f0f87a88135f7b41"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()
# print user.username
# print user

#
# User(username='zhangolve', premiumInfo=None, updated=None,
# name=None, created=None, deleted=None, email=None, shardId='s1',
# active=True, accounting=Accounting(businessRole=None, currency=None,
# uploadLimitNextMonth=62914560, premiumOrderNumber=None, lastRequestedCharge=None,
# nextPaymentDue=None, unitDiscount=None, premiumCommerceService=None, nextChargeDate=None, premiumServiceStart=None,
#  premiumSubscriptionNumber=None, lastFailedCharge=None, updated=None, businessId=None, uploadLimitEnd=1505718000000,
#  uploadLimit=62914560, lastSuccessfulCharge=None, premiumServiceStatus=0, unitPrice=None, premiumServiceSKU=None, premiumLockUntil=None,
#  businessName=None, lastFailedChargeReason=None), attributes=None, privilege=1, timezone=None, businessUserInfo=None, id=605676)

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
# for n in notebooks:
#     print n

note = Types.Note()
note.title = "I'm a test note!"
note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note>Hello, world!</en-note>'
note = noteStore.createNote(note)



# Notebook
# Notebook(restrictions=NotebookRestrictions(noSetDefaultNotebook=None, noPublishToBusinessLibrary=True,
# noCreateTags=None, noUpdateNotes=None, expungeWhichSharedNotebookRestrictions=None, noExpungeTags=None,
# noSetNotebookStack=None, noCreateSharedNotebooks=None, noExpungeNotebook=None, noUpdateTags=None, noPublishToPublic=True,
# noUpdateNotebook=None, updateWhichSharedNotebookRestrictions=None, noSetParentTag=None, noCreateNotes=None, noEmailNotes=True,
# noReadNotes=None, noExpungeNotes=None, noShareNotes=None, noSendMessageToRecipients=None), name='\xe6\x88\x91\xe7\x9a\x84\xe7\xac\xac\xe4\xb8\x80\xe4\xb8\xaa\xe7\xac\x94\xe8\xae\xb0\xe6\x9c\xac', defaultNotebook=True, serviceUpdated=1500427744000, sharedNotebookIds=None,
# businessNotebook=None, contact=None, sharedNotebooks=None, updateSequenceNum=1, published=None, serviceCreated=1500427744000, guid='1d1852cb-f7d3-4905-8d6a-e5b7132217cc', stack=None, publishing=None)
# Notebook(restrictions=NotebookRestrictions(noSetDefaultNotebook=None, noPublishToBusinessLibrary=True,\
#  noCreateTags=None, noUpdateNotes=None, expungeWhichSharedNotebookRestrictions=None, noExpungeTags=None,
# noSetNotebookStack=None, noCreateSharedNotebooks=None, noExpungeNotebook=None, noUpdateTags=None, noPublishToPublic=True,
#  noUpdateNotebook=None, updateWhichSharedNotebookRestrictions=None, noSetParentTag=None, noCreateNotes=None, noEmailNotes=True,
# noReadNotes=None, noExpungeNotes=None, noShareNotes=None, noSendMessageToRecipients=None), name='give a test', defaultNotebook=False,
# serviceUpdated=1503128636000, sharedNotebookIds=None, businessNotebook=None, contact=None, sharedNotebooks=None, updateSequenceNum=5,
# published=None, serviceCreated=1503128636000, guid='8e06c2b3-14fb-42bf-8c8c-a1261257666b', stack=None, publishing=None)

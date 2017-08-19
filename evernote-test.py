# -*- coding: UTF-8 -*-

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import time


dev_token = "S=s1:U=93dec:E=16551700c9b:C=15df9bedef0:P=1cd:A=en-devtoken:V=2:H=b0d21307fb2371db1601776b3aa34642"
client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
user = userStore.getUser()


noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()

note = noteStore.getNote('db874106-0bf7-455d-9472-702aa71d45cb', True, False, False, False)
print('note', note)
st = time.localtime(note.created/1000.0)
print(time.strftime('%Y-%m-%d %H:%M:%S', st))
#  根据一条笔记的guid来找到对应的笔记
# 2017-08-19 17:17:52
#('note', Note(contentHash='_R\xd7\xef\xb4\x98W\xd4\xd7\x82\xfc\x1d}P\xd9\x0f', updated=1503134272000,
# created=1503134272000, deleted=None, contentLength=135, title='\xe4\xbd\xa0\xe5\xa5\xbd \xe8\xbf\x99\xe6\x98\xaf\xe4\xb8\xaa\xe6\xb5\x8b\xe8\xaf\x95,\xe6\xac\xa2\xe8\xbf\x8e\xe4\xbd\xa0!', notebookGuid='1d1852cb-f7d3-4905-8d6a-e5b7132217cc', content='<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note>Hello, world!</en-note>', tagNames=None, updateSequenceNum=9, tagGuids=None, active=True, attributes=NoteAttributes(lastEditorId=None, placeName=None, sourceURL=None, classifications=None, creatorId=None, author=None, reminderTime=None, altitude=None, reminderOrder=None, shareDate=None, reminderDoneTime=None, longitude=None, lastEditedBy=None, source=None, applicationData=None, sourceApplication=None, latitude=None, contentClass=None, subjectDate=None), guid='db874106-0bf7-455d-9472-702aa71d45cb', resources=None))





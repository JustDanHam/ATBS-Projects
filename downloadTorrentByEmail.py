#! python3
# downloadTorrentByEmail.py - checks for emails containing
# torrent magnet links, and downloads files automatically.
# Requires textMyself.py to be in the cwd.

import imapclient
import pyzmail
import subprocess
import textMyself


email = 'yourEmail'
password = 'yourPassword'
imapAddress = 'yourImapAddress'
torrentClient = 'filepathToTorrentClient'

# Add torrentClient as first element of magnetLinks
magnetLinks = []
magnetLinks.append(torrentClient)

# Only uses emails with subjectKey in subject, for added security
subjectKey = 'qBit95'

# Connect to the email server
imapObj = imapclient.IMAPClient(imapAddress, ssl=True)
imapObj.login(email, password)

# Select the inbox folder
imapObj.select_folder('INBOX', readonly=False)

# Fetch all emails with subjectKey as subject
UIDs = imapObj.search(['SUBJECT', f'{subjectKey}'])
for UID in UIDs:
    rawMessages = imapObj.fetch([UID], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])

    # Get magnet link from email and add to magnetLinks list
    magnetLink = message.text_part.get_payload().decode(message.text_part.charset)
    magnetLinks.append(magnetLink)

    # Delete email after link is extracted
    imapObj.delete_messages([UID])

# Disconnect from email server
imapObj.logout()

# Opens client and starts downloading files from all links provided
subprocess.run(magnetLinks)

# Send a text saying downloads are complete
textMyself.textMyself('All downloads have been completed.')

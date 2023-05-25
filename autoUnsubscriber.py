#! python3
# autoUnsubscriber.py - checks emails for unsubscribe links and opens
# a browser tab for each.

import imapclient
import pyzmail
import bs4
import webbrowser


def autoUnsub(email, password, imapDomName):
    # Connect to the email server
    imapObj = imapclient.IMAPClient(imapAddress, ssl=True)
    imapObj.login(email, password)

    # Select the inbox folder
    imapObj.select_folder('INBOX', readonly=True)

    # Fetch all the emails in the inbox
    UIDs = imapObj.search(['ALL'])
    for UID in UIDs:
        rawMessages = imapObj.fetch([UID], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])

        # If an email has an HTML body, parse it with bs4
        if message.html_part:
            html = message.html_part.get_payload().decode(message.html_part.charset)
            soup = bs4.BeautifulSoup(html, 'html.parser')

            # If 'unsubscribe' is in link text, open link in browser
            linkElems = soup.select('a')
            for linkElem in linkElems:
                if 'unsubscribe' in linkElem.text.lower():
                    link = linkElem.get('href')
                    webbrowser.open(link)

    imapObj.logout()


if __name__ == '__main__':

    email = input('Enter your email address: ')
    password = input('Enter your password: ')
    imapDomName = input("Enter your email's IMAP server domain name: ")

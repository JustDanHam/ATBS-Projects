#! python3
# randomChore.py - takes a list of people's email addresses and a list
# of chores and randomly assigns chores to people. Emails each person
# their assigned chores.

import random
import smtplib


emails = ['crazyhamsterboy@hotmail.com']


def choreAssign(emails):
    chores = ['dishes', 'bathroom', 'hoover', 'feed cat']

    # Loop through each email, picking a random chore for each.
    for email in emails:
        # check if chores list is empty before assigning chore
        if not chores:
            randomChore = 'There are not chores left. Lucky you!'
        else:
            randomChore = random.choice(chores)
            # this chore is now taken, so remove it
            chores.remove(randomChore)

        # Set up the SMTP server, in order to send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('alldhamnonedspam@gmail.com',
                      input('Enter email password'))

        # Send the email with chosen chore.
        msg = ('Subject: Your chosen chore\n\n'
              'Hi there!\n'
              'It\'s that time of the week again!\n'
              'Your chore this week is...\n'
              '\n'
              f'{randomChore}!'
              '... enjoy!')

        server.sendmail('alldhamnonedspam@gmail.com', email, msg)
        # Close the connection
        server.quit()

choreAssign(emails)

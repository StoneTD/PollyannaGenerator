# Dylan Stone, 2023

# Many details such as family, member names, and emails have been omitted to preserve privacy

from email.message import EmailMessage
import random
import smtplib
import ssl

emailSender = ''
emailPassword = ''
emailReciever = ''
giftReciever = ''

# availability, 0 means hasn't been picked yet
# final index in each list states how many family members have been chosen in that family
# once it reaches the number of family members that family is considered complete

fam1 = [0, 0, 0, 0, 00] # Sample family of 4
fam2 = [0, 0, 0, 0, 0, 00] # Sample family of 5
fam3 = [0, 0, 0, 00] # Sample family of 3
fam4 = [0, 0, 0, 0, 00]
fam5 = [0, 0, 0, 0, 00]

fam1Name = ['', '', '', '']
fam2Name = ['', '', '', '', '']
fam3Name = ['', '', '']
fam4Name = ['', '', '', '']
fam5Name = ['', '', '', '']

fam1Email = ['', '', '', '']
fam2Email = ['', '', '', '', '']
fam3Email = ['', '', '']
fam4Email = ['', '', '', '']
fam5Email = ['', '', '','']

availList = [fam1, fam2, fam3, fam4, fam5]
nameList = [fam1Name, fam2Name, fam3Name, fam4Name, fam5Name]
emailList = [fam1Email, fam2Email, fam3Email, fam4Email, fam5Email]
i = 0
j = 0

for x in availList:
    j = 0
    for y in x:
        if (j >= len(x) - 1):
            break

        # sets the person recieving the email
        emailReciever = emailList[i][j]

        # finds the family for the current member
        offset = random.randrange(1, 4, 1)

        # simulates wraparound searching
        if (i + offset >= len(availList)):
            ranFamIndex = (i + offset) - len(availList) + 1
        else:
            ranFamIndex = i + offset

        size = len(availList[ranFamIndex]) - 1

        # if we hit a family that is complete, go next
        while (availList[ranFamIndex][size] == size):
            ranFamIndex += 1

            # you cannot have your own family
            if (ranFamIndex == i):
                ranFamIndex += 1

            # wraparound
            if (ranFamIndex >= len(availList)):
                ranFamIndex = 0

            size = len(availList[ranFamIndex]) - 1

        ranMem = random.randrange(0, size - 1, 1)

        # has to be someone who hasn't been picked yet
        while (availList[ranFamIndex][ranMem] != 0):
            ranMem += 1

            # wraparound
            if (ranMem >= size):
                ranMem = 0

        # found a person, set availability and reciver variables
        availList[ranFamIndex][ranMem] = 1
        availList[ranFamIndex][size] += 1
        giftReciever = nameList[ranFamIndex][ranMem]

        # debugging
        # print('Email being sent to: ' + emailReciever)
        # print('Chosen Pollyanna is: ' + giftReciever)
        # print()

        # crafting the email
        subject = 'Your Pollyanna for this year'
        body = 'Your Pollyanna has been chosen to be: ' + giftReciever 

        em = EmailMessage()
        em['From'] = emailSender
        em['To'] = emailReciever
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        # sending the actual email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(emailSender, emailPassword)
                smtp.sendmail(emailSender, emailReciever, em.as_string())

        j += 1
    i += 1


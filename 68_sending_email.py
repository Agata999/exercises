import smtplib

mailFrom = 'Harry Potter'
mailTo = ['spamerka666@gmail.com']
mailSubject = 'Avada Kedavra'
mailBody = '''
AIN EINGARP ACRESO GEWTEL AZ RAWTA WTE IN MAJ IBDO,

You-know-who!'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = 'spamerka666@gmail.com'
password = 'qwer4321!'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')

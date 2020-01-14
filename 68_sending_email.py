import smtplib
import functools


def send_email(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = '''From: {}
    Subject: {}
    
    {}
    '''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False


mailFrom = 'Harry Potter'
mailTo = ['spamerka666@gmail.com']
mailSubject = 'Avada Kedavra'
mailBody = '''
AIN EINGARP ACRESO GEWTEL AZ RAWTA WTE IN MAJ IBDO,

You-know-who!'''
user = 'spamerka666@gmail.com'
password = 'qwer4321!'

send_email_from_gmail = functools.partial(send_email, user, password, mailSubject="Execution")
send_email_from_gmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody)

import smtplib
import datetime
from email.mime.multipart import MIMEMultipart


class Gmail:
    def __init__(self):
        return

    @staticmethod
    def send_email(body):
        try:
            # gmail account authentication
            gmail_user = 'tyfreechuang@gmail.com'
            gmail_password = 'isczuwwdkqqtpopw'

            # set email configuration
            msg = MIMEMultipart('alternative')
            msg.attach(body)
            msg['From'] = 'tyfreechuang@gmail.com'
            msg['To'] = 'tchuang-17099@email.esunbank.com.tw'
            now = datetime.datetime.now()
            msg['Subject'] = 'Stock Insights: '+ str(now.month) + '-' + str(now.day) + '-' + str(now.year) +

            # send mail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.close()

        except Exception as e:
            # print thrown error
            print(str(e))
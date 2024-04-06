import configparser
import smtplib
from email.mime.text import MIMEText


def send_email():
    # fetch config
    config = configparser.RawConfigParser()
    config.read("ConfigFile.properties")

    # set up email details
    from_address = config.get("EmailSection", "from.email.address")
    to_address = config.get("EmailSection", "to.email.address")
    login_name = from_address
    app_pass = config.get("EmailSection", "app.password")
    subject = "Hello, that's me"
    text = "I am a mad scientist"
    smtp_server = "smtp.gmail.com"

    # send email
    message = MIMEText(text)
    message["Subject"] = subject
    message["From"] = from_address
    message["To"] = to_address
    sender = smtplib.SMTP_SSL(smtp_server)
    sender.login(login_name, app_pass)
    sender.sendmail(from_address, to_address, message.as_string())
    sender.quit()


if __name__ == '__main__':
    send_email()

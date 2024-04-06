import configparser
import smtplib
from email.mime.text import MIMEText
import requests


def send_email():
    config = get_config()
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


def notify_line():
    config = get_config()

    message = "Hello, Line. How are you doing?"
    url = "https://notify-api.line.me/api/notify"
    token = config.get("LineSection", "access.token")
    headers = {"Authorization" : "Bearer " + token}
    param = {"message" : message}

    response = requests.post(url, headers=headers, params=param)
    print(response)


def get_config():
    # fetch config
    config = configparser.RawConfigParser()
    config.read("ConfigFile.properties")
    return config


if __name__ == '__main__':
    # send_email()
    notify_line()

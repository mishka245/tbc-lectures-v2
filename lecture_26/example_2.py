import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY') # SendGrid API key, correct way to get API key from environment variable


sg = SendGridAPIClient(SENDGRID_API_KEY)


def send_email(send_to: str = 'lomidzemikheili@gmail.com'):
    message = Mail(
        from_email='besomeskhia40k@gmail.com',
        to_emails=send_to,
        subject='Hello from TBC academy',
        html_content='სალამი <br> <br> <br><br><br><br><br>კეთილი სურვილებით, Python intro!')
    response = sg.send(message)
    if response.status_code != 202:
        print(response.status_code, response.text)
        raise Exception('Email was not sent')


def main():
    send_email()


if __name__ == "__main__":
    main()

import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 456

    username = "momomuimui060622@gmail.com"
    password = "ntvn bnci ssxx rbdq"

    receiver = "momomuimui060622@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()
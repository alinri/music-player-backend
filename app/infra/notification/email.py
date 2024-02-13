import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.models.settings import Settings

from .interface import INotificaiton


class EmailNotification(INotificaiton):
    def __init__(
        self,
        receiver: str,
        subject: str,
    ) -> None:
        settings = Settings()
        self._smtp_server = settings.SMTP_SERVER
        self._smtp_port = settings.SMTP_PORT
        self._smtp_sender = settings.SMTP_SENDER
        self._smpt_passowrd = settings.SMTP_PASSWORD
        self._receiver = receiver
        self._subject = subject

    def send_message(self, content: str):
        context = ssl.create_default_context()
        msg = MIMEMultipart("alternative")
        msg["Subject"] = self._subject
        msg["From"] = self._smtp_sender
        msg["To"] = self._receiver
        text = content
        html = """\
<html>
    <body>
    {}
    </body>
</html>
""".format(
            content
        )
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        msg.attach(part1)
        msg.attach(part2)
        with smtplib.SMTP_SSL(
            self._smtp_server,
            self._smtp_port,
            context=context,
        ) as smtp_server:
            smtp_server.login(
                self._smtp_sender,
                self._smpt_passowrd,
            )
            smtp_server.sendmail(
                self._smtp_sender,
                self._receiver,
                msg.as_string(),
            )

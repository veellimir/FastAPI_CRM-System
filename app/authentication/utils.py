import aiosmtplib
from email.message import EmailMessage

from settings.config import settings


async def send_email(email: str, token: str):
    link = f"http://localhost:8000/auth/login?token={token}"
    message = EmailMessage()
    message["From"] = settings.SMTP_USERNAME
    message["To"] = email
    message["Subject"] = "Вход в систему"
    message.set_content(f"Для входа нажмите на ссылку: {link}")

    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_SERVER,
        port=settings.SMTP_PORT,
        username=settings.SMTP_USERNAME,
        password=settings.SMTP_PASSWORD,
        start_tls=True,
    )

from email.mime.text import MIMEText
from aiosmtplib import SMTP

from core.settings import settings


async def send_email(to_email: str, link: str):
    """
    Верификация по почте
    :param to_email:
    :param link:
    :return: None
    """
    msg = MIMEText(f"Здравствуйте !\n\nДля подтверждения аккаунта перейдите по ссылке: {link}")
    msg["Subject"] = "Подтверждение или сброс пароля"
    msg["From"] = settings.SMTP_EMAIL_HOST_USER
    msg["To"] = to_email

    server = SMTP(
        hostname=settings.SMTP_EMAIL_HOST,
        port=settings.SMTP_EMAIL_PORT,
        use_tls=False  # важно!
    )
    await server.connect()

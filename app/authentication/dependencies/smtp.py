from email.mime.text import MIMEText
from aiosmtplib import SMTP

from core.settings import settings


async def send_email(to_email: str, link: str) -> None:
    html_content = f"""
    <html>
      <body style="margin: 0; padding: 0; background-color: #1E1E2F; font-family: Arial, sans-serif; color: #ffffff;">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 600px; margin: 40px auto; background-color: #2A2A3C; border-radius: 12px; padding: 32px;">
          <tr>
            <td align="center" style="padding-bottom: 24px;">
              <h2 style="color: #ffffff; font-size: 24px; margin: 0;">Добро пожаловать в CRM - System</h2>
            </td>
          </tr>
          <tr>
            <td style="font-size: 16px; line-height: 1.6; color: #dcdcdc; padding-bottom: 32px;">
              <p style="margin: 0;">Для подтверждения вашего аккаунта нажмите на кнопку ниже:</p>
            </td>
          </tr>
          <tr>
            <td align="center" style="padding-bottom: 32px;">
              {link}
            </td>
          </tr>
          <tr>
            <td style="font-size: 14px; color: #888888;">
              <p style="margin: 0;">Если вы не регистрировались, просто проигнорируйте это письмо.</p>
            </td>
          </tr>
        </table>
      </body>
    </html>
    """

    msg = MIMEText(html_content, "html")
    msg["Subject"] = "Подтверждение аккаунта"
    msg["From"] = settings.SMTP_EMAIL_HOST_USER
    msg["To"] = to_email

    server = SMTP(
        hostname=settings.SMTP_EMAIL_HOST,
        port=settings.SMTP_EMAIL_PORT,
        use_tls=False,
        start_tls=True
    )
    await server.connect()

    await server.login(settings.SMTP_EMAIL_HOST_USER, settings.SMTP_EMAIL_HOST_PASSWORD)
    await server.send_message(msg)

    await server.quit()

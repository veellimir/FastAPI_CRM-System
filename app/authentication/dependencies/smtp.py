from email.mime.text import MIMEText
from aiosmtplib import SMTP

from core.settings import settings


async def send_custom_email(
        to_email: str,
        subject: str,
        title: str,
        body_text: str,
        button_text: str,
        link: str,
        footer_note: str
) -> None:
    html_content = f"""
    <!DOCTYPE html>
    <html>
      <body style="margin:0; padding:0; background-color:#1E1E2F;">
        <center>
          <table width="100%" cellpadding="0" cellspacing="0" style="padding: 40px 0;">
            <tr>
              <td align="center">
                <table width="600" cellpadding="0" cellspacing="0" style="background-color:#2A2A3C; border-radius:12px; padding:32px; text-align:center; font-family:Arial, sans-serif;">
                  <tr>
                    <td style="color:#ffffff; font-size:24px; font-weight:bold; padding-bottom:24px;">
                      {title}
                    </td>
                  </tr>
                  <tr>
                    <td style="color:#dcdcdc; font-size:16px; padding-bottom:32px;">
                      {body_text}
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="padding-bottom:32px;">
                      <a href="{link}" target="_blank" style="
                        background-color: #FF5722;
                        color: white;
                        padding: 12px 24px;
                        text-decoration: none;
                        border-radius: 6px;
                        font-weight: bold;
                        display: inline-block;
                        font-size: 16px;
                      ">{button_text}</a>
                    </td>
                  </tr>
                  <tr>
                    <td style="color:#888888; font-size:14px;">
                      {footer_note}
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </center>
      </body>
    </html>
    """

    msg = MIMEText(html_content, "html")
    msg["Subject"] = subject
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

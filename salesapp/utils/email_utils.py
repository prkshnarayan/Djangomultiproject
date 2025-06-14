import logging
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

logger = logging.getLogger(__name__)


def send_welcome_email(student):
    try:
        subject = f"Welcome to Our Program, {student.name}!"
        html_content = render_to_string('emails/welcome_student.html', {'student': student})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject,
            text_content,
            None,  # Uses DEFAULT_FROM_EMAIL
            [student.email]
        )
        email.attach_alternative(html_content, "text/html")

        # Add logging before sending
        logger.info(f"Attempting to send email to {student.email}")
        email.send()
        logger.info(f"Email sent successfully to {student.email}")
        return True

    except Exception as e:
        logger.error(f"Failed to send email to {student.email}: {str(e)}")
        return False

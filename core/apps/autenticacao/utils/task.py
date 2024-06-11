from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True)
def send_email(self, data, template_name):
    try:
        message = render_to_string(template_name, data)
        email = EmailMessage(data['subject'], message, to=[data['user']])
        email.content_subtype = "html"
        email.send()
    except Exception as error:
        logger.error(error)

# import os
# from collections import namedtuple

# from django.core.mail import EmailMultiAlternatives, DEFAULT_ATTACHMENT_MIME_TYPE
# from django.conf import settings
# from django.template.loader import render_to_string
# from django.contrib.sites.models import Site

# Attachment = namedtuple('Attachment', 'name,content,content_type')

# def send_templated_email(template, context, to, from_email=settings.DEFAULT_FROM_EMAIL, subject=None, attachments=None):
#     template_base, _ext = os.path.splitext(template)
#     text_template = template_base + '.txt'
#     html_template = template_base + '.html'

#     if 'site' not in context:
#         context['site'] = Site.objects.get_current()

#     if isinstance(to, str):
#         to = [to]

#     text_content = render_to_string(text_template, context)
#     html_content = render_to_string(html_template, context)

#     msg = EmailMultiAlternatives(subject, text_content, from_email, to)
#     msg.attach_alternative(html_content, "text/html")

#     if attachments is not None:
#         for attachment in attachments:
#             if not attachment.content_type:
#                 content_type = DEFAULT_ATTACHMENT_MIME_TYPE
#             else:
#                 basetype, subtype = attachment.content_type.split('/', 1)
#                 content_type = attachment.content_type
#                 if basetype == 'text':
#                     content_type = DEFAULT_ATTACHMENT_MIME_TYPE
#             msg.attach(attachment.name, attachment.content, content_type)
#     msg.send()

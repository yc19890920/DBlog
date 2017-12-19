# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
import logging

from libs.tools import getSmtpAccout
from libs.email.send_email import MailSender

logger = logging.getLogger(__name__)

import time

@shared_task
def celery_send_email(subject, message, recipient_list, **kwrags):
    host, port, is_ssl, account, password = getSmtpAccout()
    # print '---------------', host, port, is_ssl, account, password
    try:
        # 使用celery并发处理邮件发送的任务
        s = MailSender()
        # time.sleep(10)
        s.send_email(host, port, account, password, recipient_list, subject, message, ssl=is_ssl)
        # send_mail(subject, message, from_email, recipient_list, **kwrags)
        return 'success!'
    except Exception as e:
        logger.error(u"邮件发送失败: {}".format(e))
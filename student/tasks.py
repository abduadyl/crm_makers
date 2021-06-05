from crm_back._celery import app
from celery.utils.log import get_task_logger
from datetime import datetime, timedelta, date
from django.db.models import Q
from .models import Student
from group.models import Group
from mailjet_rest import Client
from crm_back.settings import MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE, SENDER_EMAIL

logger = get_task_logger(__name__)

QUERYSET = Group.objects.all()


mailjet = Client(auth=(MJ_APIKEY_PUBLIC, MJ_APIKEY_PRIVATE), version='v3.1')

def send_mail(student_id):
    data = {
        'Messages': [
    {
      "From": {
        "Email": SENDER_EMAIL,
        "Name": "CRM"
      },
      "To": [
        {
          "Email": "corpviex@gmail.com",
          "Name": "Info About students"
        }
      ],
      "Subject": "Список студентов которые не оплатили",
      "TextPart": "Список",
      "HTMLPart": f"Лист студентов которые не оплатали: {student_id}"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print(result.json())


@app.task
def get_students_from_group(groups):
    for group in groups:
        students = group.student.get_queryset()
        for student in students:
            student.check = True
            send_mail(student.personal_data)
            student.save()


@app.task # run func every day at 12 a.m
def get_checked_groups():
    for query in QUERYSET:
        query.last_check = query.start
        month_ago = date.today() - timedelta(days=30)
        groups = Group.objects.filter(Q(last_check__lte=month_ago) | Q(last_check=month_ago))
        query.last_check = date.today()
        if groups:
            get_students_from_group(groups)
        query.save()


        

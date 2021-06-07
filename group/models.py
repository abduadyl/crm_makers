from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_title_generator


class Course(models.Model):
    COURSE_CHOICE = (
        ('JavaScript', 'JavaScript'),
        ('Python', 'Python'),
        ('FullStack', 'FullStack'),
        ('JavaScriptEvening', 'JavaScriptEvening'),
        ('PythonEvening', 'PythonEvening'),
    )
    type = models.CharField(max_length=50, choices=COURSE_CHOICE)

    def __str__(self):
        return self.type


class Group(models.Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='course')
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    start = models.DateField()
    end = models.DateField()
    total_students = models.PositiveIntegerField(default=0)
    last_check = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.title


def title_generator(sender, instance, *args, **kwargs):
    instance.title = unique_title_generator(instance)


pre_save.connect(title_generator, sender=Group)



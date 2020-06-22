from django.db import models

# Create your models here.
class Schedule(models.Model):
    """Schedule"""
    STATUS = (
        (10,"仮登録"),
        (20,"確定")
    )
    userId = models.CharField('code', max_length=255)
    start_time =  models.TimeField('startTime', blank=True, null=True)
    end_time = models.TimeField('endTime', blank=True, null=True)
    startDate = models.DateField('startDate', blank=True, null=True)
    comment =  models.TextField('comment', blank=True, null=True, max_length=5000 )
    title = models.CharField('title', blank=True, null=True, max_length=255 )
    status = models.IntegerField('ステータス', choices=STATUS, blank=True, null=True, default=10)

    def __str__(self):
        return self.title

class Users(models.Model):
    """Users"""
    STATUS = (
        (10,'正社員'),
        (20, 'パート'),
        (30, 'アルバイト')
    )
    name = models.CharField('名前', max_length=255)
    user_code = models.CharField('社員コード', max_length=255, null=True, blank=True)
    employment_status = models.IntegerField('雇用形態', choices=STATUS, blank=True, null=True)
    comment = models.TextField('comment', blank=True, null=True, max_length=5000 )

    def __str__(self):
        return self.name
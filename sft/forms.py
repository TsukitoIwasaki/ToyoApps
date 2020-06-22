from django import forms

from .models import Users, Schedule

class UsersForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ('name', 'user_code','employment_status', 'comment',)

class SchedulesForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('title', 'startDate', 'start_time', 'end_time', 'comment', 'status',)
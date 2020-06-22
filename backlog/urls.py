from django.urls import path
from backlog import views

app_name = 'backlog'
urlpatterns = [
    # 書籍
    path('issue/', views.issue_list, name='issue_list'),   # 一覧
]

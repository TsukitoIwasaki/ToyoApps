
from django.urls import path

from sft import views

app_name = 'sft'
urlpatterns = [
    # slack
    path('', views.index, name='index'),   # 一覧
    path('user_list/', views.user_list, name='user_list'),   # user一覧
    path('user/<int:pk>/', views.user_edit, name='user_edit'),  # 詳細
    path('user/add/', views.user_edit, name='user_add'),  # 追加
    path('sft_chart/', views.sft_chart, name='sft_chart'),   # シフトチャート
    path('schedule/<int:pk>/', views.schedule_edit, name='schedule_edit'),  # 詳細
    path('schedule/add/', views.schedule_edit, name='schedule_add'),  # 追加
    path('comment/', views.comment_list, name='comment_list'),   # 一覧
    path('department_list/', views.department_list, name='department_list'),  # 一覧
    path('department/<int:pk>/', views.department_edit, name='department_edit'),  # 詳細
    path('department/add/', views.department_edit, name='department_add'),  # 追加
    path('create_user/', views.create_slack_menber, name='create_slack_menber'),   # ユーザー作成
    # path('add_event$', views.add_event, name='add_event'),
    # path('sft_chart/update$', views.update, name='update'),
    # path('sft_chart/remove', views.remove, name='remove'),
]

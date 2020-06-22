from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .forms import UsersForm, SchedulesForm
from django.db.models import Q

from .models import Users, Schedule

def index(request):
    """TOPメニュー"""
    return render(request,
                  'sft/index.html',  # 使用するテンプレート
                    )  # テンプレートに渡すデータ

def user_list(request):
    """User List"""
    users = Users.objects.all()
    return render(request,
                  'sft/user_list.html',  # 使用するテンプレート
                  {'users': users}, )  # テンプレートに渡すデータ

def user_edit(request, pk=None):
    if pk:  # idがあるとき（編集の時）
        # idで検索して、結果を戻すか、404エラー
        member = get_object_or_404(Users, pk=pk)
    else:  # idが無いとき（新規の時）
        # Memberを作成
        member = Users()

    # POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = UsersForm(request.POST, instance=member)
        if form.is_valid():  # バリデーションがOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('sft:user_list')
    else:  # GETの時（フォームを生成）
        form = UsersForm(instance=member)

    # 新規・編集画面を表示
    return render(request, 'sft/member_edit.html', dict(form=form ))

def schedule_edit(request, pk=None):
    if pk:  # idがあるとき（編集の時）
        # idで検索して、結果を戻すか、404エラー
        schedule = get_object_or_404(Schedule, pk=pk)
    else:  # idが無いとき（新規の時）
        # Memberを作成
        schedule = Schedule()

    # POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = SchedulesForm(request.POST, instance=schedule)
        if form.is_valid():  # バリデーションがOKなら保存
            schedule = form.save(commit=False)
            schedule.save()
            return redirect('sft:sft_chart')
    else:  # GETの時（フォームを生成）
        form = SchedulesForm(instance=schedule)
    # 新規・編集画面を表示
    return render(request, 'sft/schedule_edit.html', dict(form=form, id=id))


def sft_chart(request):
    schedules = Schedule.objects.all()
    users = Users.objects.all()
    # 新規・編集画面を表示
    return render(request, 'sft/GanttChart.html', dict(schedules=schedules, users=users ))


def department_list(request):
    """Department List"""
    departments = Department.objects.all()
    return render(request,
                  'slack/department_list.html',  # 使用するテンプレート
                  {'departments': departments}, )  # テンプレートに渡すデータ

def department_edit(request, pk=None):
    if pk:  # idがあるとき（編集の時）
        # idで検索して、結果を戻すか、404エラー
        member = get_object_or_404(Department, pk=pk)
    else:  # idが無いとき（新規の時）
        # Memberを作成
        member = Department()

    # POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = DepartmentForm(request.POST, instance=member)
        if form.is_valid():  # バリデーションがOKなら保存
            member = form.save(commit=False)
            member.save()
            return redirect('slack:department_list')
    else:  # GETの時（フォームを生成）
        form = DepartmentForm(instance=member)
    # 新規・編集画面を表示
    return render(request, 'slack/department_edit.html', dict(form=form, id=id))


def comment_list(request):
    """メッセージの一覧"""
    # salckメッセージ取込
    get_slack();
    # ステータス更新
    update_status();

    departments = Department.objects.all()

    slacks = SlackMember.objects.all()
    keyword = request.GET.get('query')
    key = request.GET.get('key')
    print(key)
    if keyword:
        slacks = slacks.filter(
            Q(name__contains=keyword)
        )
    if key:
        slacks = slacks.filter(
            Q(department_id=key)
        )

    return render(request,
                  'slack/slack_index.html',  # 使用するテンプレート
                  {'slacks': slacks,
                   'departments': departments},)  # テンプレートに渡すデータ

def create_slack_menber(request):
    create_user();
    return HttpResponse('Create User')

def calendar(request):
    all_events = Schedule.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'GanttChart.html',context)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    resourceId = request.GET.get("resourceId", None)
    print(resourceId)
    event = Schedule(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Schedule.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)

def remove(request):
    id = request.GET.get("id", None)
    event = Schedule.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
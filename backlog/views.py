from django.shortcuts import render
from django.http import HttpResponse
from backlog.models import Issue


def issue_list(request):
    """課題の一覧"""
    issues = []
    names = Issue.objects.values('name').order_by('name').distinct()

    # namesがJSON形式の為配列へ変換
    values_len = len(names)
    i = 0
    values = []
    while i < values_len:
        json_name = names[i]
        json_name_value = json_name['name']
        values.append(json_name_value)
        i += 1

    names = values

    for name in names:
        issuebyname = Issue.objects.filter(name=name)
        for issue in issuebyname:
            issue.summary = issue.summary[:12]
            issue.elapsedTime = issue.elapsedTime
        issues.append(issuebyname)
        print(issues)

    return render(request,
                  'backlog/issue_list.html',  # 使用するテンプレート
                  {'issues': issues})  # テンプレートに渡すデータ

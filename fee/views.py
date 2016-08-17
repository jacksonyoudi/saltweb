# coding: utf-8
# Create your views here.

from __future__ import unicode_literals
import json
import sys

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# from dboperation.user import isuserexist
# from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout

import datetime


@login_required(login_url="/accounts/login")
def main(request):
    return render_to_response('main.html')


def test(request):
    print request.POST
    print "\n"
    one = request.POST['one']
    two = request.POST['two']
    print dir(request)
    # print type(request.POST)
    print "\n"
    print one
    print request.path
    print request.get_host()
    a = request.environ['HTTP_REFERER']
    print a
    print a.split('/')[3]
    # print c
    # print c[3]
    print type(one)
    print "\n"
    print two

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (
    a, one, two)
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    b = []
    for i in range(10):
        b.append('#32bdbc')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return render_to_response('bar.html', {'cost': json.dumps(a)})

    return HttpResponse('测试')


def debugg(request):
    return render_to_response('test.html')


import MySQLdb


def feehtml(request):
    c = MySQLdb.connect(host='localhost', user='fee', passwd='fee', db='fee', port=3306)
    cur = c.cursor()
    cur.execute('select * from cost;')
    t = cur.fetchall()
    cur.close()
    c.close()

    b = ['#6a6aff', '#82d900', '#984b4b', '#ff0000', '#46a3ff', '#f9f900', '#a5a552', '#ff79bc', '#00ffff', '#ff00ff',
         '#02f78f', '#ff8000', '#5a5aad', '#8600ff', '#00bb00', '#bb3d00', '#a5c2d5', '#cbab4f', '#76a871', '#a56f8f',
         '#c12c44', '#9f7961', '#6f83a5']
    z = zip(t, b)

    a = []
    for i in z:
        a.append({'name': i[0][1], 'value': int(i[0][2]), 'color': i[1]})

    print a
    return render_to_response('fee.html', {'cost': json.dumps(a)})


def linehtml(request):
    c = MySQLdb.connect(host='localhost', user='fee', passwd='fee', db='fee', port=3306)
    cur = c.cursor()
    cur.execute('select * from cost;')
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    for i in t:
        d.append(i[1])

    l = []
    for i in t:
        l.append(int(i[2]))

    return render_to_response('line.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def areahtml(request):
    c = MySQLdb.connect(host='localhost', user='fee', passwd='fee', db='fee', port=3306)
    cur = c.cursor()
    cur.execute('select * from cost;')
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    for i in t:
        d.append(i[1])

    l = []
    for i in t:
        l.append(int(i[2]))

    return render_to_response('area.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def composehtml(request):
    c = MySQLdb.connect(host='localhost', user='fee', passwd='fee', db='fee', port=3306)
    cur = c.cursor()
    cur.execute('select * from cost;')
    t = cur.fetchall()
    cur.execute('select * from comput;')
    c = cur.fetchall()
    cur.close()
    c.close()

    d = []
    for i in t:
        d.append(i[1])

    l = []
    for i in t:
        l.append(int(i[2]))

    return render_to_response('compose.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def charthtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    ldzw = cur.fetchall()
    cur.close()
    c.close()

    ldzwd = []
    ldzwl = []
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    cqb = cur.fetchall()
    cur.close()
    c.close()

    cqbd = []
    cqbl = []
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    tkzz = cur.fetchall()
    cur.close()
    c.close()

    tkzzd = []
    tkzzl = []
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d = tkzzd
    l = []
    l = map(lambda x, y, z: x + y + z, ldzwl, cqbl, tkzzl)
    print l
    print d

    b = ['#6a6aff', '#82d900', '#984b4b', '#ff0000', '#46a3ff', '#f9f900', '#a5a552', '#ff79bc', '#00ffff', '#ff00ff',
         '#02f78f', '#ff8000', '#5a5aad', '#8600ff', '#00bb00', '#bb3d00', '#a5c2d5', '#cbab4f', '#76a871', '#a56f8f',
         '#c12c44', '#9f7961', '#6f83a5']
    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})
    print a
    return render_to_response('chart.html', {'cost': json.dumps(a)})


def ldzwhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('line.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def cqbhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('line.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def tkzzhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('line.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def stackhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    ldzw = cur.fetchall()
    cur.close()
    c.close()

    ldzwd = []
    ldzwl = []
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    cqb = cur.fetchall()
    cur.close()
    c.close()

    cqbd = []
    cqbl = []
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    tkzz = cur.fetchall()
    cur.close()
    c.close()

    tkzzd = []
    tkzzl = []
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d = tkzzd
    l = []
    l = map(lambda x, y, z: x + y + z, ldzwl, cqbl, tkzzl)

    a = [{'name': '乱斗之王', 'value': ldzwl, 'color': '#32bdbc'}, {'name': '苍穹变', 'value': cqbl, 'color': '#d75a5e'},
         {'name': '坦克之战', 'value': tkzzl, 'color': '#be77ff'}]
    print a
    return render_to_response('stack.html', {'cost': json.dumps(a), 'd': json.dumps(d)})


def chartbarhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    ldzw = cur.fetchall()
    cur.close()
    c.close()

    ldzwd = []
    ldzwl = []
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    cqb = cur.fetchall()
    cur.close()
    c.close()

    cqbd = []
    cqbl = []
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    tkzz = cur.fetchall()
    cur.close()
    c.close()

    tkzzd = []
    tkzzl = []
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d = tkzzd
    l = []
    l = map(lambda x, y, z: x + y + z, ldzwl, cqbl, tkzzl)
    print l
    print d

    b = ['#6a6aff', '#82d900', '#984b4b', '#ff0000', '#46a3ff', '#f9f900', '#a5a552', '#ff79bc', '#00ffff', '#ff00ff',
         '#02f78f', '#ff8000', '#5a5aad', '#8600ff', '#00bb00', '#bb3d00', '#a5c2d5', '#cbab4f', '#76a871', '#a56f8f',
         '#c12c44', '#9f7961', '#6f83a5']
    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})
    print a
    return render_to_response('chartbar.html', {'cost': json.dumps(a)})


def ldzwbarhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    b = []
    for i in range(10):
        b.append('#32bdbc')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return render_to_response('bar.html', {'cost': json.dumps(a)})


def cqbbarhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    b = []
    for i in range(10):
        b.append('#d75a5e')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return render_to_response('bar.html', {'cost': json.dumps(a)})


def tkzzbarhtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))
    b = []
    for i in range(10):
        b.append('#be77ff')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return render_to_response('bar.html', {'cost': json.dumps(a)})


def ldzwareahtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('linearea.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def cqbareahtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('linearea.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def tkzzareahtml(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()

    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return render_to_response('linearea.html', {'labels': json.dumps(d), 'flow': json.dumps(l)})


def chartbar1html(request):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '乱斗之王'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    ldzw = cur.fetchall()
    cur.close()
    c.close()

    ldzwd = []
    ldzwl = []
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '苍穹变'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    cqb = cur.fetchall()
    cur.close()
    c.close()

    cqbd = []
    cqbl = []
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    a = '坦克之战'

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
    cur.execute(sql)
    tkzz = cur.fetchall()
    cur.close()
    c.close()

    tkzzd = []
    tkzzl = []
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d = tkzzd
    l = []
    l = map(lambda x, y, z: x + y + z, ldzwl, cqbl, tkzzl)
    print l
    print d

    b = ['#6a6aff', '#82d900', '#984b4b', '#ff0000', '#46a3ff', '#f9f900', '#a5a552', '#ff79bc', '#00ffff', '#ff00ff',
         '#02f78f', '#ff8000', '#5a5aad', '#8600ff', '#00bb00', '#bb3d00', '#a5c2d5', '#cbab4f', '#76a871', '#a56f8f',
         '#c12c44', '#9f7961', '#6f83a5']
    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})
    print a
    return render_to_response('chartbar1.html', {'cost': json.dumps(a)})


def excel(requset):
    # response = HttpResponse(mimetype='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment;filename=demo.xlsx'

    import xlsxwriter
    import MySQLdb
    import StringIO

    output = StringIO.StringIO()

    def getdata(b):
        c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
        cur = c.cursor()
        a = b

        sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' % a
        cur.execute(sql)
        t = cur.fetchall()
        cur.close()
        c.close()
        return t

    ldzwt = getdata('乱斗之王')
    cqbt = getdata('苍穹变')
    tkzzt = getdata('坦克之战')

    d = []
    ldzwl = []
    for i in ldzwt:
        d.append(str(i[0]))
        ldzwl.append(int(i[1]))

    cqbl = []
    for i in cqbt:
        cqbl.append(int(i[1]))

    tkzzl = []
    for i in tkzzt:
        tkzzl.append(int(i[1]))

    print ldzwl, cqbl, tkzzl, d

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('test')

    worksheet.set_column('A:A', 20)
    bold = workbook.add_format({'bold': True})

    top = workbook.add_format({'border': 6, 'align': 'center', 'bg_color': 'cccccc', 'font_size': 13, 'bold': True})
    title = ['date', 'ldzw_fee', 'cqb_fee', 'tkzz_fee']
    worksheet.write_row('A1', title, top)

    for i in range(2, len(d) + 2):
        p = 'A' + str(i)
        q = 'B' + str(i)
        m = 'C' + str(i)
        n = 'D' + str(i)

        j = i - 2

        worksheet.write(p, d[j])
        worksheet.write(q, ldzwl[j])
        worksheet.write(m, cqbl[j])
        worksheet.write(n, tkzzl[j])

    chart = workbook.add_chart({'type': 'column'})
    worksheet.insert_chart('A13', chart)

    chart.add_series({
        'categories': '=Sheet1!$A$2:$A$8',
        'values': '=Sheet1!$B$2:$B$8',
        'line': {'color': 'red'},
    })

    chart.add_series({
        'categories': '=Sheet1!$A$2:$A$8',
        'values': '=Sheet1!$C$2:$C$8',
        'line': {'color': 'red'},
    })

    chart.add_series({
        'categories': '=Sheet1!$A$2:$A$8',
        'values': '=Sheet1!$D$2:$D$8',
        'line': {'color': 'red'},
    })

    chart.set_x_axis({
        'name': 'date',
        'name_font': {'size': 14, 'bold': True},
    })

    chart.set_size({'width': 720, 'height': 576})
    chart.set_title({'name': 'Game Progrom Fee'})
    workbook.close()

    output.seek(0)

    response = HttpResponse(output.read(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=test.xlsx"
    # import StringIO,sys
    # output=StringIO.StringIO()
    # workbook.write(output)
    # output.seek(0)
    # response.write(output.getvalue())
    return response

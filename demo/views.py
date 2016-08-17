# Create your views here.
# coding: utf-8

from django.contrib.auth import authenticate, login, logout
# from __future__ import unicode_literals
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
from django.contrib.auth.decorators import login_required


def mysql(sql):  # 连接数据库，进行sql操作
    try:
        c = MySQLdb.connect(host='localhost', user='saltweb', passwd='saltweb', db='saltweb', port=3306)
        cur = c.cursor()
        cur.execute(sql)
        t = cur.fetchall()
        cur.close()
        c.close()
        return t[0][0]
    except Exception, e:
        print e


def data(m):
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()

    sql = 'select date,money from (select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d  order by date desc limit 15) as e order by date;' % m
    cur.execute(sql)
    t = cur.fetchall()
    cur.close()
    c.close()
    print t
    d = []
    l = []
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))
    b = []
    for i in range(20):
        b.append('#32bdbc')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})
    print a
    return a


def alld():
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

    sql = 'select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date ;' % a
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
    return a


def alldate(request):
    on = request.POST['one']
    tw = request.POST['two']
    one = on.replace('-', '', 2)
    two = tw.replace('-', '', 2)

    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
    m = '乱斗之王'

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (
    m, one, two)
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
    m = '苍穹变'

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (
    m, one, two)
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
    m = '坦克之战'

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (
    m, one, two)
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
    return a


# from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext


# from dboperation.user import isuserexist
# from users.models import User

# @csrf_protect
def denglu(request):
    return render_to_response("account.html")


# @csrf_protect
def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        username = user.username
        sql = 'select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
        a = mysql(sql)
        print dir(request.user)
        print request.user.username
        print request.user.is_superuser
        one = '2016-01-01'
        two = '2016-07-01'
        if a == "ldzw":
            m = '乱斗之王'
            fee = data(m)
            return render_to_response('game.html',
                                      {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one,
                                       'two': two})

        if a == "cqb":
            m = '苍穹变'
            fee = data(m)
            return render_to_response('game.html',
                                      {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one,
                                       'two': two})

        if a == "tkzz":
            m = '坦克之战'
            fee = data(m)
            return render_to_response('game.html',
                                      {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one,
                                       'two': two})
        if a == "admin":
            fee = alld()
            username = u'root'
            m = u'所有游戏业务项目'
            end = 2000000
            scale = 200000
            return render_to_response('all.html',
                                      {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                       'username': username, 'program': json.dumps(m), 'one': one, 'two': two})
    else:
        return render_to_response("account.html")


@login_required(login_url="/account/")
def logout_view(request):
    logout(request)
    return render_to_response("account.html")


def senddata(m):
    fee = data(m)
    return fee


def datadate(m, request):  # 处理在admin页面中单个游戏业务的数据
    on = request.POST['one']
    tw = request.POST['two']
    one = on.replace('-', '', 2)
    two = tw.replace('-', '', 2)

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % ( m, one, two)
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
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
    for i in range(20):
        b.append('#32bdbc')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return a


@login_required(login_url="/account/")
def ldzw(request):
    if request.user.is_superuser:
        one = '2016-01-01'
        two = '2016-07-01'
        ldzw = u'selected'
        m = '乱斗之王'
        fee = senddata(m)
        username = request.user.username
        end = 1000000
        scale = 100000
        return render_to_response('all.html',
                                  {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                   'username': username, 'program': json.dumps(m), 'ldzw': ldzw, 'one': one, 'two': two,
                                   'net': 'in'})
    else:
        return render_to_response("505.html")


@login_required(login_url="/account/")
def cqb(request):
    if request.user.is_superuser:
        one = '2016-01-01'
        two = '2016-07-01'
        m = '苍穹变'
        cqb = u'selected'
        fee = senddata(m)
        username = request.user.username
        end = 1000000
        scale = 100000
        return render_to_response('all.html',
                                  {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                   'username': username, 'program': json.dumps(m), 'cqb': cqb, 'one': one, 'two': two,
                                   'net': 'in'})
    else:
        return render_to_response("505.html")


@login_required(login_url="/account/")
def tkzz(request):
    if request.user.is_superuser:
        one = '2016-01-01'
        two = '2016-07-01'
        tkzz = u'selected'
        m = '坦克之战'
        fee = senddata(m)
        username = request.user.username
        end = 1000000
        scale = 100000
        return render_to_response('all.html',
                                  {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                   'username': username, 'program': json.dumps(m), 'tkzz': tkzz, 'one': one, 'two': two,
                                   'alone': 'in'})
    else:
        return render_to_response("505.html")


@login_required(login_url="/account/")
def showall(request):
    if request.user.is_superuser:
        one = '2016-01-01'
        two = '2016-07-01'
        fee = alld()
        username = request.user.username
        m = '所有游戏业务项目'
        end = 2000000
        scale = 200000
        return render_to_response('all.html',
                                  {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                   'username': username, 'program': json.dumps(m), 'one': one, 'two': two})
    else:
        return render_to_response("505.html")


def submitdate(m, request):
    on = request.POST['one']
    tw = request.POST['two']
    one = on.replace('-', '', 2)
    two = tw.replace('-', '', 2)

    sql = 'select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (
    m, one, two)
    c = MySQLdb.connect(host='localhost', user='ledou', passwd='ledou', db='ledou', port=3306, charset='utf8')
    cur = c.cursor()
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
    for i in range(20):
        b.append('#32bdbc')

    z = zip(d, l, b)
    print z

    a = []
    for i in z:
        a.append({'name': i[0], 'value': int(i[1]), 'color': i[2]})

    return a


@login_required(login_url="/account/")
def ldzwdate(request):
    username = request.user.username
    m = '乱斗之王'
    fee = submitdate(m, request)
    return render_to_response('game.html', {'cost': json.dumps(fee), 'username': username, 'program': m})


@login_required(login_url="/account/")
def update(request):
    all = u''
    ldzw = u''
    cqb = u''
    tkzz = u''
    one = request.POST['one']
    two = request.POST['two']
    username = request.user.username
    sql = 'select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
    a = mysql(sql)
    if a == "ldzw":
        m = '乱斗之王'
        fee = submitdate(m, request)
        return render_to_response('game.html',
                                  {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one, 'two': two})

    if a == "cqb":
        m = '苍穹变'
        fee = submitdate(m, request)
        return render_to_response('game.html',
                                  {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one, 'two': two})

    if a == "tkzz":
        m = '坦克之战'
        fee = submitdate(m, request)
        return render_to_response('game.html',
                                  {'cost': json.dumps(fee), 'username': username, 'program': m, 'one': one, 'two': two})
    if a == "admin":
        three = request.POST['three']
        if request.POST['three'] == u'所有游戏业务项目':
            fee = alldate(request)
            username = u'root'
            m = u'所有游戏业务项目'
            end = 2000000
            scale = 200000
            all = u'selected'
            return render_to_response('all.html',
                                      {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                       'username': username, 'program': json.dumps(m), 'one': one, 'two': two,
                                       'three': three, 'all': all, 'ldzw': ldzw, 'cqb': cqb, 'tkzz': tkzz})

        if request.POST['three'] == u'乱斗之王':
            m = '乱斗之王'
            fee = datadate(m, request)
            username = request.user.username
            end = 1000000
            scale = 100000
            ldzw = u'selected'
            return render_to_response('all.html',
                                      {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                       'username': username, 'program': json.dumps(m), 'one': one, 'two': two,
                                       'three': three, 'all': all, 'ldzw': ldzw, 'cqb': cqb, 'tkzz': tkzz})
        if request.POST['three'] == u'苍穹变':
            m = '苍穹变'
            fee = datadate(m, request)
            username = request.user.username
            end = 1000000
            scale = 100000
            cqb = u'selected'
            return render_to_response('all.html',
                                      {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                       'username': username, 'program': json.dumps(m), 'one': one, 'two': two,
                                       'three': three, 'all': all, 'ldzw': ldzw, 'cqb': cqb, 'tkzz': tkzz})
        if request.POST['three'] == u'坦克之战':
            m = '坦克之战'
            fee = datadate(m, request)
            username = request.user.username
            end = 1000000
            scale = 100000
            tkzz = u'selected'
            return render_to_response('all.html',
                                      {'cost': json.dumps(fee), 'end': json.dumps(end), 'scale': json.dumps(scale),
                                       'username': username, 'program': json.dumps(m), 'one': one, 'two': two,
                                       'three': three, 'all': all, 'ldzw': ldzw, 'cqb': cqb, 'tkzz': tkzz})

        else:
            return render_to_response("505.html")


def table(request):
    all = u''
    ldzw = u''
    cqb = u''
    tkzz = u''
    if request.method == 'POST':
        one = request.POST['one']
        two = request.POST['two']
        username = request.user.username
        sql = 'select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
        a = mysql(sql)
        if a == "ldzw":
            m = '乱斗之王'
            fee = submitdate(m, request)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'one': one, 'two': two, 'a': 'disabled',
                                       'ldzw': 'selected'})

        if a == "cqb":
            m = '苍穹变'
            fee = submitdate(m, request)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'one': one, 'two': two, 'a': 'disabled',
                                       'cqb': 'selected'})

        if a == "tkzz":
            m = '坦克之战'
            fee = submitdate(m, request)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'one': one, 'two': two, 'a': 'disabled',
                                       'tkzz': 'selected'})
        if a == "admin":
            three = request.POST['three']
            if request.POST['three'] == u'所有游戏业务项目':
                fee = alldate(request)
                username = u'root'
                m = u'所有游戏业务项目'
                all = u'selected'
                return render_to_response('showtable.html',
                                          {'dat': fee, 'program': m, 'one': one, 'two': two, 'all': all, 'ldzw': ldzw,
                                           'cqb': cqb, 'tkzz': tkzz})

            if request.POST['three'] == u'乱斗之王':
                m = '乱斗之王'
                fee = datadate(m, request)
                username = request.user.username
                ldzw = u'selected'
                return render_to_response('showtable.html',
                                          {'dat': fee, 'program': m, 'one': one, 'two': two, 'all': all, 'ldzw': ldzw,
                                           'cqb': cqb, 'tkzz': tkzz})
            if request.POST['three'] == u'苍穹变':
                m = '苍穹变'
                fee = datadate(m, request)
                username = request.user.username
                cqb = u'selected'
                return render_to_response('showtable.html',
                                          {'dat': fee, 'program': m, 'one': one, 'two': two, 'all': all, 'ldzw': ldzw,
                                           'cqb': cqb, 'tkzz': tkzz})

            if request.POST['three'] == u'坦克之战':
                m = '坦克之战'
                fee = datadate(m, request)
                username = request.user.username
                tkzz = u'selected'
                return render_to_response('showtable.html',
                                          {'dat': fee, 'program': m, 'one': one, 'two': two, 'all': all, 'ldzw': ldzw,
                                           'cqb': cqb, 'tkzz': tkzz})

            else:
                return render_to_response("505.html")
    else:
        username = request.user.username
        sql = 'select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
        a = mysql(sql)
        one = '2016-01-01'
        two = '2016-07-01'
        if a == "ldzw":
            m = '乱斗之王'
            fee = data(m)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'a': 'disabled', 'ldzw': 'selected', 'one': one,
                                       'two': two})

        if a == "cqb":
            m = '苍穹变'
            fee = data(m)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'a': 'disabled', 'cqb': 'selected', 'one': one,
                                       'two': two})

        if a == "tkzz":
            m = '坦克之战'
            fee = data(m)
            return render_to_response('showtable.html',
                                      {'dat': fee, 'program': m, 'a': 'disabled', 'tkzz': 'selected', 'one': one,
                                       'two': two})
        if a == "admin":
            program = u'所有游戏业务项目'
            dat = alld()
            username = u'root'
            all = u'selected'
            return render_to_response('showtable.html', locals())


def information(request):
    return render_to_response('information.html')

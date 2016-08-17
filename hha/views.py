# Create your views here.
#coding: utf-8

from django.contrib.auth import authenticate,login,logout
#from __future__ import unicode_literals
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb
from django.contrib.auth.decorators import login_required

def mysql(sql):   #连接数据库，进行sql操作
    try:
        c=MySQLdb.connect(host='localhost',user='saltweb',passwd='saltweb',db='saltweb',port=3306)
        cur=c.cursor()
        cur.execute(sql)
        t=cur.fetchall()
        cur.close()
        c.close()
        return t[0][0]
    except Exception,e:
        print e

def data(m):
    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()

    sql='select date,money from (select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d  order by date desc limit 15) as e order by date;' % m
    cur.execute(sql)
    t=cur.fetchall()
    cur.close()
    c.close()
    d=[]
    l=[]
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return  d,l

def all():
    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    a='乱斗之王'

    sql='select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' %a
    cur.execute(sql)
    ldzw=cur.fetchall()
    cur.close()
    c.close()

    ldzwd=[]
    ldzwl=[]
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))


    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    a='苍穹变'

    sql='select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date ;' %a
    cur.execute(sql)
    cqb=cur.fetchall()
    cur.close()
    c.close()

    cqbd=[]
    cqbl=[]
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    a='坦克之战'

    sql='select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date;' %a
    cur.execute(sql)
    tkzz=cur.fetchall()
    cur.close()
    c.close()

    tkzzd=[]
    tkzzl=[]
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d=tkzzd
    l=[]
    l=map(lambda x,y,z:x+y+z,ldzwl,cqbl,tkzzl)


    return d,l

def alldate(request):
    on=request.POST['one']
    tw=request.POST['two']
    one=on.replace('-','',2)
    two=tw.replace('-','',2)

    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    m='乱斗之王'

    sql='select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (m,one,two)
    cur.execute(sql)
    ldzw=cur.fetchall()
    cur.close()
    c.close()

    ldzwd=[]
    ldzwl=[]
    for i in ldzw:
        ldzwd.append(str(i[0]))
        ldzwl.append(int(i[1]))


    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    m='苍穹变'

    sql='select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (m,one,two)
    cur.execute(sql)
    cqb=cur.fetchall()
    cur.close()
    c.close()

    cqbd=[]
    cqbl=[]
    for i in cqb:
        cqbd.append(str(i[0]))
        cqbl.append(int(i[1]))

    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    m='坦克之战'

    sql='select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (m,one,two)
    cur.execute(sql)
    tkzz=cur.fetchall()
    cur.close()
    c.close()

    tkzzd=[]
    tkzzl=[]
    for i in tkzz:
        tkzzd.append(str(i[0]))
        tkzzl.append(int(i[1]))

    d=tkzzd
    l=[]
    l=map(lambda x,y,z:x+y+z,ldzwl,cqbl,tkzzl)
    print l
    print d

    return d,l




#from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render,render_to_response,RequestContext
#from dboperation.user import isuserexist
#from users.models import User

#@csrf_protect
def  dengluline(request):
     return render_to_response("accountline.html")

#@csrf_protect
def login_viewline(request):
    user = authenticate(username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        login(request,user)
        username=user.username
        sql='select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
        a=mysql(sql)
        print dir(request.user)
        print request.user.username
        print request.user.is_superuser
        if  a == "ldzw":
            m='乱斗之王'
            labels,dataline = data(m)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})

        if a == "cqb":
            m='苍穹变'
            labels,dataline = data(m)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})


        if a == "tkzz":
            m='坦克之战'
            labels,dataline = data(m)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})

        if a == "admin":
            labels,dataline = all()
            m=u'所有游戏业务项目'
            username=request.user.username
            end=1000000
            scale=100000
            return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
        return render_to_response("accountline.html")

@login_required(login_url="/accountline/")
def logout_viewline(request):
    logout(request)
    return render_to_response("accountline.html")



def senddata(m):
    lables,dataline = data(m)
    return lables,dataline


def datadate(m,request):   #处理在admin页面中单个游戏业务的数据
    on=request.POST['one']
    tw=request.POST['two']
    one=on.replace('-','',2)
    two=tw.replace('-','',2)

    sql='select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (m,one,two)
    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    cur.execute(sql)
    t=cur.fetchall()
    cur.close()
    c.close()
    d=[]
    l=[]
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1]))

    return  d,l









@login_required(login_url="/accountline/")
def ldzwline(request):
    if request.user.is_superuser:
        m = '乱斗之王'
        labels,dataline=senddata(m)
        username=request.user.username
        end=1000000
        scale=100000
        return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
    else:
        return render_to_response("505.html")

@login_required(login_url="/accountline/")
def cqbline(request):
    if request.user.is_superuser:
        m = '苍穹变'
        labels,dataline=senddata(m)
        username=request.user.username
        end=1000000
        scale=100000
        return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
    else:
        return render_to_response("505.html")


@login_required(login_url="/accountline/")
def tkzzline(request):
    if request.user.is_superuser:
        m = '坦克之战'
        labels,dataline=senddata(m)
        username=request.user.username
        end=1000000
        scale=100000
        return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
    else:
        return render_to_response("505.html")


@login_required(login_url="/accountline/")
def showallline(request):
    if request.user.is_superuser:
        labels,dataline = all()  #不确定
        m='所有游戏业务项目'
        labels,dataline=datadate(m,request)
        username=request.user.username
        end=1000000
        scale=100000
        return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
    else:
        return render_to_response("505.html")

def submitdate(m,request):
    on=request.POST['one']
    tw=request.POST['two']
    one=on.replace('-','',2)
    two=tw.replace('-','',2)

    sql='select * from (select date,money from (select b.projectName,a.date,a.money from server_costs as a join project_info as b on a.projectId=b.projectid) as c where projectName="%s" order by date) as d where date between "%s" and "%s" ;' % (m,one,two)
    c=MySQLdb.connect(host='localhost',user='ledou',passwd='ledou',db='ledou',port=3306, charset='utf8')
    cur=c.cursor()
    cur.execute(sql)
    t=cur.fetchall()
    cur.close()
    c.close()
    d=[]
    l=[]
    for i in t:
        d.append(str(i[0]))
        l.append(int(i[1])

    return  d,l


@login_required(login_url="/accountline/")
def ldzwdateline(request):
    username=request.user.username
    m='乱斗之王'
    labels,dataline=submitdate(m,request)
    return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})


@login_required(login_url="/accountline/")
def updateline(request):
        username=request.user.username
        sql='select c.name from auth_user as a,auth_user_groups as b,auth_group as c where a.id=b.user_id and b.group_id = c.id and a.username="%s";' % username
        a=mysql(sql)
        if  a == "ldzw":
            m='乱斗之王'
            labels,dataline=submitdate(m,request)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})


        if a == "cqb":
            m='苍穹变'
            labels,dataline=submitdate(m,request)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})
        if a == "tkzz":
            m='坦克之战'
            labels,dataline=submitdate(m,request)
            return  render_to_response('gameline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'username':username,'program':m})
        if a == "admin":
            if request.POST['three'] == u'所有游戏业务项目':
                labels,dataline = alldate(request)
                username = u'root'
                m=u'所有游戏业务项目'
                end=2000000
                scale=200000
                return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})

            if request.POST['three'] == u'乱斗之王':
                m = '乱斗之王'
                labels,dataline=datadate(m,request)
                username=request.user.username
                end=1000000
                scale=100000
                return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
            if request.POST['three'] == u'苍穹变':
                m = '苍穹变'
                labels,dataline=datadate(m,request)
                username=request.user.username
                end=1000000
                scale=100000
                return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})
            if request.POST['three'] == u'坦克之战':
                m = '坦克之战'
                labels,dataline=datadate(m,request)
                username=request.user.username
                end=1000000
                scale=100000
                return  render_to_response('allline.html', {'flow': json.dumps(dataline),'labels': json.dumps(labels),'end': json.dumps(end),'scale': json.dumps(scale),'username':username,'program':m})

            else:
                return render_to_response("505.html")



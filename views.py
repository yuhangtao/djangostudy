from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades,Students

def index(request):
    return HttpResponse("sunck is a good man")

def grades(request):

    gradeslist=Grades.objects.all()

    return render(request,'myapp/grades.html',{'grades':gradeslist})

def student(request):

    studentlist=Students.objects.all()

    return render(request,'myapp/students.html',{'students':studentlist})

def gradestudent(request,num):

    grade=Grades.objects.get(pk=num)
    studentlist=grade.students_set.all()
    return render(request, 'myapp/students.html', {'students': studentlist})

def get1(request):
    #get方法为获取类似于http://127.0.0.1:8000/get1?a=1&b=2&c=3中的某些参数，若想获取某一变量的多个值可用getlist
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+''+b+''+c)

def register(request):
    name=request.POST.get('name')
    gender=request.POST.get('gender')
    age=request.POST.get('age')
    hobby = request.POST.getlist('hobby')
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse('注册成功')

def showregister(request):
    return render(request,'myapp/register.html')

def testcookie(request):

    res=HttpResponse()
    cookie=request.COOKIES
    res.write('<h1>'+cookie['test']+'</h1>')
    #cookie=res.set_cookie("test","good") #给cookie添加键值对
    return res
1
from django.http import HttpResponseRedirect
def redirect1(request):

    return HttpResponseRedirect('showregister/') #跳转到另一个页面 也就是重定向


def main(request):
    #取出session值 可使用BASE64解码session值
    username=request.session.get('username','游客') #第二个参数为默认值
    return  render(request,'myapp/main.html',{'username':username})

def login(request):
    return render(request,'myapp/login.html')

def showmain(request):
    #提取数据
    username=request.POST.get('username')
    #存储数据到session
    request.session['username']=username
    return HttpResponseRedirect('/main/')

#from django.contrib.auth import logout
def quit(request):
    #清除session
    #logout(request)
    request.session.clear()
    return HttpResponseRedirect('/main/')

def upfile(request):
    return render(request,'myapp/upfile.html')

import os
from django.conf import settings
def savefile(request):
    if request.method=="POST":
        f=request.FILES["file"]
        filepath=os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filepath,'wb') as fp:
            for i in f.chunks():
                fp.write(i)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")

def edit(request):
    return render(request,'myapp/edit.html')
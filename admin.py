from django.contrib import admin

# Register your models here.
from .models import Students,Grades

class StudentInfo(admin.TabularInline):
    model=Students
    extra=2

class GradesAdmin(admin.ModelAdmin):

    #创建类型时添加子类型
    inlines=[StudentInfo]
    #列表页属性
    #1.显示字段
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    #2.添加过滤器
    list_filter = ['gname']
    #3.添加查找器
    search_fields = ['gname']
    #分页功能
    list_per_page =5

    #添加，修改页属性
    #1.改变顺序
    #fields =['ggirlnum','gboynum','gname','gdate','isDelete']
    #2.给属性分组  fields与fieldsets不能同时使用
    fieldsets =[
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']})
    ]

admin.site.register(Grades,GradesAdmin)

class StudentAdmin(admin.ModelAdmin):

    #运用函数修改布尔值
    def gender(self):
        if self.sgender:
            return"男"
        else:
            return"女"

    #修改列名称
    gender.short_description = "性别"

    list_display = ['pk', 'sname', 'sage', 'scontend', gender,'sgrade','isDelete']
    list_per_page = 2
admin.site.register(Students,StudentAdmin)

from .models import text
admin.site.register(text)
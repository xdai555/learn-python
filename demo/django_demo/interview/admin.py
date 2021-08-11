import imp
from re import A
from django.contrib import admin
from django.db import models
from django.http.response import HttpResponse
from django.utils.safestring import mark_safe
from interview.models import Candidate
from jobmanage.models import Resume
from datetime import datetime
import csv
import logging
from interview import dingtalk
from django.contrib import messages

# Register your models here.
logging.basicConfig(level=logging.DEBUG)


EXPORT_LIST = ('username', 'city', 'phone','email','born_address')

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response.charset = 'utf-8-sig' if "Windows" in request.headers.get('User-Agent') else 'utf-8'
    field_list = EXPORT_LIST
    response['Content-Disposition'] = 'attachment; filename=export-%s.csv' %(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name for f in field_list],
    )
    for obj in queryset:
        csv_line_values = []
        for field in field_list:
            field_obj = queryset.model._meta.get_field(field)
            field_value = field_obj.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)
    logging.info("%s exported %s recoreds."%(request.user, len(queryset)))
    return response

def notify(modeladmin, request, queryset):
    msg = "测试消息：\n"
    for obj in queryset:
        msg += "%s 的手机号是 %s\n" %( obj.username, obj.phone)
    dingtalk.send_msg(msg)
    messages.add_message(request, messages.INFO, "发送成功")


class CandidateAdmin(admin.ModelAdmin):
    # 排除显示
    exclude = ('creator','created_date', 'modified_date')
    # 显示字段，可以显示模型里面定义的字段，也可以显示函数

    def get_resume(self, obj):
        if not obj.username:
            return ""
        resumes = Resume.objects.filter(username=obj.username)
        if resumes and len(resumes) > 0:
            return mark_safe('<a href="/resume/%s" target="_blank">查看简历</a>'%resumes[0].id)
        return ""

    get_resume.short_description = "查看简历"
    get_resume.allow_tags = True    


    list_display = ('username', "get_resume", 'city', 'phone','email','born_address')
    # 字段详情页分组
    fieldsets = (
        (None, {'fields': (('username','phone'),)}),
        ("城市", {'fields': (('city','email'),'born_address')}),
    )
    # 查询字段
    search_fields = ('username','phone','email')
    # 筛选字段
    list_filter = ('city','username')
    # 默认排序字段
    ordering = ('city','username')
    actions = [export_to_csv, notify]

    # 添加动作相关的权限控制
    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm('%s.%s'% (opts.app_label,"export"))

    # 手动设置只读字段，这样所有的用户都无法修改
    # readonly_fields = ('age',)

    # 根据用户进行判断设置只读字段
    # 先通过 request.user 获取用户所属的组
    def get_group_names(self,user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        print(user,user.groups.all())
        return group_names
    # 通过用户判断所属组信息，如果属于某个组，设置只读字段，这里是重写父类的指定方法
    def get_readonly_fields(self, request, obj):
        group_names = self.get_group_names(request.user)
        print(group_names)
        if "readonly" in group_names:
            return ("city",) # 返回只读字段
        return ()
    
    # 设置在浏览页面上可以直接修改内容
    # list_editable = ('city',)
    # 同样这里也可以使用一个函数进行判断，指定的用户才能在浏览页面修改内容
    default_list_editable = ('city',)
    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or "editable_group" in group_names:
            return self.default_list_editable
        return ()
    # 这里需要重写父类的 changelist 方法来对 list_editable 赋值
    def get_changelist_instance(self, request):
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)
    


export_to_csv.short_description = "导出为 CSV..."
# 为动作设置权限为 export，具有该权限的才能执行，权限需要在 models 里的 meta 类里定义
# 
export_to_csv.allowed_permissions = ("export",)
admin.site.register(Candidate, CandidateAdmin)
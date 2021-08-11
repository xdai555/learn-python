from datetime import datetime
from django.contrib import admin
from jobmanage.models import Job, Resume
from django.contrib import messages
from interview.models import Candidate

# Register your models here.

def enter_interview_process(modeladmin, request, queryset):
    candidate_names = ""
    for  resume in queryset:
        # 把对象属性全部赋值到另外的对象中
        candidate = Candidate()
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.creator = request.user.username
        candidate.save()
    messages.add_message(request, messages.INFO, "已经进入面试环节")

enter_interview_process.short_description = "进入面试流程"

class JobAdmin(admin.ModelAdmin):
    # 前端要隐藏的字段
    exclude = ('creator', 'created_date', 'modify_date')
    # 显示在前端的信息
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modify_date')

    # 在页面提交时，需要自动保存的信息
    def save_model(self, request, obj, form, change):
        # 时间自动生成了，但是创建人还是需要手动选择，所以这里的作用是在提交的时候填充上创建人
        obj.creator = request.user
        # 提交的时候自动更新修改时间
        obj.modify_date = datetime.now()
        return super().save_model(request, obj, form, change)

class ResumeAdmin(admin.ModelAdmin):
    
    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major','created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    actions = [enter_interview_process,]

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender", ), ("picture", "attachment",),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience","project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)
    ...

# 两个都需要注册
admin.site.register(Job, JobAdmin)
admin.site.register(Resume, ResumeAdmin)
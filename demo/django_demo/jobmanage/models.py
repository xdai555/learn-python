from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
]

Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳"),
]

DEGREE_TYPE = ((u'本科', u'本科'), (u'硕士', u'硕士'), (u'博士', u'博士'))

class Job(models.Model):
    # 使用下拉选项，需要定义一个列表
    job_type = models.SmallIntegerField(
        blank=False, choices=JobTypes, verbose_name=_("职位类别"))
    job_name = models.CharField(
        max_length=250, blank=False, verbose_name=_("职位名称"))
    job_city = models.SmallIntegerField(
        choices=Cities, blank=False, verbose_name=_("工作地点"))
    job_responsibility = models.TextField(
        max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(
        max_length=1024, blank=False, verbose_name="职位要求")
    # 通过外键关联默认的鉴权系统，给创建人赋值为当前登录的用户
    creator = models.ForeignKey(
        User, verbose_name=_("创建人"), on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(verbose_name=_("创建日期"), default=datetime.now)
    modify_date = models.DateTimeField(verbose_name=_("修改时间"), default= datetime.now)
# 之后需要在 admin 里面注册一下当前的模型，使其可以在 admin 管理页面中显示。


class Resume(models.Model):
    username = models.CharField(max_length=135, verbose_name=_('姓名'))
    applicant = models.ForeignKey(User, verbose_name=_("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=_('城市'))
    phone = models.CharField(max_length=135,  verbose_name=_('手机号码'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=_('邮箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=_('应聘职位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=_('生源地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=_('性别'))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=_('个人照片')) 
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=_('简历附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=_('本科学校'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=_('研究生学校'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士生学校')
    major = models.CharField(max_length=135, blank=True, verbose_name=_('专业'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=_('学历'))
    created_date = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'工作经历')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'项目经历')

    class Meta:
        verbose_name = _('简历')
        verbose_name_plural = _('简历列表')
    
    def __str__(self):
        return self.username

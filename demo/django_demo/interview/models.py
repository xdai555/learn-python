from django.db import models

# Create your models here.
class Candidate(models.Model):
    username = models.CharField(max_length=135, verbose_name='姓名')
    city = models.CharField(max_length=135, verbose_name='城市')
    phone = models.CharField(max_length=135, verbose_name='手机号码')
    email = models.EmailField(max_length=135, blank=True, verbose_name='邮箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name='应聘职位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name='生源地',help_text="老家是哪里的呀？")
    gender = models.CharField(max_length=135, blank=True, verbose_name='性别')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name='候选人信息备注')
    
    creator = models.CharField(max_length=256, blank=True, verbose_name='候选人数据的创建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name='最后编辑者')

    class Meta:
        db_table = 'canditate'
        # 单条信息显示的信息
        verbose_name = '应聘者'
        # 复数显示的信息
        verbose_name_plural = '应聘者'
        # 定义权限，然后在 admin 中授权
        permissions = [
            ("export", "Can export db"),
            ("notify", "Can notify message"),
        ]
    
    def __str__(self):
        return self.username
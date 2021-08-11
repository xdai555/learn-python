from django import template
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from jobmanage.models import Job, Cities, JobTypes, Resume

# Create your views here.

def job_list(request):
    job_list = Job.objects.order_by("job_type")
    template = loader.get_template('job_list.html')
    
    context = {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))

def job(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("职位不存在")
    return render(request, "job.html", {"job":job})

# 使用类定义一个简历视图
class ResumeCreateView(LoginRequiredMixin, CreateView):
    # 定义使用哪个模板
    template_name = 'resume_form.html'
    # 定义成功后的重定向页面
    success_url = '/job_list/'
    # 定义使用的 model
    model = Resume
    # 定义表单页面要显示 model 里面的哪些字段
    fields = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major',)
	# 定义获取初始值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        print(initial)
        return initial
	# 数据验证及保存数据，并进行重定向
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResumeDitailView(LoginRequiredMixin, DetailView):
    model = Resume
    template_name = "resume_detail.html"
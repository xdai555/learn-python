from django.conf.urls import url
from django.db.models import fields
from django.urls.conf import path, include
from jobmanage import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from jobmanage.models import Job


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('job_list', JobViewSet)


urlpatterns = [
    url(r"^$", views.job_list, name="job_list"),
    url(r"^job_list/", views.job_list, name="job_list"),
    url(r"^job/(?P<job_id>\d+)/$", views.job, name="job"),
    url(r'^resume/add/', views.ResumeCreateView.as_view(), name='resume_add'),
    path('resume/<int:pk>/', views.ResumeDitailView.as_view(), name='resume_detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

from django.urls import path, include
from .views import indexA, indexaaa, indexbbb, indexccc

app_name = 'a'

urlpatterns = [
    path('', indexA, name='sampleA'),
    path('aaa/', indexaaa, name='sampleaaa'),
    path('bbb/', indexbbb),
    path('ccc/', indexccc),
]

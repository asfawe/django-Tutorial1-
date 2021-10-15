from django.shortcuts import render
from django.views.generic import ListView, DetailView
from b.models import Blog

# def indexC(request):
#    return render(request, 'indexC.html')

class BlogList(ListView): #여기서 class명은 상관이 없습니다.
    model = Blog
    template_name = 'indexC.html'
    ordering = '-pk'
    
class BlogDetail(DetailView):
    model = Blog
    template_name = 'indexCdetail.html'
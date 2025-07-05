from django.shortcuts import render, get_object_or_404
from .models import MBTIType

def home(request):
    mbti_types = MBTIType.objects.all()
    return render(request, 'pages/home.html', {'mbti_types': mbti_types})

def mbti_detail(request, pk):
    mbti = get_object_or_404(MBTIType, pk=pk)
    return render(request, 'pages/mbti_detail.html', {'mbti': mbti})

def about(request):
    return render(request, 'pages/about.html')

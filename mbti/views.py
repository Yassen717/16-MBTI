from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import MBTIType


def home(request):
    q = request.GET.get('q', '').strip()
    mbti_types = MBTIType.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)) if q else MBTIType.objects.all()
    return render(request, 'pages/home.html', {'mbti_types': mbti_types, 'q': q})


def mbti_detail(request, pk):
    mbti = get_object_or_404(MBTIType, pk=pk)
    return render(request, 'pages/mbti_detail.html', {'mbti': mbti})


def about(request):
    return render(request, 'pages/about.html')

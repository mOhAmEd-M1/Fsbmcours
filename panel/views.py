from django.shortcuts import render

# Create your views here.
def homepanel(request):
  context = {}
  return render(request,'panel/index.html',context)
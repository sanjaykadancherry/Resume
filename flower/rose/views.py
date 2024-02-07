from django.shortcuts import render

# Create your views here.
# def demo(request):
#     return render(request,"index.html")
# def gallery(request):
#     return render(request,"gallery.html")
#
# def about(request):
#     return HttpResponse("I am about page")
#
# def contact(request):
#     return HttpResponse("I am contact page")


def index(request):
    return render(request,"index.html")

from django.http import HttpResponse


def hello(request):
    print(r"/ / ( . )Y( . ) \ \ ")
    return HttpResponse(r'<h2>/ / ( . )Y( . ) \ \</h2>')
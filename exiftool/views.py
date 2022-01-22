import imp
import pdb
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from uuid import uuid4

# Create your views here.
def index(request):
    """
    docstring
    """
    return render(request,'exiftool/upload.html')

def handler(request):
    """
    docstring
    """
    uuid = uuid4()

    if request.method == "POST":
        excel = request.POST['excel']
        files = request.FILES.getlist('file')
        import pdb; pdb.set_trace()

    return JsonResponse({

    })
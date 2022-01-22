import imp
import pdb
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from uuid import uuid4
from exiftool.models import Batch

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

        return JsonResponse({
            "batch_id" : f"{uuid}"
        })

def batch(request, uuid=None):
    """
    docstring
    """
    batch = Batch.objects.get(uuid=uuid)
    return render(request,'exiftool/batch.html',{"batch":batch})
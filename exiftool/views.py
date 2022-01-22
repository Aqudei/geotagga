import imp
import pdb
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from uuid import uuid4
from exiftool.models import Batch, Picture

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
        files = [request.FILES[f'file[{i}]'] for i in range(len(request.FILES))]
        excel_file =  list(filter(lambda k: 'sheet' in k.content_type, files))
        if not excel_file or len(excel_file)<=0:
            return
        
        batch = Batch.objects.create(
            uuid=uuid
        )
        batch.excel.save(excel_file[0].name,excel_file[0])

        for f in files:
            if f == excel_file[0]:
                continue

            picture = Picture.objects.create(
                batch=batch
            )
            picture.image.save(f.name,f)
            
        return JsonResponse({
            "batch_id" : f"{uuid}"
        })

def batch(request, uuid=None):
    """
    docstring
    """
    batch = Batch.objects.get(uuid=uuid)
    return render(request,'exiftool/batch.html',{"batch":batch})
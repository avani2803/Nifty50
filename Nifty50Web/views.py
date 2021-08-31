import json
from django.shortcuts import render
from Nifty50.settings import FILE_DIR
from Nifty50Web.util import *

# Create your views here.
def home(request):

    file =  open(FILE_DIR, "r")
    top = json.loads(file.read())
    dict = {"data": top}
    return render(request,"index.html", dict)


    
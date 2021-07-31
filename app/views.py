from django.utils import timezone
from django.shortcuts import render
from time import localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M %p", localtime())
    }

    print(timezone.now(),timezone.localdate()
)
    return render(request,'index.html', context)

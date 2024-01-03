from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def Topics(request):
    if request.method=='POST':
        topic_name=request.POST['tn']
        QLTO=Topic.objects.get_or_create(topic_name=topic_name)[0]
        QLTO.save()

        TO=Topic.objects.all()
        d={'topics':TO}
        return render(request,'display_topic.html',d)
    

    return render(request,'Topic.html')



def Webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
         tn=request.POST['tn']
         nm=request.POST['nm']
         ur=request.POST['ur']
         em=request.POST['em']

         TO=Topic.objects.get(topic_name=tn)
         QLWO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur,email=em)[0]
         QLWO.save()

         WO=Webpage.objects.all()
         d1={'webpages':WO}
 
         return render(request,'display_webpage.html',d1)


    return render(request,'Webpage.html',d)




def Accessrecords(request):
    QLAO=Webpage.objects.all()
    d={'webpages':QLAO}
    if request.method=='POST':
       nm1=request.POST['nm']
       dt=request.POST['dt']
       at=request.POST['at']

       WO=Webpage.objects.get(pk=nm1)
    
       QLAO=Accessrecord.objects.get_or_create(name=WO,Date=dt,author=at)[0]
       QLAO.save()

       AR=Accessrecord.objects.all()
       d1={'accessrecords':AR}

       return render(request,'display_accessrecord.html',d1)

    return render(request,'Accessrecord.html',d)




def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={"topics":QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')  #['c','VB','FB']
        #print(tn)
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)

        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    
    return render(request,'select_multiple_webpage.html',d)


def select_multiple_accessrecord(request):
    QLWO=Webpage.objects.all()
    d1={'webpages':QLWO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')

        QLAO=Accessrecord.objects.none()
        for i in topiclist:
            QLAO=QLAO|Accessrecord.objects.filter(name=i)

        d={'accessrecords':QLAO}
        return render(request,'display_accessrecord.html',d)



    return render(request,'select_multiple_accessrecord.html',d1)




def checkbox(request):
        QLTO=Topic.objects.all()
        d={'topics':QLTO}



        return render(request,'checkbox.html',d)






from django.shortcuts import render,HttpResponse,redirect
from .utilits import open_img,upload_img
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def open(request):
    open_img(request)
    return redirect('/')

def upload(request):
    print(request)
    print(request.FILES)
    fileobj=request.FILES['filepath']
    fs=FileSystemStorage()
    filepathname=fs.save(fileobj.name,fileobj) # name of file and file
    filepathname=fs.url(filepathname)
    #print(type(fileobj.name))
    temp=fileobj.name.split('.')
    new_name=temp[0]+'_new'
    print(new_name)
    img_new=upload_img('.'+filepathname)

    new_path='./media/'+new_name+'.jpeg'
    img_new.save(new_path)
    
    #print(new_path)
    
    #img_new.show()
    context={'filepathname':new_path ,'flag':True }
    return render(request, 'index.html',context)

    
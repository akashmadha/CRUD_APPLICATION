from django.shortcuts import render,redirect
from .models import EmpForm,EMP,IMG,ImgForm
from django.views.generic import DeleteView


# Create your views here.
def index(request):
    return render(request,'index.html')

def eddemp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    
    else:
        f=EmpForm
        context={'form':f}
    return render(request,'eddemployee.html',context)

def emplist(request):
    empl=EMP.objects.all()
    context={'el':empl}
    return render(request,'employee_list.html',context)

class delete(DeleteView):
    model=EMP
    template_name='delete.html'
    success_url='/'
  
def edit(request,eid):
    emp=EMP.objects.get(id=eid)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=emp)
        f.save()
        return redirect('/list')
    
    else:
        f=EmpForm(instance=emp)
        context={'form':f}
    return render(request,'eddemployee.html',context)


def empimg(request):
    if request.method=='POST':
        f=ImgForm(request.POST,request.FILES)
        f.save()
        return redirect('/imgl')
    else:
        f=ImgForm
        context={'form':f}
        return render(request,'imgf.html',context)
    
def imglist(request):
    imgl=IMG.objects.all()
    context={'imgl':imgl}
    return render(request,'imglist.html',context)

class delete_img(DeleteView):
    model = IMG
    success_url =('/imgl')  
    template_name = 'delete_img.html'


from django.shortcuts import render, get_object_or_404, redirect

def edit_img(request, eid):
    product = get_object_or_404(IMG, id=eid)
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/imgl')  # Redirect to detail view after saving
    else:
        form = ImgForm(instance=product)
    
    return render(request, 'imgf.html', {'form': form, 'IMG': product})





# def edit_img(request,eid):
#     emp=IMG.objects.get(id=eid)
#     if request.method=='POST':
#         f=ImgForm(request.POST,instance=emp)
#         f.save()
#         return redirect('/imgl')
    
#     else:
#         f=ImgForm(instance=emp)
#         context={'form':f}
#     return render(request,'imgf.html',context)

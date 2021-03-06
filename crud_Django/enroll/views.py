from .forms import StudentRegistration
from django.shortcuts import render,HttpResponseRedirect
from .models import User

# Create your views here.

#This function will Add new data and show on front-end
def add_show(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm =StudentRegistration()
    else:
        fm =StudentRegistration()
    
    stud=User.objects.all()

    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

#this function update/Edit
def update_data(request,id):
    if request.method == 'POST':
        curr_data= User.objects.get(pk=id)
        fm =StudentRegistration(request.POST,instance=curr_data)
        if fm.is_valid():
            fm.save()
    else:
        curr_data= User.objects.get(pk=id)
        fm =StudentRegistration(instance=curr_data)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#This function will delete data
def delete_data(request,id):
    if(request.method=='POST'):
        curr_data = User.objects.get(pk=id)
        curr_data.delete()
        return HttpResponseRedirect('/')



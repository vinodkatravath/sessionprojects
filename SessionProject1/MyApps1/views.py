

from django.shortcuts import render
# Create your views here.
#Session-Application-1
def page_count_view(request):
 count=request.session.get('count',0)
 newcount=count+1
 request.session['count']=newcount
 print(request.session.get_expiry_age()) #check in server-console
 print(request.session.get_expiry_date())
 return render(request,'MyApps1/pagecount.html',{'count':newcount})



#session-Application-2
from django.shortcuts import render
from MyApps1.forms import *
#Create your views here.
def name_view(request):
 formobj1=NameForm();
 return render(request,'MyApps1/name2.html',{'formobj1':formobj1})
def age_view(request):
 name=request.GET['name']
 request.session['name']=name
 formobj2=AgeForm();
 return render(request,'MyApps1/age2.html',{'formobj2':formobj2})
def parent_view(request):
 age=request.GET['age']
 request.session['age']=age
 formobj3=ParentForm()
 return render(request,'MyApps1/parent2.html',{'formobj3':formobj3})
def result_view(request):
 pname=request.GET['pname']
 request.session['pname']=pname
 return render(request,'MyApps1/results.html')

def add_item_view(request):
 formobj=AddItemForm()
 if request.method=='POST':
  # formobj=AddItemForm(request.POST)
  # formobj.cleaned_data('name')
  name=request.POST['name']
  quantity=request.POST['quantity']
  request.session[name] = quantity
  request.session.set_expiry(30)
  # request.session.set_expiry(0) #expires when browser is closed...
 return render(request, 'MyApps1/additem2.html', {'formobj': formobj})

def display_items_views(request):
  return render(request, 'MyApps1/displayitems.html')
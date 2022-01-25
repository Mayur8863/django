from django.shortcuts import render

# Create your views here.
def home(request):
    # var = {'name':['mayur','name1','mayur1','name2','mayur2','name3','mayur3'],}
    var = {'name':'FALSE'}
    return render(request,'cllg/index.html',var)
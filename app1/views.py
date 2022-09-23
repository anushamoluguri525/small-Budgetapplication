from django.shortcuts import render, redirect

from app1.models import Budget


def showIndex(request):
    return render(request,"index.html")
def addproject(request):
    return render(request,'add_project.html')
def save_project(request):
    pcode = request.POST.get("t1")
    print(pcode)
    pamount= request.POST.get("t2")
    pdate= request.POST.get("t3")
    print(pdate)
    Budget(code=pcode, amount=pamount, month=pdate).save()
    return redirect('addproject')


def viewbudget(request):
    return render(request,"viewbudget.html")


def viewbudget_details(request):
    fromdate = request.POST.get("d1")
    print(fromdate)
    todate = request.POST.get("d2")
    print(todate)
    searchresult = Budget.objects.raw('select id,code,amount,month from budget where month between "'+fromdate+'"and "'+todate+'"')
    #searchresult = Budget.objects.raw('select id,code,amount,month from budget where month between '+fromdate +'"and"'+ todate+'')
    #searchresult = Budget.objects.filter(date_range=["fromdate", "todate"])
    print(searchresult)
    return render(request, "viewbudget.html", {"data": searchresult})
from django.shortcuts import render,redirect
from app1.models import *


# Create your views here.
def show(request):
    return render(request,"index.html")


def adminlogin(request):

    return render(request,"adminlogin.html")


def adminlogincheck(request):
    un=request.POST.get("c1")
    pa=request.POST.get("c2")

    if un == "suresh" and pa == "12345":
        return render(request,"adminhome.html")
    else:
        return render(request,"adminlogin.html",{"error":"invalid details"})


def adminhome(request):
    return render(request,"adminhome.html")


def customerlogin(request):
    return render(request,"customerlogin.html")


def creg(request):
    cna=request.POST.get("t1")
    cadd=request.POST.get("t2")
    cimg=request.FILES["t3"]
    ccont=request.POST.get("t4")
    cpa=request.POST.get("t5")
    CustomerModel(cname=cna,address=cadd,image=cimg,contact=ccont,password=cpa).save()
    return redirect('customerlogin')


def clogincheck(request):
    cn = request.POST.get("c1")
    pa = request.POST.get("c2")

    try:

        res= CustomerModel.objects.get(contact=cn,password=pa)

        request.session['user']=res.cno



        return render(request,"customerhome.html",{"data":res})
    except CustomerModel.DoesNotExist:
        return render(request,"customerlogin.html",{"error":"invalid details"})





def addp(request):
    return render(request,'Addproducts.html',{"data":ProductModel.objects.all()})


def savep(request):
    pna= request.POST.get("t1")
    pprice=request.POST.get("t2")

    pqua=request.POST.get("t4")
    pimg = request.FILES["t3"]
    ProductModel(pname=pna,price=pprice,quantity=pqua,Photo=pimg).save()
    return redirect('addp')


def vpro(request):



    return render(request,"vpro.html",{"data":ProductModel.objects.all()})


def orderp(request):
    pid=request.POST.get("t1")
    cid=request.POST.get("t2")
    print(cid)

    try:
        OrderModel.objects.get(Product_id=pid,Customer_id=cid)
        return render(request,"vpro.html",{"data":ProductModel.objects.all(),"message":"product is already ordered"})
    except OrderModel.DoesNotExist:
        OrderModel(Product_id=pid,Customer_id=cid).save()
        return redirect('corder')


def orders(request):
    res=OrderModel.objects.all()
    return render(request,"order.html",{"data":res})


def corder(request):
    return render(request,"corders.html",{"data":OrderModel.objects.filter(Customer_id=request.session['user'])})
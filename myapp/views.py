from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import (
    login,
    item,
    exercise,
    deficiency,
    blog,
    diet,
    contactus,
    feedback,
    order,
    placeorder,
)
from django.contrib import messages

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def index(request):
    fetchitem = item.objects.all()[0:8]
    print(fetchitem)
    return render(request, "index.html", {"products": fetchitem})


def blogs(request):
    getblog = blog.objects.all()
    print(getblog)
    return render(request, "blog.html", {"blog": getblog})


def exercises(request):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    getexercise = exercise.objects.all().filter(de_id=deffid)
    print(getexercise)
    return render(request, "exercise.html", {"exercises": getexercise})


def loginpage(request):
    return render(request, "registration/login.html")


def vwg(request):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Vegetarian", weight_type="Weight-gain", de_id=deffid
    )[0:3]
    print(fetchdiet)
    return render(request, "weightgain1.html", {"diet": fetchdiet})


def vwgdaywise(request, id):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Vegetarian", weight_type="Weight-gain", de_id=deffid, day=id
    )
    print(fetchdiet)
    return render(request, "weightgain1.html", {"diet": fetchdiet})


def vwl(request):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Vegetarian", weight_type="Weight-loose", de_id=deffid
    )[0:3]
    print(fetchdiet)
    return render(request, "weightloose1.html", {"diet": fetchdiet})


def vwldaywise(request, id):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Vegetarian", weight_type="Weight-loose", de_id=deffid, day=id
    )
    print(fetchdiet)
    return render(request, "weightloose1.html", {"diet": fetchdiet})


def nwg(request):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Non-Vegetarian", weight_type="Weight-gain", de_id=deffid
    )[0:3]
    print(fetchdiet)
    return render(request, "weightgain2.html", {"diet": fetchdiet})


def nwgdaywise(request, id):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Non-Vegetarian", weight_type="Weight-gain", de_id=deffid, day=id
    )
    print(fetchdiet)
    return render(request, "weightgain2.html", {"diet": fetchdiet})


def nwl(request):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Non-Vegetarian", weight_type="Weight-loose", de_id=deffid
    )[0:3]
    print(fetchdiet)
    return render(request, "weightloose2.html", {"diet": fetchdiet})


def nwldaywise(request, id):
    uid = request.session["log_id"]
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(
        food_type="Non-Vegetarian", weight_type="Weight-loose", de_id=deffid, day=id
    )
    print(fetchdiet)
    return render(request, "weightgain2.html", {"diet": fetchdiet})


def products(request):
    getproducts = item.objects.all()[0:6]
    print(getproducts)
    return render(request, "products.html", {"products": getproducts})


def productcatwise(request, id):
    getproducts = item.objects.all().filter(category=id)
    print(getproducts)
    return render(request, "products.html", {"products": getproducts})


def register(request):
    fetchdef = deficiency.objects.all()
    return render(request, "registration/register.html", {"def": fetchdef})


def secblog(request, id):
    fetchblog = blog.objects.get(id=id)
    return render(request, "secblog.html", {"blog": fetchblog})


def single(request, id):
    fetchproduct = item.objects.get(id=id)
    return render(request, "single.html", {"item": fetchproduct})


def weightgain1(request):
    return render(request, "weightgain1.html")


def weightgain2(request):
    return render(request, "weightgain2.html")


def weightloose1(request):
    return render(request, "weightloose1.html")


def weightloose2(request):
    return render(request, "weightloose2.html")


def mailus(request):
    return render(request, "mail.html")


def viewdata(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST.get("gender")
        defid = request.POST.get("Deficiency")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("number")

        logindata = login(
            firstname=firstname,
            lastname=lastname,
            address=address,
            age=age,
            height=height,
            phone_no=phone,
            weight=weight,
            gender=gender,
            de_id=deficiency(id=defid),
            email_id=email,
            password=password,
            role=2,
            status=1,
        )
        logindata.save()
        messages.success(request, "Data Inserted Successfully. you can login now")
        return redirect("login.html")
        # return render(request, 'registration/login.html')
    else:
        messages.error(request, "error occured")
        print("errrorrr")

    return redirect("login.html")
    # return render(request, 'registration/login.html')


def viewblg(request):
    if request.method == "POST":
        uid = request.session["log_id"]
        wr_name = request.POST.get("wr_name")
        b_name = request.POST.get("b_name")
        b_desc1 = request.POST.get("b_desc1")
        b_desc2 = request.POST.get("b_desc2")
        b_media = request.FILES["b_media"]

        blogdata = blog(
            l_id=login(id=uid),
            wr_name=wr_name,
            b_name=b_name,
            b_desc1=b_desc1,
            b_desc2=b_desc2,
            b_media=b_media,
        )
        blogdata.save()
        messages.success(request, "Data Inserted Successfully.")
        return render(request, "blog.html")
    else:
        messages.error(request, "error occured")
        print("errrorrr")

    return render(request, "blog.html")


def checklogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = login.objects.get(email_id=email, password=password)
            request.session["log_user"] = user.email_id
            request.session["log_id"] = user.id
            request.session.save()
            fetchitem = item.objects.all()[0:8]
            print(fetchitem)

        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, "index.html", {"products": fetchitem})

        else:
            messages.info(request, "account does not exit plz sign in")
    return render(request, "index.html")


def logout(request):
    try:
        del request.session["log_user"]
        del request.session["log_id"]
    except:
        pass
    return redirect("login.html")


# Create your views here.
def insertcontact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email_id = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("msg")
        contactdata = contactus(
            name=name, email_id=email_id, subject=subject, message=message
        )
        contactdata.save()
        messages.success(request, "Data Inserted Successfully.")
        return render(request, "mail.html")
    else:
        messages.error(request, "error occured")
        print("errrorrr")

    return render(request, "mail.html")


def insertfeedback(request):
    if request.method == "POST":
        uid = request.session["log_id"]
        review = request.POST.get("star")
        comment = request.POST.get("comment")

        feedbackdata = feedback(l_id=login(id=uid), review=review, comment=comment)
        feedbackdata.save()
        messages.success(request, "Data Inserted Successfully.")
        return render(request, "index.html")
    else:
        messages.error(request, "error occured")
        print("errrorrr")

    return render(request, "index.html")


def addtocart(request, id):
    pid = id
    uid = request.session["log_id"]

    fetchprice = item.objects.get(id=pid)
    price = fetchprice.i_price

    cartdata = order(
        i_id=item(id=pid),
        loginid=login(id=uid),
        o_quantity=1,
        total=price,
        oid=0,
        ostatus=0,
    )
    cartdata.save()
    messages.success(request, "Data Inserted Successfully.")
    return render(request, "index.html")


def deleteproduct(request, id):
    obj = order.objects.get(i_id=id)
    obj.delete()
    uid = request.session["log_id"]
    fetchcart = order.objects.filter(loginid=uid)
    print(fetchcart)
    fetchpid = order.objects.values("i_id").filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    return redirect("checkout.html")
    # return redirect(checkout)


def ucart(request, id):
    num = request.POST.get("qua")
    price = request.POST.get("price")
    q = int(num)
    t = int(price)
    total = q * t
    obj = order.objects.get(i_id=id)
    obj.o_quantity = num
    obj.total = total
    obj.save()
    uid = request.session["log_id"]
    fetchcart = order.objects.filter(loginid=uid)
    print(fetchcart)
    fetchpid = order.objects.values("i_id").filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    return redirect("checkout.html")
    # return redirect(checkout)


def checkout(request):
    uid = request.session["log_id"]
    add = login.objects.filter(id=uid).first()
    nadd = add.address
    print(nadd)
    fetchcart = order.objects.filter(loginid=uid)
    print(fetchcart)
    fetchpid = order.objects.values("i_id").filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    items = order.objects.filter(loginid=uid, ostatus=0).aggregate(Sum("total"))
    print(items)
    return render(
        request,
        "checkout.html",
        {"products": fetchpro, "cart": fetchcart, "login": nadd, "tamount": items},
    )


def placeorders(request):
    uid = request.session["log_id"]
    amount = request.POST.get("tamount")
    query = placeorder(loginid=login(id=uid), tamount=amount)
    query.save()
    flid = placeorder.objects.latest("id")
    items = order.objects.filter(loginid=uid, ostatus=0)
    for obj in items:
        obj.oid = flid
        obj.ostatus = 1
    messages.success(request, "order placed successfully")
    return render(request, "index.html")

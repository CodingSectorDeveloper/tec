from django.shortcuts import render, HttpResponseRedirect
from main.models import *

def index(request):
    branches = 109
    students = 1903
    courses = 32
    return render(request, "Main_admin/home.html", {"branches":branches, "students":students, "courses":courses})

def branch_admins(request):
    branches = BranchAdmin.objects.all()
    return render(request, "Main_admin/branch_admins.html", {"branches":branches})

def zonal_admins(request):
    zonals = ZonalAdmin.objects.all()
    return render(request, "Main_admin/zonal_admins.html", {"zonals":zonals})

def regional_admins(request):
    regionals = RegionalAdmin.objects.all()
    return render(request, "Main_admin/regional_admins.html", {"regionals":regionals})

def create_branch_admin(request):
    zonals = ZonalAdmin.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        location = request.POST['location']
        zonal = request.POST['zonal']
        zonal = ZonalAdmin.objects.filter(pk=zonal).last()

        if " " not in username:
            user = User.objects.create_user(username=username, password=password)
            branch = BranchAdmin.objects.create(name=name, username=username, password=password, location=location, user=user, zonal=zonal)
            user_detail = UserDetails.objects.create(user=user, role="Branch Admin")
            return render(request, "Main_admin/create_branch_admin.html", {"zonals":zonals, "success":True})
        elif User.objects.filter(username=username).exists():
            return render(request, "Main_admin/create_branch_admin.html", {"zonals":zonals, "error":True, "message":"Same Branch already exists"})
        elif BranchAdmin.objects.filter(location=location).exists():
            return render(request, "Main_admin/create_branch_admin.html", {"zonals":zonals, "error":True, "message":"Branch on same location already exists"})
        else:
            return render(request, "Main_admin/create_branch_admin.html", {"error":True, "message":"Username Can't Contain Spaces", "zonals":zonals})


    return render(request, "Main_admin/create_branch_admin.html", {"zonals":zonals})

def create_zonal_admin(request):
    regionals = RegionalAdmin.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        regional = request.POST['regional']
        regional = RegionalAdmin.objects.filter(pk=regional).last()

        if " " not in username:
            user = User.objects.create_user(username=username, password=password)
            zonaladmin = ZonalAdmin.objects.create(name=name, username=username, password=password, regional=regional, user=user)
            user_detail = UserDetails.objects.create(user=user, role="Zonal Admin")
            return render(request, "Main_admin/create_zonal_admin.html", {"regionals":regionals, "success":True})
        elif User.objects.filter(username=username).exists():
            return render(request, "Main_admin/create_zonal_admin.html", {"regionals":regionals, "error":True, "message":"Same Zonal Admin already exists"})
        elif ZonalAdmin.objects.filter(location=location).exists():
            return render(request, "Main_admin/create_zonal_admin.html", {"regionals":regionals, "error":True, "message":"Same Zonal Admin already exists"})
        else:
            return render(request, "Main_admin/create_zonal_admin.html", {"regionals":regionals, "error":True, "message":"Username Can't Contain Spaces"})


    return render(request, "Main_admin/create_zonal_admin.html", {"regionals":regionals})

def create_regional_admin(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']

        if " " not in username:
            user = User.objects.create_user(username=username, password=password)
            regionaladmin = RegionalAdmin.objects.create(name=name, username=username, password=password, user=user)
            user_detail = UserDetails.objects.create(user=user, role="Regional Admin")
            return render(request, "Main_admin/create_regional_admin.html", {"success":True})
        elif User.objects.filter(username=username).exists():
            return render(request, "Main_admin/create_regional_admin.html", {"error":True, "message":"Same Regional Admin already exists"})
        elif RegionalAdmin.objects.filter(location=location).exists():
            return render(request, "Main_admin/create_regional_admin.html", {"error":True, "message":"Same Regional Admin already exists"})
        else:
            return render(request, "Main_admin/create_regional_admin.html", {"error":True, "message":"Username Can't Contain Spaces"})


    return render(request, "Main_admin/create_regional_admin.html")

def delete_branch_admin(request, id):
    BranchAdmin.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/main_admin_dashboard/branch_admins")

def delete_zonal_admin(request, id):
    ZonalAdmin.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/main_admin_dashboard/zonal_admins")

def delete_regional_admin(request, id):
    RegionalAdmin.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/main_admin_dashboard/regional_admins")

def courses(request):
    courses = Course.objects.all()
    return render(request, "Main_admin/courses.html", {"courses":courses})

def create_course(request):
    if request.method == "POST":
        name = request.POST['name']
        addmission_fee = request.POST['addmission_fee']
        monthly_fee = request.POST['monthly_fee']
        registration_fee = request.POST['registration_fee']

        if Course.objects.filter(name=name).exists():
            return render(request, "Main_admin/create_course.html", {"error":True, "message":"Same Course Already Exists"})
        else:
            course = Course.objects.create(name=name, addmission_fee=addmission_fee, monthly_fee=monthly_fee, registration_fee=registration_fee)
            return render(request, "Main_admin/create_course.html", {"success":True})
    return render(request, "Main_admin/create_course.html")

def notice(request):
    notices = Notice.objects.filter(by_admin=True)
    return render(request, "Main_admin/notice.html", {"notices":notices})

def create_notice(request):
    image = None
    video = None
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        if 'image' in request.FILES:
            image = request.FILES['image']
        if 'video' in request.FILES:
            video = request.FILES['video']
        notice = Notice.objects.create(title=title, description=description, image=image, video=video, by_branch=False, by_admin=True)
        return render(request, "Main_admin/create_notice.html", {"success":True})
    return render(request, "Main_admin/create_notice.html")

def material_required(request):
    requirements = MaterialRequisition.objects.all()
    return render(request, "Main_admin/material_required.html", {"requirements":requirements})

def material_entry(request):
    entries = MaterialEntry.objects.all()
    return render(request, "Main_admin/material_entry.html", {"entries":entries})

def student_record_list(request):
    students = Student.objects.all()
    return render(request, "Main_admin/student_record_list.html", {"students":students})

def software(request):
    if request.method == "POST":
        file = request.FILES['file']
        software = Software.objects.create(file=file)
        return render(request, "Main_admin/software.html", {"success":True})
    return render(request, "Main_admin/software.html")

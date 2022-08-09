import datetime
from django.shortcuts import render, HttpResponseRedirect
from main.models import *
import random
import string

def index(request):
    return render(request, "Branch_admin/home.html")

def student_registration(request):
    student_reg_id = ''.join(random.choice(string.digits) for _ in range(10))
    courses = Course.objects.all()
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        father_name = request.POST['father_name']
        dob = request.POST['dob']
        address = request.POST['address']
        student_id = request.POST['id']
        money_paid = request.POST['money_paid']
        course = request.POST['course']
        course = Course.objects.filter(pk=course).last()
        total_fees = (course.monthly_fee*12) + course.addmission_fee + course.registration_fee
        balance = total_fees - int(money_paid)
        branch_admin = BranchAdmin.objects.filter(user=request.user).last()
        no_due = None

        if total_fees < int(money_paid):
            return render(request, "Branch_admin/student_registration.html", {"id":student_reg_id, "courses":courses, "error":True, "message":"'Money Paid' Cannot Be More Than Total Fees Of the Selected Course"})

        student = Student.objects.create(
            first_name=first_name, 
            last_name=last_name,
            father_name=father_name,
            dob=dob,
            course=course,
            address=address,
            money_paid=money_paid,
            balance=balance,
            student_id=student_id,
            branch_admin=branch_admin)
        return render(request, "Branch_admin/student_registration.html", {"courses":courses, "success":True, "id":student_reg_id})

    return render(request, "Branch_admin/student_registration.html", {"courses":courses, "id":student_reg_id})

def student_login_creation(request):
    if request.method == "POST":
        student_id = request.POST['id']
        password = request.POST['password']

        if Student.objects.filter(student_id=student_id).exists():
            user = User.objects.create_user(username=student_id, password=password)
            student = Student.objects.filter(student_id=student_id).last()
            student.password = password
            student.user=user
            student.save()
            return render(request, "Branch_admin/student_login_creation.html", {"success":True})
        else:
            return render(request, "Branch_admin/student_login_creation.html", {"error":True, "message":"Invalid Student Reg. ID !"})

    return render(request, "Branch_admin/student_login_creation.html")

def student_record_list(request):
    branch_admin = BranchAdmin.objects.filter(user=request.user).last()
    print(branch_admin)
    students = Student.objects.filter(branch_admin=branch_admin)
    return render(request, "Branch_admin/student_record_list.html", {"students":students})

def fees_collection(request):
    if request.method == "POST":
        student_id = request.POST['id']
        if not Student.objects.filter(student_id=student_id).exists():
            return render(request, "Branch_admin/fee_collection.html", {"error":True, "message":"Invalid Student Registration ID"})
        else:
            return render(request, "Branch_admin/fee_collection.html", {"success":True, "id":student_id})
    return render(request, "Branch_admin/fee_collection.html")

def fees_collection_2(request, id):
    student = Student.objects.filter(student_id=id).last()
    extra_charge = None
    present = datetime.date.today()
    fine_date = datetime.date(datetime.date.today().year, datetime.date.today().month, 10)
    if fine_date < present:
        extra_days = present - fine_date
        extra_days = extra_days.days
        extra_charge = 5 * extra_days
    else:
        extra_charge = 0
    money_pay = student.course.monthly_fee + extra_charge
    return render(request, "Branch_admin/fee_collection_2.html", {"money_pay":money_pay, "id":id})

def notice(request):
    notices = Notice.objects.filter(by_admin=True)
    notices_by_you = Notice.objects.filter(branch=BranchAdmin.objects.filter(user=request.user).last())
    print(notices)
    print(notices_by_you)
    return render(request, "Branch_admin/notice.html", {"notices":notices, "notices_by_you":notices_by_you})

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
        branch = BranchAdmin.objects.filter(user=request.user).last()
        notice = Notice.objects.create(title=title, description=description, image=image, video=video, by_branch=True, by_admin=False, branch=branch)
        return render(request, "Branch_admin/create_notice.html", {"success":True})
    return render(request, "Branch_admin/create_notice.html")

def material_entry(request):
    if request.method == "POST":
        student_id = request.POST['id']
        bag = request.POST['bag']
        pen = request.POST['pen']
        uniform = request.POST['uniform']
        id_card = request.POST['id_card']

        entry = MaterialEntry.objects.create(student_id=student_id, bag=bag, pen=pen,uniform=uniform, id_card=id_card)
        return render(request, "Branch_admin/material_entry.html", {"success":True})
    return render(request, "Branch_admin/material_entry.html")

def material_requisition(request):
    if request.method == "POST":
        branch = BranchAdmin.objects.filter(user=request.user).last()
        bag = request.POST['bag']
        pen = request.POST['pen']
        uniform = request.POST['uniform']
        id_card = request.POST['id_card']
        
        requisiton = MaterialRequisition.objects.create(branch=branch, bag=bag, pen=pen, uniform=uniform, id_card=id_card)
        return render(request, "Branch_admin/material_requisiton.html", {"success":True})
    return render(request, "Branch_admin/material_requisiton.html")

def paid(request,id,money):
    student = Student.objects.filter(student_id=id).last()
    student.balance = student.balance - int(money)
    student.save()
    return HttpResponseRedirect("/branch_admin_dashboard")

def enquiry(request):
    if request.method == "POST":
        branch = BranchAdmin.objects.filter(user=request.user).last()
        details = request.POST['details']
        status = request.POST['status']

        enquiry = Enquiry.objects.create(branch=branch, details=details, status=status)
        return render(request, "Branch_admin/enquiry.html", {"success":True})
    return render(request, "Branch_admin/enquiry.html")

def crf(request):
    courses = Course.objects.all()
    if request.method == "POST":
        student_name = request.POST['student_name']
        father_name = request.POST['father_name']
        student_id = request.POST['id']
        date_of_admission = request.POST['date_of_admission']
        date_of_completion = request.POST['date_of_completion']
        course = request.POST['course']
        course = Course.objects.filter(id=course).last()
        payment_done = request.POST['payment_done']

        if CRF.objects.filter(student_name=student_name).exists():
            return render(request, "Branch_admin/crf.html", {"courses":courses, "error":True, "message":"Same Student's CRF Exists"})
        else: 
            crf = CRF.objects.create(student_name=student_name, father_name=father_name, student_id=student_id, date_of_admission=date_of_admission, date_of_completion=date_of_completion, course_completed=course, payment_done=payment_done)
            return render(request, "Branch_admin/crf.html", {"courses":courses, "success":True})

    return render(request, "Branch_admin/crf.html", {"courses":courses})

def prf(request):
    courses = Course.objects.all()
    if request.method == "POST":
        student_name = request.POST['student_name']
        project_done = request.POST['project_done']
        course = request.POST['course']
        course = Course.objects.filter(id=course).last()
        payment_cleared = request.POST['payment_cleared']

        if PRF.objects.filter(student_name=student_name).exists():
            return render(request, "Branch_admin/prf.html", {"courses":courses, "error":True, "message":"Same Student's PRF Exists"})
        else: 
            prf = PRF.objects.create(student_name=student_name, project_done=project_done, course=course, payment_cleared=payment_cleared)
            return render(request, "Branch_admin/prf.html", {"courses":courses, "success":True})

    return render(request, "Branch_admin/prf.html", {"courses":courses})

def download(request):
    softwares = Software.objects.all()
    return render(request, "Branch_admin/download.html", {"softwares":softwares})
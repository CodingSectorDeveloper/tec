from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.TextField(blank=False)

class Course(models.Model):
    name = models.TextField(blank=False)
    addmission_fee = models.IntegerField(blank=False)
    registration_fee = models.IntegerField(blank=False, default=1000)
    monthly_fee = models.IntegerField(blank=False)

    def return_total_fees(self):
        return self.addmission_fee + self.registration_fee + (self.monthly_fee*12)

class SubAdmin(models.Model):
    name = models.TextField(blank=False)
    password = models.TextField(blank=False)
    role = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class MidAdmin(models.Model):
    name = models.TextField(blank=False)
    password = models.TextField(blank=False)
    location = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class RegionalAdmin(models.Model):
    name = models.TextField(blank=False)
    username = models.TextField(blank=False, default="User345")
    password = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ZonalAdmin(models.Model):
    name = models.TextField(blank=False)
    username = models.TextField(blank=False, default="User345")
    password = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regional = models.ForeignKey(RegionalAdmin, on_delete=models.CASCADE)

class BranchAdmin(models.Model):
    name = models.TextField(blank=False)
    username = models.TextField(blank=False, default="User345")
    password = models.TextField(blank=False)
    location = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zonal = models.ForeignKey(ZonalAdmin, on_delete=models.CASCADE)

class Student(models.Model):
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    password = models.TextField(blank=True, null=True)
    father_name = models.TextField(blank=False)
    dob = models.DateField(blank=False)
    address = models.TextField(blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    money_paid = models.IntegerField(blank=False)
    balance = models.IntegerField(default=0)
    student_id = models.IntegerField(blank=False)
    branch_admin = models.ForeignKey(BranchAdmin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class Notice(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    video = models.FileField(blank=True, null=True, upload_to="notice_video/")
    image = models.ImageField(blank=True, null=True, upload_to="notice_image/")
    by_admin = models.BooleanField()
    by_branch = models.BooleanField()
    branch = models.ForeignKey(BranchAdmin, on_delete=models.CASCADE, blank=True, null=True)

class MaterialEntry(models.Model):
    student_id = models.IntegerField()
    bag = models.IntegerField()
    uniform = models.IntegerField()
    pen = models.IntegerField()
    id_card = models.IntegerField()

class MaterialRequisition(models.Model):
    branch = models.ForeignKey(BranchAdmin, on_delete=models.CASCADE)
    bag = models.IntegerField()
    pen = models.IntegerField()
    id_card = models.IntegerField()
    uniform = models.IntegerField()
    date_issued = models.DateField(auto_now_add=True)

class Enquiry(models.Model):
    branch = models.ForeignKey(BranchAdmin, on_delete=models.CASCADE)
    details = models.TextField()
    status = models.DateField()

class PRF(models.Model):
    student_name = models.TextField()
    project_done = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment_cleared = models.BooleanField(default=True)

class CRF(models.Model):
    student_name = models.TextField()
    father_name = models.TextField()
    student_id = models.IntegerField()
    payment_done = models.BooleanField(default=True)
    course_completed = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_admission = models.DateField()
    date_of_completion = models.DateField()

class Software(models.Model):
    file = models.FileField(upload_to='software/')
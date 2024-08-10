from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from MainApp import models, forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User


@login_required(login_url='login')
def dash(request):
    user_obj = models.Staff.objects.filter(id=request.user.id).first()

    attendance = models.Attendance.objects.all().order_by('-date')

    context = {
        'users': user_obj,
        'attendances': attendance
    }
    return render(request, "dash/dash.html", context)


@login_required(login_url='login')
def accounts(request):

    user_obj = get_object_or_404(User, id=request.user.id)

    return render(request, "dash/accounts.html", {'users':user_obj})

@login_required(login_url='login')
def security(request):
    return render(request, "dash/security.html")

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                return render(request, "dash/login.html", {"message": "Invalid username or password"})
        else:
            return render(request, "dash/login.html", {"message": "Username and password are required"})

    return render(request, 'dash/login.html')



def logout_view(request):
    logout(request)
    return render(request, "dash/logout.html")


@login_required
def create_staff(request):
    if request.method == 'POST':
        form = forms.CreateStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash')  # Replace with your success URL
    else:
        form = forms.CreateStaffForm()

    return render(request, 'dash/register_staff.html', {'form': form})

@login_required(login_url='login')
def create_attendance(request):
    form = forms.AttendanceForm()
    if request.method == 'POST':
        form = forms.AttendanceForm(request.POST)
        if form.is_valid():
            form.save()



        return redirect('dash')



    return render(request, 'dash/attendance.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user

        try:
            staff = models.Staff.objects.get(user_name=user.username)
        except ObjectDoesNotExist:
            return redirect('accounts')


        if 'profile_pic' in request.FILES:
            staff.profile_pic = request.FILES['profile_pic']

        staff.full_name = request.POST.get('full_name')
        staff.email = request.POST.get('email')
        staff.organization = request.POST.get('organization')
        staff.ph_number = request.POST.get('phone')
        staff.address = request.POST.get('address')
        staff.region = request.POST.get('state')
        staff.country = request.POST.get('zip_code')

        staff.save()

        return redirect('accounts')

    return render(request, 'accounts.html')


@login_required
def update_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current-password')
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-password')

        if not request.user.check_password(current_password):
            return render(request, 'dash/security.html', {'message':'Current password is incorrect.'})

        if new_password != confirm_password:
            return render(request, 'dash/security.html',{'message':'New passwords do not match.'})

        request.user.set_password(new_password)
        request.user.save()

        update_session_auth_hash(request, request.user)

        return render(request, 'dash/security.html',{'message':'Your password has been changed successfully.'})

    return render(request, 'dash/security.html')


def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(models.Attendance, id=attendance_id)
    attendance.delete()
    return redirect('dash')

def edit_attendance(request, attendance_id):
    attendance = get_object_or_404(models.Attendance, id=attendance_id)

    if request.method == 'POST':
        form = forms.AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        form = forms.AttendanceForm(instance=attendance)

    return render(request, 'dash/edit_attendance.html', {'form': form, 'attendance': attendance})


@login_required(login_url='login')
def list(request):

    staff = models.Staff.objects.all()

    context = {
        'staffs': staff,

    }
    return render(request, "dash/list.html", context)

def delete_staff(request, staff_id):
    staff = get_object_or_404(models.Staff, id=staff_id)
    if request.method == 'POST':
        staff.delete()
        return redirect('list')

def edit_staff(request, staff_id):
    staff = get_object_or_404(models.Staff, id=staff_id)
    if request.method == 'POST':
        form = forms.StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = forms.StaffForm(instance=staff)
    return render(request, 'dash/edit_attendance.html', {'form': form})


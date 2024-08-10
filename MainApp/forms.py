from django import forms
from .models import Attendance, Staff

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['staff', 'date', 'present']


class CreateStaffForm(forms.ModelForm):
    login_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Staff
        fields = [
            'full_name', 'user_name', 'email', 'organization',
            'ph_number', 'address', 'region', 'country',
            'profile_pic', 'super_staff'
        ]

    def save(self, commit=True):
        staff = super().save(commit=False)
        if self.cleaned_data['login_password']:
            staff.login_password = self.cleaned_data['login_password']
        else:
            staff.set_password(self.cleaned_data[
                                   'login_password'])  # Assuming set_password method is in Staff model or use save method to generate it.

        if commit:
            staff.save()
        return staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['full_name', 'user_name', 'email', 'organization', 'ph_number', 'region', 'country']

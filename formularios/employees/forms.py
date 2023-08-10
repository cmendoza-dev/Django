from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all___'
        # exclude = ('email',) no incluir un campo en el formulario





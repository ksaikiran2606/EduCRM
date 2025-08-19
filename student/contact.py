class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # This will include 'contact'
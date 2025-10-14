from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
def index(request):
    return render(request,'index.html')

def student_list(request):
    object=Student.objects.all()
    return render(request,"student_list.html",{'student':object})

def student_create(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        course=request.POST.get('course')
        Student.objects.create(name=name,email=email,course=course)
        return redirect('student_list')

    return render(request,"student_form.html")

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student})

def student_delete(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect("student_list")
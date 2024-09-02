from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Addcourse, Student, Teacher
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"home.html")



# def user_signup(request):
#     return render(request,"signup.html")

# def admin_dashboard(request):
#     return render(request,"admin_dashboard.html")

# def add_course(request):
#     return render(request,"add_course.html")

# def add_student(request):
#     return render(request,"add_student.html")

# def show_teachers(request):
#     return render(request,"show_teachers.html")



# def show_students(request):
#     return render(request,"show_students.html")

# def edit_student(request):
#     return render(request,"edit_student.html")


# def edit_teacher_profile(request):
#     return render(request,"edit_teacher_profile.html")

# def view_teacher_profile(request):
#     return render(request,"view_teacher_profile.html")



def adminlogin(request):                             ######user_auth username and password and also for teacher admin##
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                login(request, user)
                
                return redirect('teacher_dashboard')
        else:
            messages.info(request, 'Invalid username & password')
            return redirect('home')
    
    return render(request, 'home.html')
                



@login_required(login_url='home')                #Dashboard 
def admin_dashboard(request):
    return render(request,"admin_dashboard.html")                           



@login_required(login_url='home')                  # add course in admin dashboard 
def add_course(request):
    if request.method=="POST":
        name=request.POST['name']
        fee=request.POST['fee']
        Addcourse.objects.create(coursename=name,coursefee=fee)
        return redirect('add_course')
    return render(request,'add_course.html') 


@login_required(login_url='home')        # add student in admin dashboard 
def add_student(request):
    courses = Addcourse.objects.all()
    if request.method=="POST":
        name=request.POST["name"]
        address=request.POST["address"]
        age=request.POST["age"]
        dob=request.POST["dateofbirth"]
        course_id=request.POST['course']
        course=Addcourse.objects.filter(id=course_id).first()          

        if course:
            Student.objects.create(stdname=name,address=address,
                                   age=age,date=dob,course=course)
            return redirect('add_student')
    return render(request,'add_student.html',{'courses':courses}) 




@login_required(login_url='home')                     # show students in admin dashboard                                 
def show_std_details(request):
    std=Student.objects.all() 
    return render(request,'show_students.html',{'students':std})   


@login_required(login_url='home')           #edit students in admin dashboard 
def edit_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student:
        courses = Addcourse.objects.all()
        if request.method == 'POST':
            student.stdname = request.POST['name']
            student.address = request.POST['address']
            student.age = request.POST['age']
            student.date = request.POST['date_of_birth']
            course_id = request.POST['course']
            course = Addcourse.objects.filter(id=course_id).first()
            if course:
                student.course = course
                student.save()
                return redirect('show_std_details')
        return render(request, 'edit_student.html', {'student': student, 'courses': courses})
    return redirect('show_std_details')



@login_required(login_url='home')               #delete students in admin dashboard 
def delete_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student:
        student.delete()
    return redirect('show_std_details')






@login_required(login_url='home')                        # show teachers in admin dashboard              
def show_tch_details(request):
    tech=Teacher.objects.all()
    return render(request,'show_teachers.html',{'tea':tech})



@login_required(login_url='home')                         #logout in admin dashboard
def logout(request):                        
    auth.logout(request)
    return redirect('home')



def register(request):                                       #teacher registration is done 
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        pwd = request.POST['password']
        cpwd = request.POST['confirm_password']
        email = request.POST['email']
        add = request.POST['address']
        age = request.POST['age']
        num = request.POST['contact_number']
        course_id = request.POST['course']
        img = request.FILES['photo']

        if pwd == cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "This username already exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pwd,
                    email=email,
                )
                course = Addcourse.objects.get(id=course_id)
                teacher = Teacher(
                    user=user,
                    course=course,
                    address=add,
                    age=age,
                    contact=num,
                    img=img
                )
                teacher.save()
                return redirect('home')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('signup')
    else:
        return redirect('signup')



@login_required(login_url='home')
def show_teachers(request):
    teacher=Teacher.objects.all()
    return render(request,'show_teachers.html',{'th':teacher})



@login_required(login_url='home')
def delete_teacher(request, id):
    teacher = Teacher.objects.filter(id=id).first()
    
    if teacher:
        user = teacher.user
        teacher.delete()
        if user:
            user.delete()
        messages.success(request, "Teacher deleted successfully.")
    else:
        messages.error(request, "Teacher does not exist.")
    return redirect('show_teachers')






def signup(request):
    course=Addcourse.objects.all()
    return render(request,'signup.html',{'crs':course})





@login_required(login_url='home')
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')




@login_required(login_url='home')
def view_teacher_detail(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'view_teacher_detail.html', {'teacher': teacher})





@login_required(login_url='home')
def edit_teacher_detail(request):
    teacher = Teacher.objects.get(user=request.user)
    user = teacher.user

    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['username']
        
        user.email = request.POST['email']
        user.save()

        teacher.address = request.POST['address']
        teacher.age = request.POST['age']
        teacher.contact = request.POST['contact']
        
        if 'course' in request.POST:
            teacher.course_id = request.POST['course']  
        
        if 'img' in request.FILES:
            teacher.img = request.FILES['img']
            
        teacher.save()

        return redirect('view_teacher_detail')

    courses = Addcourse.objects.all()  
    
    return render(request, 'edit_teacher_detail.html', {'teacher': teacher, 'courses': courses})


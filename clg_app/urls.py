from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminlogin', views.adminlogin, name='adminlogin'),

    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),

    path('add_course', views.add_course, name='add_course'),                                  #on admin dashboard                                    
    path('add_student', views.add_student, name='add_student'),                         #on admin dashboard 
    path('show_std_details', views.show_std_details, name='show_std_details'),      #on admin dashboard
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),                      #on admin dashboard--------> edit in show_std_details
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),             #on admin dashboard--------> delete in show_std_details

    

    path('logout', views.logout, name='logout'),        # logout from dashboard 

    path('register', views.register, name='register'),  #teacher registration signup function is added

    path('signup', views.signup, name='signup'),        #teacher registration signup page

    path('show_teachers', views.show_teachers, name='show_teachers'), # show teachers list on admin panel

    path('delete_teacher/<int:id>', views.delete_teacher, name='delete_teacher'),

    path('teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),

    path('view_teacher_detail', views.view_teacher_detail, name='view_teacher_detail'),

    path('edit_teacher_detail', views.edit_teacher_detail, name='edit_teacher_detail'),
    

    

    

    # path('show_teachers', views.show_teachers, name='show_teachers'),
    # path('show_students', views.show_students, name='show_students'),
    # path('edit_student', views.edit_student, name='edit_student'),
    # path('edit_teacher_profile', views.edit_teacher_profile, name='edit_teacher_profile'),
    # path('view_teacher_profile', views.view_teacher_profile, name='view_teacher_profile'),   
]

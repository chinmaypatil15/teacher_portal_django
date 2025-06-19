
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q, Avg, Count
from .models import Student
from .forms import StudentForm, CustomLoginForm


def login_view(request):
    """Handle user login"""
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
    else:
        form = CustomLoginForm()
    
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    """Handle user logout"""
    username = request.user.username
    logout(request)
    messages.success(request, f'Goodbye, {username}! You have been logged out.')
    return redirect('login')


def register_view(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})


@login_required
def dashboard_view(request):
    """Dashboard view with student statistics"""
    # Get search query
    search_query = request.GET.get('search', '')
    
    # Filter students based on search
    students = Student.objects.all()
    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) | 
            Q(subject__icontains=search_query)
        )
    
    # Calculate statistics
    total_students = Student.objects.count()
    avg_marks = Student.objects.aggregate(Avg('marks'))['marks__avg'] or 0
    subjects_count = Student.objects.values('subject').distinct().count()
    
    # Get top performers
    top_students = Student.objects.order_by('-marks')[:5]
    
    context = {
        'students': students,
        'search_query': search_query,
        'total_students': total_students,
        'avg_marks': round(avg_marks, 2),
        'subjects_count': subjects_count,
        'top_students': top_students,
    }
    
    return render(request, 'auth/dashboard.html', context)


@login_required
def add_student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].strip()
            subject = form.cleaned_data['subject'].strip()
            marks = form.cleaned_data['marks']

            # Check for existing student
            existing_student = Student.objects.filter(
                name__iexact=name,
                subject__iexact=subject
            ).first()

            if existing_student:
                existing_student.marks += marks
                existing_student.save()
                messages.success(request, f"{name}'s marks updated to {existing_student.marks}.")
            else:
                form.save()
                messages.success(request, f"{name} added successfully.")

            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()

    return render(request, 'auth/add_student.html', {'form': form})



@login_required
def edit_student_view(request, student_id):
    """Edit existing student"""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'auth/edit_student.html', {'form': form, 'student': student})


@login_required
def delete_student_view(request, student_id):
    """Delete student"""
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student_name = student.name
        student.delete()
        messages.success(request, f'Student {student_name} deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'auth/delete_student.html', {'student': student})


@login_required
def profile_view(request):
    """User profile view"""
    return render(request, 'auth/profile.html')

from django.shortcuts import render


def courses_list(request, *args, **kwargs):
    courses = [
        'Languages',
        'Makeup',
        'IT'
    ]
    return render(request, 'courses/courses_list.html', {'app_courses': courses})


def courses_info(request, *args, **kwargs):
    return render(request, 'courses/courses_info.html', {})

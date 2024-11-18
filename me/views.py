from django.shortcuts import render


def portfolio(request):
    skills = [
        {'name': 'C', 'level': 80},
        {'name': 'C++', 'level': 75},
        {'name': 'Python', 'level': 80},
        {'name': 'Django', 'level': 90},
        {'name': 'JavaScript', 'level': 80},
        {'name': 'Jquery', 'level': 90},
        {'name': 'React.js', 'level': 90},
        {'name': 'SQL', 'level': 85},
        {'name': 'HTML', 'level': 100},
        {'name': 'CSS', 'level': 95},
        {'name': 'Linux', 'level': 90},
        {'name': 'Bash', 'level': 80},
        {'name': 'Git/GitHub/GitLab', 'level': 90},
    ]

    languages = [{'name': 'Haitian Creole', 'level': 100},
        {'name': 'French', 'level': 100},
        {'name': 'English', 'level': 95},
        {'name': 'Russian', 'level': 85},
        {'name': 'Spanish', 'level': 70},
    ]
    return render(request, 'me/portfolio.html', {'skills': skills, 'languages': languages})

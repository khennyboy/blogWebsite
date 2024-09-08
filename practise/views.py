from django.shortcuts import render
from .models import Person, City, Student, Course, User, Profile, Musician, Group, Membership, Supplier, Place

def index(request):
    city = City.objects.get(id=1)
    #this is used to get all the people in that city
    people_in_city = city.person_set.all()  
    print(people_in_city)

    # Get all courses a student is enrolled in
    student = Student.objects.get(id=1)
    courses = student.courses.all()
    print(courses)

    # Get all students enrolled in a course
    course = Course.objects.get(id=1)
    students_in_course = course.student_set.all()
    for student in students_in_course:
        print(student)

    username = User.objects.get(id=1)
    print(username.profile.bio)

    profile = Profile.objects.get(id=1)
    print(profile.user.username)

    musician = Musician.objects.get(name='pasuma')
    groups_of_musician = musician.group_set.all()
    print(groups_of_musician)

    group = Group.objects.get(name='abiyamo')
    memberships = Membership.objects.filter(group=group)
    print(memberships)

    musician = Musician.objects.get(name='pasuma')
    memberships = Membership.objects.filter(person=musician)
    print(memberships)
    
    supplier_details = Supplier.objects.get(id =2)
    print(supplier_details.name)

    company_place = Place.objects.get(id =2)
    print(company_place.providers.all())


    return render(request, 'index.html', {
        'profiles': Person.objects.all()
    })
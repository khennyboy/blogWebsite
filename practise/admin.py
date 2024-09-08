from django.contrib import admin
from .models import City, Person, Student, Course, User, Profile, Group, Musician, Membership, Place, Supplier, PersonProxy, MyPersonProxy

admin.site.register(City)
admin.site.register(Course)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Musician)
admin.site.register(Place)
admin.site.register(Supplier)
admin.site.register(PersonProxy)
admin.site.register(MyPersonProxy)

class PersonAdmin(admin.ModelAdmin):
    list_display =['name', 'city']
admin.site.register(Person, PersonAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display =['name']
admin.site.register(Student, StudentAdmin)

class MembershipAdmin(admin.ModelAdmin):
    list_display =['group', 'person']
admin.site.register(Membership, MembershipAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display =['name', 'slug']
admin.site.register(Group, GroupAdmin)

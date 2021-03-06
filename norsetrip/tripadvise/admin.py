from django.contrib import admin

# Register your models here.
from .models import Lodge
from .models import Course
from .models import Course_Lodge_Assignment
from .models import User
from .models import Review
from .models import Course_Assignment

#admin.site.register(Lodging)
class LodgeAdmin(admin.ModelAdmin):
	#fields = ["lodge_name", "Lodge_address", "City", "Country", "Pub_date" ]
	list_display = ("lodgeId","lodge_name","country","average_rating");
	list_filter = ['country']
	search_fields = ['city']
	list_per_page = 50 #pagination

admin.site.register(Lodge, LodgeAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ("courseId",'name','dept', 'term')
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 50
admin.site.register(Course, CourseAdmin)

class Course_Lodge_AssignmentAdmin(admin.ModelAdmin):
	list_display = ('lodgeAssignId','course_Id','lodge_Id')
	list_filter = ['course_Id']
	search_fields = ['course_Id']
	
admin.site.register(Course_Lodge_Assignment, Course_Lodge_AssignmentAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display = ('userId','email','role')
admin.site.register(User, UserAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('reviewId','lodge_Id','user_Id','rating','cost','pub_date')
admin.site.register(Review, ReviewAdmin)

class Course_AssignmentAdmin(admin.ModelAdmin):
	list_display = ('courseAssignId','course_Id','user_Id')
admin.site.register(Course_Assignment, Course_AssignmentAdmin)

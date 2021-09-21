from django.urls import path



from courses.includes.semesterList import (
    semester_list,
)
from courses.includes.moduleList import (
    module_list,
)
from courses.includes.courseList import (
    course_list,

)

# app_name = "courses"

urlpatterns = [
    path('<filier>/',semester_list, name='front-semester-list'),
    path('<filier>/<semester>/',module_list, name='front-module-list'),
    path('<filier>/<semester>/<modl>/',course_list, name='front-course-list'),
 
]
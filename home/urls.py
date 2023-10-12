from django.urls import path , include

from .views import *

urlpatterns = [

  path('',get_student),
  path('post-student/',post_student),
  path('put-student/<id>',put_student),
  path('patch-student/<id>',patch_student),
  path('delete-student/<id>',delete_student),
  path('get-book', get_book),
  
  path('student/',studentapi.as_view()),



  path('register/',registeruser.as_view()),

]

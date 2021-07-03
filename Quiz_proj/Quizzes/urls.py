from django.urls import path
from .views import QuizListView,quiz_view,quiz_data_view,save_data,result_view,createquiz
app_name='Quizzes'
urlpatterns=[
    path('',QuizListView.as_view(),name='main_view'),
     path('create',createquiz,name='create-view'),
    path('<pk>',quiz_view,name='quiz_view'),
    path('<pk>/data',quiz_data_view,name='quiz_data-view'),
    path('<pk>/save',save_data,name='save_data'),
    path('<pk>/<score>/result/',result_view,name='result'),


    
    ]
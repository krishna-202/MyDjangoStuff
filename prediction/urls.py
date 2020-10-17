from django.urls import path
from prediction import views

app_name='prediction'

urlpatterns = [
    path('appointment',views.make_appointment,name='make_appointment'),
    path('milage',views.mpg,name='mpg'),
    path('milage_prediction',views.milage_prediction,name='milage_prediction'),
    path('loan_prediction',views.loan_prediction,name='loan_prediction'),
    path('loan_predicted',views.loan_predicted,name='loan_predicted'),

]

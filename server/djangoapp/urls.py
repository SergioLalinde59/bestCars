# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [    # # path for registration    # path for login    path(route='login', view=views.login_user, name='login'),
    path(route='djangoapp/login', view=views.login_user, name='login_alternative'),
    path(route='api/login', view=views.login_user, name='api_login'),
    path('logout', views.logout_request, name='logout'),
    path('api/logout', views.logout_request, name='api_logout'),
    path('djangoapp/logout', views.logout_request, name='legacy_logout'),
    path('register', views.registration, name='register'),
    path('api/register', views.registration, name='api_register'),
    path(route='getcars', view=views.get_cars, name ='getcars'),

    # path for dealer reviews view
    path(route='get_dealers/', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_reviews'),
    path(route='add_review', view=views.add_review, name='add_review'),

    # path for add a review view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from main_page import views

app_name = 'main_page'

urlpatterns = [
    path('', views.index, name='category-name'),
    path('right_holders/', views.right_holders),
    path('how_to_get/', views.how_to_get),
    path('how_to_order/', views.how_to_order),
    # path('view_all_document/', views.view_all_document),
    path('populating_the_database/', views.populating_the_database),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<cat>/', views.about_cat),
    path('<cat>/<doc>', views.about_doc),
]

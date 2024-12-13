from django.contrib import admin
from django.urls import path
from task2.views import func_view, ClassView
from task3.views import home_view, store_view, cart_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', ClassView.as_view()),
    path('', func_view),  # Корневой маршрут
    path('functional/', func_view),  # Новый маршрут для /functional/
    path('home/', home_view),
    path('store/', store_view),
    path('cart/', cart_view),
]

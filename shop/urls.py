from django.contrib import admin
from django.urls import path
from store.views import add_to_cart, index, product_detail, cart, delete_cart, remove_from_cart
from accounts.views import login_user, logout_user, signup 
from django.conf.urls.static import static
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup, name="signup"),
    path('logout/',logout_user, name="logout"),
    path('login/',login_user, name="login"),
    path('cart/',cart, name="cart"),
    path('cart/delete',delete_cart, name="delete-cart"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
    path('cart/remove/<int:order_id>/', remove_from_cart, name="remove-from-cart"),
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

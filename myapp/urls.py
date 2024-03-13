from django.urls import path
from .views import ContactView, UserLoginView, UserSignupView, HomeView, logout_view, AboutView, ShopView, ProductDetailView, UpdateProfileView, CartView, AddToCartView, delete_from_cart, UpdateCartItemView, order_payment, callback

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact", ContactView.as_view(), name="contact"),
    path("login", UserLoginView.as_view(), name="login"),
    path("signup/", UserSignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
    path("about", AboutView.as_view(), name="about"),
    path("shop", ShopView.as_view(), name='shop'),
    path("product/<slug:slug>", ProductDetailView.as_view(),
         name="product-detail-page"),
    path("profile/update/", UpdateProfileView.as_view(), name="update-profile"),
    path("cart", CartView.as_view(), name="cart" ),
    path("add-to-cart/", AddToCartView.as_view(), name="add-to-cart"),
    path("cart/<int:pk>/", delete_from_cart, name="delete-from-cart" ),
    path("update-cart-item/<int:id>", UpdateCartItemView.as_view(), name="update-cart-item"),
    path("payment/", order_payment, name="payment" ),
    path("callback/", callback, name="callback" )
]

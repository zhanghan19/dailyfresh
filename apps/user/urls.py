from django.urls import path
from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from user import views

urlpatterns = [
    # path('register', views.register, name='register'),  # 注册
    # url(r'^register_handle$', views.register_handle, name='register_handle')

    path('register', RegisterView.as_view(), name='register'),
    url(r'active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    path('login', LoginView.as_view(), name='login'),  # 登录
    path('logout', LogoutView.as_view(), name='logout'),  # 登录
    path('', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    path('order', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    path('address', AddressView.as_view(), name='address'),  # 用户中心地址页
]

from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # path('admin_home',views.admin_home,name="admin"),
    path('home',views.home,name="home"),
    path('products/<str:name>',views.products,name="pro"),
    path('items/<str:name>',views.allitems,name="items1"),
    path('details/<str:name>',views.detail,name="det"),
    path('reg',views.reg,name="reg"),
    path('lo',views.loginpage,name='lo'),
    path('log',views.logoutpage,name='log'),
    path('search',views.search,name="items"),
    path('add_to_cart/<str:name>',views.addcart,name="add"),
    path('viewcart',views.viewcart,name="cart"),
    path('reject/<int:id>',views.rejectcart,name="reject"),
    path('add_category',views.add_category.as_view(),name="add_cat"),
    path('add_product',views.add_product.as_view(),name="add_pro"),
    path('add_items',views.add_items.as_view(),name="add_items"),
    path('edit_pro/<str:name>',views.up_pro,name="edit_pro"),
    path('del_pro/<str:name>',views.pro_delete,name="del"),
    path('view_product',views.view_product,name="view_pro"),
    path('edit_cat/<str:name>',views.up_category,name="edit_cat"),
    path('del_cat/<str:name>',views.cat_delete,name="del_cat"),
    path('view_category',views.view_category,name="view_cat"),
    path('edit_items/<str:name>',views.up_items,name="edit_items"),
    path('del_items/<str:name>',views.items_delete,name="del_item"),
    path('view_items',views.view_items,name="view_items"),
    path('about',views.about,name="about"),
    path('add_to_wish/<str:name>',views.add_to_wish,name="wish"),
    path('viewwish',views.wishlist,name="wishlist"),
    path('rejectwish/<int:id>',views.rejectwish,name="rejectwish"),
    # path('placed',views.placed,name="placed"),
    # path('bill',views.bill,name="bill"),
    path('payment',views.payment,name="payment"),
    path('orders',views.order_list,name="orders"),
    path('placeorder',views.placeorder,name="placeorder")
    

    



    
]

urlpatterns+=static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

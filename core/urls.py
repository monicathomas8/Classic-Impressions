from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),                  # Home page
    path('about/', views.about, name='about'),          # About page
    path('faq/', views.faq, name='faq'),                # FAQ page
    path(
        'insallation/', views.installation, name='installation'
    ),  # Installation guide
    path('accounts/', include('accounts.urls')),         # User accounts
    path('admin/', admin.site.urls),                     # Admin site
    path("orders/", include("orders.urls")),             # Order management
    path('products/', include('catalogue.urls')),        # Product catalogue
    path('cart/', include('cart.urls')),                 # Shopping cart
    path('contact/', include('contact.urls')),           # Contact form
    path('custom-services/', include('requests.urls')),  # Custom service
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

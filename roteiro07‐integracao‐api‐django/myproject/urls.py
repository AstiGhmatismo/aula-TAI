"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# ... urlpatterns com include("alunos.urls") ...

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.pagina_inicial, name="pagina_inicial"),
    path("api/alunos", views.api_alunos, name="api_alunos"),
    path("api/alunos/<int:aluno_id>", views.remover_aluno, name="remover_aluno")
    
]
if settings.DEBUG and settings.STATICFILES_DIRS:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATICFILES_DIRS[0],
)
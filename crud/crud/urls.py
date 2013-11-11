from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'principal.views.index'),
    url(r'^add/$', 'principal.views.agregar_alumno'),
    url(r'^borrar/(?P<id_alumno>\d+)$', 'principal.views.borrar_alumno'),
    url(r'^editar/(?P<id_alumno>\d+)$', 'principal.views.editar_alumno'),
)

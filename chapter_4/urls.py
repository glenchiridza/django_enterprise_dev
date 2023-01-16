from django.urls import path, register_converter, re_path
from django.views.generic import TemplateView, RedirectView
from .converters import YearConverter

from .views import practice_view,vehicle_view


register_converter(YearConverter, 'year')

app_name = "chapter_4"
urlpatterns = [

    path('', TemplateView.as_view(template_name='chapter_four/index.html')
         , kwargs={'sub_title': 'This is a sub title passed as kwargs'}),
    path(
        'chapter4/',
        TemplateView.as_view(
            template_name='chapter_4/chapter_4.html'
        )
    ),
    path(
        'my_path/my_unwanted_url/',
        RedirectView.as_view(
            url='http://localhost:8000/my_wanted_url/'
        )
    ),
    # path converters, path,int,str,slug,uuid
    path('my_path/<path:my_pattern>/',
         TemplateView.as_view(template_name='chapter_four/index.html')),
    path(
        'my_year_path/<year:year>/',
        TemplateView.as_view(template_name='chapter_four/index.html')),
    # instead of making a custome converter, can use the regular expression path
    re_path(
        'my_year_pathy/(?P<year>[0-9]{4})/$',
        TemplateView.as_view(template_name='chapter_four/index.html')
    ),

    path('practice_path/<year:year>/',practice_view),
    path('vehicle/<int:id>/',vehicle_view,name='vehicle-detail'),

]

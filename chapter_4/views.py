# from django.shortcuts import render
# from django.views.generic import TemplateView
#
#
# class IndexPage(TemplateView):
#     template_name = "chapter_4/chapter_4.html"

from django.http import Http404
from django.template.response import (
    TemplateResponse
)

from chapter_3.models import Vehicle





def practice_view(request, year):
    if year >= 1900:
        return TemplateResponse(
            request,
            'chapter_4/practice_page.html', {
                'year': year
            }
        )
    else:
        raise Http404(f'Year not found: {year}')

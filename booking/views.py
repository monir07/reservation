from django.views.generic import TemplateView


class Index(TemplateView):
    '''
    Render index.html
    '''
    template_name = "index.html"

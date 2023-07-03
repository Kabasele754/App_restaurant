# importation de package django views
from django.views.generic import TemplateView

#  definir la class dashboard view

class DashboradViews(TemplateView):
    # refferencier la page html
    template_name = 'employer_admin/dashboard.html'


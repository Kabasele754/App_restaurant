# importation de package django views
from django.views.generic import TemplateView

#  definir la class dashboard view

class AddFoodViews(TemplateView):
    # refferencier la page html
    template_name = 'employer_admin/pages/food_add.html'


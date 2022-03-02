from .models import *


def top_categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return context
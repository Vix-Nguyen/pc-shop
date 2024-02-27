from .models import Category


def add_variable_to_context(request):
    context = {
        "categories": Category.get_category_by_level()
    }
    return context

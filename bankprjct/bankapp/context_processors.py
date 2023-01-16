from .models import Category
from.models import State
def menu_links(request):
    links=Category.objects.all()
    link=State.objects.all()
    
    return dict(links=links,link=link,)
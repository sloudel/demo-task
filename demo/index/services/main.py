from index.models import Page

def increase_view_counter(page_id):
    page = Page.objects.get(id=page_id)
    page.increase_view_counter()

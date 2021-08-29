from demo.celery import app
from .services.main import increase_view_counter

@app.task
def increase_view_counter_task(page_id):
    increase_view_counter(page_id)











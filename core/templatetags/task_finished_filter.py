from django import template

register = template.Library()

@register.filter
def filter_task(tasks):
    not_finished_counter = 0
    
    for task in tasks:
        if not task.is_finished:
            not_finished_counter += 1

    
    return not_finished_counter
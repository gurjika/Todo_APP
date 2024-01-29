from django import template

register = template.Library()

@register.filter
def filter_todo(todos):
    not_finished_counter = 0
    
    for todo in todos:
        if not todo.is_finished:
            not_finished_counter += 1

    
    return not_finished_counter




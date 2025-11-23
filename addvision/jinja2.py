import jinja2

def environment(**options):
    env = jinja2.Environment(**options)
    # Add any custom filters or globals here if needed
    return env

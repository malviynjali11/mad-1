from jinja2 import Template
data = ['Analyst', 'Programmer', 'Developer']
temp = """
{% for item in data %}
{% if 't' in item %}
{{item}}
{% endif %}
{% endfor %}
"""
made_temp = Template(temp)
output = made_temp.render(data=data)
print(output)
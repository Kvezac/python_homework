from jinja2 import Template

""" Создайте макроопределение для отображения списка пользователей в HTML-документе. У вас есть список пользователей 
    в переменной users, каждый пользователь представлен в виде словаря с ключами name и email. Используйте цикл for и 
    условие if для отображения пользователей, у которых почта кончается на gmail.com
    """

persons = [
    {"name": "Alexei", "email": "alexei@gmail.com"},
    {"name": "Nicholas", "email": "nicolas@gmail.com"},
    {"name": "Ivan", "email": "ivan@example.com"}
]

html = '''{% macro list_users(users) -%}
<ul>{% for u in users -%}
{% if u.email.endswith("gmail.com") %}
<li>{{ u.name}}</li>
<li>{{u.email}}</li>
{%- endif %}
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)


from jinja2 import Template


"""Создайте макроопределение для отображения списка продуктов в HTML-документе. У вас есть список продуктов в
    переменной products, каждый продукт представлен в виде словаря с ключами name и price. Используйте цикл for и условие
    elif для отображения цены в зависимости от диапазона:
    - Если цена меньше 10, то пишем, что продукт доступный.
    - Если цена меньше 20, то пишем, что продукт имеет среднюю цену.
    - И если цена больше, то пишем, что продукт дорогой.
"""

products = [
    {'name': 'Молоко', 'price': 15},
    {'name': 'Хлеб', 'price': 25},
    {'name': 'Сыр', 'price': 35},
    {'name': 'Яблоки', 'price': 9},
    {'name': 'Бананы', 'price': 20},
    {'name': 'Мясо', 'price': 50},
    {'name': 'Рыба', 'price': 45},
]


html = '''{% macro list_users(products) -%}
<ul>{% for prod in products -%}
{% if prod.price > 20 %}
<li>{{ prod.name}} - продукт дорогой</li>
{%- elif prod.price > 10 %}
<li>{{ prod.name }} - имеет среднюю цену</li>
{%- else %}
<li>{{ prod.name }} - продукт доступный</li>
{%- endif %}
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users=products)

print(msg)
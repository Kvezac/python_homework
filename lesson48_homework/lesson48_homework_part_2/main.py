from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader(searchpath="./templates")
template_env = Environment(loader=file_loader)

template = template_env.get_template("index.html")
rendered_template = template.render()

if __name__ == '__main__':
    print(rendered_template)

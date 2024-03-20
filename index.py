import datetime
import jinja2
import pdfkit

my_name = "Manjula"
item1 = "TV"
item2 = "couch"
item3 = "Washing machine"
today_date = datetime.today().strftime("%d %b, %y")

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3, 'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("my-basic-template.html")
output_text = template.render(context)

pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf")
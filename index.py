import datetime
import jinja2
import pdfkit

my_name = "Manjula"
item1 = "TV"
item2 = "couch"
item3 = "Washing machine"
today_date = datetime.today().strftime("%d %b, %y")

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3, 'today_date': today_date}


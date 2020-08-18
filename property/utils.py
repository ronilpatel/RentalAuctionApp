from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import os
import random
from xhtml2pdf import pisa
from django.conf import settings

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    print("type of pdf in utils.py ", pdf)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def render_to_file(path: str, params: dict):
    template = get_template(path)
    html = template.render(params)
    file_name = "{0}-{1}.pdf".format(params['username'], random.randint(1, 1000000))
    file_path = os.path.join(settings.MEDIA_ROOT, "receiptspdf/" + file_name)    
    with open(file_path, 'wb') as pdf:
        pisa.pisaDocument(BytesIO(html.encode("UTF-8")), pdf)
    print("file name is : ", file_name)
    print("file path is : ", file_path)
    return [file_name, file_path]
from django.template import loader
from django.http import HttpResponse

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["firstname"]
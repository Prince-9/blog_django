from django.http import HttpResponse
from django.template import loader


def index(request):
  template = loader.get_template('blog_templates/blog_index.html')
  return HttpResponse(template.render())

  
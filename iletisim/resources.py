from import_export import resources
from .models import Newsletter

class NewsletterResource(resources.ModelResource):

    class Meta:
        model = Newsletter
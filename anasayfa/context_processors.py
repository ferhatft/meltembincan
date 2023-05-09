from iletisim.forms import NewsletterForm
from portfolio.models import ToursModel
from anasayfa.models import Slide


def add_variable_to_context(request):
    tourmenu = ToursModel.objects.all()
    newsletterform = NewsletterForm()
    slide = Slide.objects.all()
    return {
        'newsletterform': newsletterform,
        'tourmenu':tourmenu,
        'slide':slide,
    }

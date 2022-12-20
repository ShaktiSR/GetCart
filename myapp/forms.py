from django.db.models import fields
from django.forms import ModelForm
from .models import ulimiter
from .models import Poll

class limiter(ModelForm):
    class Meta:
        model = ulimiter
        fields = ['uid','ulimit']


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['loguser','question', 'option_one', 'option_two', 'option_three','option_four']
        #fields = ['__all__']
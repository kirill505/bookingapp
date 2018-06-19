from django.shortcuts import render
from django.utils import timezone
from .models import Hotel

def hotel_list(request):
    hotels = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hotels/hotel_list.html', {'hotels':hotels})

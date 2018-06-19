from django.shortcuts import render
from django.utils import timezone
from .models import Hotel
from django.shortcuts import get_object_or_404

def hotel_list(request):
    hotels = Hotel.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hotels/hotel_list.html', {'hotels':hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})

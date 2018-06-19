from django.shortcuts import render

def hotel_list(request):
    return render(request, 'hotels/hotel_list.html', {})

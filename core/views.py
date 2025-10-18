# shortener/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import ShortURL
from django.views.decorators.csrf import csrf_protect,csrf_exempt


@csrf_protect
def home(request):
    template = 'index.html'
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        if not long_url:
            return render(request, template, {"error": "Please enter a valid URL."})
        
        obj, created = ShortURL.objects.get_or_create(original_url=long_url)
        short_url = request.build_absolute_uri(reverse("redirect", args=[obj.short_code]))
        return render(request, template, {"short_url": short_url})
    
    return render(request, template)


def redirect_view(request, short_code):
    url_obj = get_object_or_404(ShortURL, short_code=short_code)
    url_obj.click_count += 1
    url_obj.save(update_fields=["click_count"])
    return redirect(url_obj.original_url)


# Optional API endpoint
@csrf_exempt
def api_shorten(request):
    long_url = request.GET.get("url")
    if not long_url:
        return JsonResponse({"error": "No URL provided"}, status=400)
    obj, created = ShortURL.objects.get_or_create(original_url=long_url)
    short_url = request.build_absolute_uri(reverse("redirect", args=[obj.short_code]))
    return JsonResponse({"short_url": short_url})

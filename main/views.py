from django.shortcuts import render
import info.views
import image.views


def register(request):
    image_cnt = len(image.views.ImageListView.model.objects.all())
    if image_cnt <= 12:
        data_image = image.views.ImageListView.model.objects.all().order_by('-id')[:image_cnt]
    else:
        data_image = image.views.ImageListView.model.objects.all().order_by('-id')[:8]

    cnt = len(info.views.InfoListView.model.objects.all())
    if cnt <= 10:
        data_info = info.views.InfoListView.model.objects.all().order_by('-id')[:cnt]
    else:
        data_info = info.views.InfoListView.model.objects.all().order_by('-id')[:10]

    return render(request, 'main/main.html', {'data_info': data_info, 'data_image': data_image})

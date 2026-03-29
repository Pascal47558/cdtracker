from django.shortcuts import render, redirect, get_object_or_404

from .models import CD
from .forms import CD_Form
from django.db.models import Q
# Create your views here.
def index(request):
    CDs = CD.objects.order_by("band")
    context = {'CDs': CDs,}
    return render(request, "index.html", context)

def NewCD(request):

    if request.method != "POST":
        # no data submited
        form = CD_Form()
    else:
        # data submitted
        form = CD_Form(data=request.POST)
        if form.is_valid():
            NewCD = form.save(commit=False)
            NewCD.save()
            return redirect("index")
    context = {'form': form}
    return render(request, "new_cd.html", context)

def search(request):
    query = request.GET.get('q')
    results = CD.objects.none() # Default empty queryset
    if query:
        # Use Q objects to search in multiple fields (title OR content)
        results = CD.objects.filter(
            Q(band__icontains=query) | Q(album__icontains=query)
        ).distinct()
    return render(request, 'index.html', {'CDs': results, 'query': query})

def cd_view(request, id):
    obj = get_object_or_404(CD, id=id)
    return render(request, 'detail.html', {'CD': obj})
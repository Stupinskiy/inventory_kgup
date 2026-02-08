from datetime import date

from django.shortcuts import get_object_or_404, render

from .models import Apartment, House, InventoryAct


def dashboard(request):
    houses_count = House.objects.count()
    apartments_count = Apartment.objects.count()
    acts_count = InventoryAct.objects.count()

    return render(
        request,
        'dashboard.html',
        {
            'houses_count': houses_count,
            'apartments_count': apartments_count,
            'acts_count': acts_count,
        },
    )


def houses_list(request):
    houses = House.objects.all()
    return render(request, 'houses.html', {'houses': houses})


def house_detail(request, id):
    house = get_object_or_404(House, id=id)
    apartments = Apartment.objects.filter(house=house)
    return render(request, 'house_detail.html', {
        'house': house,
        'apartments': apartments,
    })


def create_act(request, id):
    apartment = get_object_or_404(Apartment, id=id)

    if request.method == 'POST':
        InventoryAct.objects.create(
            apartment=apartment,
            year=date.today().year,
            inspection_date=date.today(),
            technical_condition=request.POST['technical_condition'],
            remarks=request.POST.get('remarks'),
            conclusion=request.POST['conclusion'],
            inspector=request.user.username,
        )

    return render(request, 'create_act.html', {'apartment': apartment})

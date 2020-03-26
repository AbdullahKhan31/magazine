from django.shortcuts import render, redirect
from auditorium.models import AuditoriumReservation
from daycare.models import DaycareReservation
from alumni.models import Alumni
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests, json
import pdb

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

# Home Screen View-----------------------------------------------------------------------------------------------------


def home_screen_view(request):
    return render(request, 'frontend/home.html')


def main_home_screen_view(request):
    return render(request, 'frontend/mainhome.html')


# Auditorium Reservation-----------------------------------------------------------------------------------------------


def auditorium_reservation(request):
    context = {
        'page_title': 'Auditorium Reservation'
    }

    if request.method == 'GET':
        return render(request, 'FrontEnd/auditorium-reservation.html', context)

    elif request.method == 'POST':
        data = {
            'reason': request.POST.get('reason'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time'),
            'requestor': 1
        }

        response = requests.post('http://localhost:8000/auditorium/reservation/', data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            return redirect('FrontEnd:auditorium_list_reservation')
        else:
            return redirect('FrontEnd:auditorium_list_reservation')

        return render(request, 'FrontEnd/auditorium-reservation.html', context)


def auditorium_list_reservation(request):
    list_reservations = AuditoriumReservation.objects.order_by('-created_at')
    page = request.GET.get('page', '1')
    paginator = Paginator(list_reservations, '9')

    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {
        'list_reservation': reservations
    }

    return render(request, 'FrontEnd/auditorium-list-reservation.html', context)


def auditorium_edit_reservation(request, reservation_id):
    reservation = AuditoriumReservation.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Update Reservation',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/auditorium-edit-reservation.html', context)


def auditorium_update_reservation(request, reservation_id):
    reservation = AuditoriumReservation.objects.get(pk=reservation_id)
    data = {
        'reason': request.POST.get('reason'),
        'start_time': request.POST.get('start_time'),
        'end_time': request.POST.get('end_time')
    }

    response = requests.put('http://localhost:8000/auditorium/reservation/' + str(reservation.id) +'/', data=json.dumps(data), headers=headers)
    # pdb.set_trace()
    if response.status_code == 200:
        return redirect('FrontEnd:auditorium_list_reservation')
    else:
        return redirect('FrontEnd:auditorium_list_reservation')


def auditorium_detail_reservation(request, reservation_id):
    reservation = AuditoriumReservation.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Detail Reservation',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/auditorium-detail-reservation.html', context)

# Daycare Reservation---------------------------------------------------------------------------------------------------


def daycare_reservation(request):
    context = {
        'page_title': 'Daycare Reservation'
    }

    if request.method == 'GET':
        return render(request, 'FrontEnd/daycare-reservation.html', context)

    elif request.method == 'POST':
        data = {
            'reason': request.POST.get('reason'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time'),
            'requestor': 1
        }

        response = requests.post('http://localhost:8000/daycare/daycare/', data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            # pdb.set_trace()
            return redirect('FrontEnd:daycare_list_reservation')
        else:
            return redirect('FrontEnd:daycare_list_reservation')

        return render(request, 'FrontEnd/daycare-reservation.html', context)


def daycare_list_reservation(request):
    list_reservations = DaycareReservation.objects.order_by('-created_at')
    page = request.GET.get('page', '1')
    paginator = Paginator(list_reservations, '9')

    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {
        'list_reservation': reservations
    }

    return render(request, 'FrontEnd/daycare-list-reservation.html', context)


def daycare_edit_reservation(request, reservation_id):
    reservation = DaycareReservation.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Update Reservation',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/daycare-edit-reservation.html', context)


def daycare_update_reservation(request, reservation_id):
    reservation = DaycareReservation.objects.get(pk=reservation_id)
    data = {
        'reason': request.POST.get('reason'),
        'start_time': request.POST.get('start_time'),
        'end_time': request.POST.get('end_time')
    }

    response = requests.put('http://localhost:8000/daycare/daycare/' + str(reservation.id) +'/', data=json.dumps(data), headers=headers)
    # pdb.set_trace()
    if response.status_code == 200:
        return redirect('FrontEnd:daycare_list_reservation')
    else:
        return redirect('FrontEnd:daycare_list_reservation')


def daycare_detail_reservation(request, reservation_id):
    reservation = DaycareReservation.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Detail Reservation',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/daycare-detail-reservation.html', context)


# Alumni --------------------------------------------------------------------------------------------------------------


def alumni_register(request):
    context = {
        'page_title': 'Alumni Registration'
    }

    if request.method == 'GET':
        return render(request, 'FrontEnd/alumni-register.html', context)

    elif request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'year_of_passing': request.POST.get('year_of_passing'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'martial_status': request.POST.get('martial_status'),
            'profession': request.POST.get('profession'),
            'address': request.POST.get('address'),
            'graduation': request.POST.get('graduation'),
            'graduation1': request.POST.get('graduation1'),
            'requestor': 1
        }

        response = requests.post('http://localhost:8000/alumni/alumni/', data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            # pdb.set_trace()
            return redirect('FrontEnd:alumni_list')
        else:
            return redirect('FrontEnd:alumni_list')

        return render(request, 'FrontEnd/alumni-register.html', context)


def alumni_list(request):
    list_reservations = Alumni.objects.order_by('-created_at')
    page = request.GET.get('page', '1')
    paginator = Paginator(list_reservations, '9')

    try:
        reservations = paginator.page(page)
    except PageNotAnInteger:
        reservations = paginator.page(1)
    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {
        'list_reservation': reservations
    }

    return render(request, 'FrontEnd/alumni-list.html', context)


def alumni_edit(request, reservation_id):
    reservation = Alumni.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Update Alumni Data',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/alumni-edit.html', context)


def alumni_update(request, reservation_id):
    reservation = Alumni.objects.get(pk=reservation_id)
    data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'year_of_passing': request.POST.get('year_of_passing'),
            'date_of_birth': request.POST.get('date_of_birth'),
            'martial_status': request.POST.get('martial_status'),
            'profession': request.POST.get('profession'),
            'address': request.POST.get('address'),
            'graduation': request.POST.get('graduation'),
            'graduation1': request.POST.get('graduation1')
    }

    response = requests.put('http://localhost:8000/alumni/alumni/' + str(reservation.id) +'/', data=json.dumps(data), headers=headers)
    # pdb.set_trace()
    if response.status_code == 200:
        return redirect('FrontEnd:alumni_list')
    else:
        return redirect('FrontEnd:alumni_list')


def alumni_detail(request, reservation_id):
    reservation = Alumni.objects.get(pk=reservation_id)

    context = {
        'page_title': 'Detail Alumni',
        'reservation': reservation
    }

    return render(request, 'FrontEnd/alumni-detail.html', context)


def about_view(request):
    return render(request, 'staticpages/about.html')


def students_view(request):
    return render(request, 'staticpages/students.html')


def arr_view(request):
    return render(request, 'staticpages/arr.html')


def coc_view(request):
    return render(request, 'staticpages/coc.html')


def cas_view(request):
    return render(request, 'staticpages/cas.html')


def ss_view(request):
    return render(request, 'staticpages/ss.html')


def office_view(request):
    return render(request, 'staticpages/office.html')


def ad_view(request):
    return render(request, 'staticpages/ad.html')


def md_view(request):
    return render(request, 'staticpages/md.html')


def po_view(request):
    return render(request, 'staticpages/po.html')


def contact_view(request):
    return render(request, 'staticpages/contact.html')


def re_view(request):
    return render(request, 'staticpages/re.html')


def research_view(request):
    return render(request, 'staticpages/research.html')


def biores_view(request):
    return render(request, 'staticpages/biores.html')


def chemres_view(request):
    return render(request, 'staticpages/chemres.html')


def civilres_view(request):
    return render(request, 'staticpages/civilres.html')


def compres_view(request):
    return render(request, 'staticpages/compres.html')


def rector_view(request):
    return render(request, 'staticpages/rector.html')


def history_view(request):
    return render(request, 'staticpages/history.html')


def cuiranking_view(request):
    return render(request, 'staticpages/cuiranking.html')



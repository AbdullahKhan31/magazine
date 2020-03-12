from django.shortcuts import render, redirect
from auditorium.models import AuditoriumReservation
from daycare.models import DaycareReservation
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests, json
import pdb

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

# Home Screen View


def home_screen_view(request):
    return render(request, 'frontend/home.html')


def main_home_screen_view(request):
    return render(request, 'frontend/mainhome.html')
# Auditorium Reservation


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
            pdb.set_trace()
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




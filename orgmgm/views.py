from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Organisation, Kontakt
from .forms import (SearchOrganisationForm, 
                    AddKontaktForm, 
                    AddOrganisationForm,
                    SearchKontaktForm,
                    AddActivityForm)

# Views for Organisation Model


def organisation_add(request):
    if request.method == 'POST':
        form = AddOrganisationForm(request.POST)
        if form.is_valid():
            organisation = form.save()
            return redirect('organisation_details', pk=organisation.pk)
    else:
        form = AddOrganisationForm()
    return render(request, 'orgmgm/organisation/add.html', {'form': form})


def organisation_delete(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    if request.method == 'POST':
        organisation.delete()
        return redirect('organisation_list')
    return render(request, 'orgmgm/organisation/delete.html',
                  {'organisation': organisation})


def organisation_detail(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    return render(request, 'orgmgm/organisation/detail.html',
                  {'organisation': organisation})


def organisation_edit(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    if request.method == 'POST':
        form = AddOrganisationForm(request.POST, instance=organisation)
        if form.is_valid():
            organisation = form.save()
            return redirect('organisation_detail', pk=organisation.pk)
    else:
        form = AddOrganisationForm(instance=organisation)
    return render(request, 'orgmgm/organisation/edit.html', {'form': form})


def organisation_list(request):
    org_list = Organisation.objects.all()
    paginator = Paginator(org_list, 25)

    page = request.GET.get('page')

    try:
        orgs = paginator.page(page)
    except PageNotAnInteger:
        orgs = paginator.page(1)
    except EmptyPage:
        orgs = paginator.page(paginator.num_pages)

    return render(request, 'orgmgm/organisation/list.html', {'orgs': orgs})


def organisation_search(request):
    if request.method == 'POST':
        form = SearchOrganisationForm(request.POST)
        if form.is_valid():
            ol = Organisation.objects.filter(
                name__icontains=form.cleaned_data['orgname'],
                plz__icontains=form.cleaned_data['plz'],
                stadt__icontains=form.cleaned_data['stadt'],
            )
            paginator = Paginator(ol, 25)
            page = request.GET.get('page')

            try:
                orgs = paginator.page(page)
            except PageNotAnInteger:
                orgs = paginator.page(1)
            except EmptyPage:
                orgs = paginator.page(paginator.num_pages)

            return render(request, 'orgmgm/organisation/list.html',
                          {'orgs': orgs})
    else:
        form = SearchOrganisationForm()
    return render(request, 'orgmgm/organisation/search.html', {'form': form})


# Views for Kontakt


def kontakt_add(request):
    if request.method == 'POST':
        form = AddKontaktForm(request.POST)
        if form.is_valid():
            kontakt = form.save()
            return redirect('kontakt_detail', pk=kontakt.pk)
    else:
        if request.GET.get('organisation'):
            fk = request.GET.get('organisation')
            form = AddKontaktForm(initial={'organisation': fk})
            # form.fields['organisation'].widget.attrs['disabled'] = True
        else:
            form = AddKontaktForm()
    return render(request, 'orgmgm/kontakt/add.html', {'form': form})


def kontakt_delete(request, pk):
    kontakt = get_object_or_404(Kontakt, pk=pk)
    if request.method == 'POST':
        kontakt.delete()
        return redirect('kontakt_add')
    return render(request, 'orgmgm/kontakt/delete.html', {'kontakt': kontakt})


def kontakt_detail(request, pk):
    kontakt = get_object_or_404(Kontakt, pk=pk)
    return render(request, 'orgmgm/kontakt/detail.html', {'kontakt': kontakt})


def kontakt_edit(request, pk):
    kontakt = get_object_or_404(Kontakt, pk=pk)
    if request.method == 'POST':
        form = AddKontaktForm(request.POST, instance=kontakt)
        if form.is_valid():
            kontakt = form.save()
            return redirect('kontakt_detail', pk=kontakt.pk)
    else:
        form = AddKontaktForm(instance=kontakt)
    return render(request, 'orgmgm/kontakt/edit.html', {'form': form})


def kontakt_list(request):
    kon_list = Kontakt.objects.all().order_by('nachname')
    paginator = Paginator(kon_list, 25)

    page = request.GET.get('page')

    try:
        kons = paginator.page(page)
    except PageNotAnInteger:
        kons = paginator.page(1)
    except EmptyPage:
        kons = paginator.page(paginator.num_pages)

    return render(request, 'orgmgm/kontakt/list.html', {'kons': kons})


def kontakt_search(request):
    if request.method == 'POST':
        form = SearchKontaktForm(request.POST)
        if form.is_valid():
            kl = Kontakt.objects.filter(
                nachname__icontains=form.cleaned_data['nachname'],
                vorname__icontains=form.cleaned_data['vorname'],
                organisation__name__icontains=form.cleaned_data[
                    'organisation'],
            )
            return render(request, 'orgmgm/kontakt/list.html', {'kl': kl})
    else:
        form = SearchKontaktForm()
    return render(request, 'orgmgm/kontakt/search.html', {'form': form})


# Views for Activity Model



def activity_add(request):
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_details', pk=activity.pk)
    else:
        form = AddActivityForm()
    return render(request, 'orgmgm/activity/add.html', {'form': form})

# Needed activity details


def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'orgmgm/activity/detail.html',
                  {'activity': activity})



# Views for Dashboard

def dashboard_overview(request):
    return render(request, 'orgmgm/dashboard/overview.html')
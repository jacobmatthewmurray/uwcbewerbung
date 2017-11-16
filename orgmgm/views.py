from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.views.generic.detail import DetailView
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractDay
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Organisation, Kontakt, Activity, Bundesland, ActivityType
from .forms import (SearchOrganisationForm,
                    AddKontaktForm,
                    SearchActivityForm,
                    AddOrganisationForm,
                    SearchKontaktForm,
                    AddActivityForm)
from .fusioncharts import FusionCharts


# For now no sign up option. Registration via email to Jacob.

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('dashboard_overview')
#     else:
#         form = SignUpForm()
#     return render(request, 'orgmgm/signup.html', {'form': form})


@login_required
def dashboard_overview(request):

    bunds = Bundesland.objects.annotate(num_orgs=Count('organisation'))

    bunds_ds = {}

    bunds_ds['chart'] = {
        "caption": "Organisationen pro Bundesland",
        "subCaption": "Testdaten",
        "xAxisName": "",
        "yAxisName": "Anzahl",
        "theme": "zune"
    }

    bunds_ds['data'] = []

    for b in bunds:
        data = {}
        data['label'] = b.bundeslandshort
        data['value'] = b.num_orgs
        bunds_ds['data'].append(data)

    column2da = FusionCharts("column2d", "ex1", "600",
                             "400", "chart-1", "json", bunds_ds)

    acts = Activity.objects \
        .annotate(actmonth=ExtractMonth('activitydate'), actday=ExtractDay('activitydate')) \
        .values('actmonth', 'actday')\
        .annotate(num_acts=Count('pk'))

    acts_ds = {}

    acts_ds['chart'] = {
        "caption": "Aktivitaeten im letzten Monat",
        "subCaption": "Testdaten",
        "xAxisName": "",
        "yAxisName": "Anzahl",
        "theme": "zune"
    }

    acts_ds['data'] = []

    for a in acts:
        data = {}
        data['label'] = ('0' + str(a['actday']))[-2:] + \
            '|' + ('0' + str(a['actmonth']))[-2:]
        data['value'] = a['num_acts']
        acts_ds['data'].append(data)

    column2db = FusionCharts("column2d", "ex2", "600",
                             "400", "chart-2", "json", acts_ds)

    return render(request, 'orgmgm/dashboard/overview.html', {'output': [column2da.render(), column2db.render()]})


# Views for Organisation Model

@login_required
def organisation_add(request):
    if request.method == 'POST':
        form = AddOrganisationForm(request.POST)
        if form.is_valid():
            organisation = form.save()
            return redirect('organisation_detail', pk=organisation.pk)
    else:
        form = AddOrganisationForm()
    return render(request, 'orgmgm/organisation/add.html', {'form': form})


@login_required
def organisation_delete(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    if request.method == 'POST':
        organisation.delete()
        return redirect('organisation_list')
    return render(request, 'orgmgm/organisation/delete.html',
                  {'organisation': organisation})


class OrganisationDetail(LoginRequiredMixin, DetailView):

    model = Organisation
    template_name = 'orgmgm/organisation/detail.html'
    context_object_name = "organisation"

    def get_context_data(self, **kwargs):
        # print(self.pk)
        context = super(OrganisationDetail, self).get_context_data(**kwargs)
        context['activity_list'] = Activity.objects.filter(
            organisation_id=self.kwargs['pk'])
        return context


# def organisation_detail(request, pk):
#     organisation = get_object_or_404(Organisation, pk=pk)
#     return render(request, 'orgmgm/organisation/detail.html',
#                   {'organisation': organisation})


@login_required
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


@login_required
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


@login_required
def organisation_search(request):
    if request.method == 'POST':
        form = SearchOrganisationForm(request.POST)
        if form.is_valid():
            ol = Organisation.objects.filter(
                name__icontains=form.cleaned_data['name'],
                plz__icontains=form.cleaned_data['plz'],
                stadt__icontains=form.cleaned_data['stadt'],
                bundesland__bundesland__icontains=form.cleaned_data['bundesland'],
                organisationtype__organisationtype__icontains=form.cleaned_data['organisationtype'],
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

@login_required
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


@login_required
def kontakt_delete(request, pk):
    kontakt = get_object_or_404(Kontakt, pk=pk)
    if request.method == 'POST':
        kontakt.delete()
        return redirect('kontakt_add')
    return render(request, 'orgmgm/kontakt/delete.html', {'kontakt': kontakt})


@login_required
def kontakt_detail(request, pk):
    kontakt = get_object_or_404(Kontakt, pk=pk)
    return render(request, 'orgmgm/kontakt/detail.html', {'kontakt': kontakt})


@login_required
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


@login_required
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


@login_required
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

            paginator = Paginator(kl, 25)
            page = request.GET.get('page')

            try:
                kons = paginator.page(page)
            except PageNotAnInteger:
                kons = paginator.page(1)
            except EmptyPage:
                kons = paginator.page(paginator.num_pages)


            return render(request, 'orgmgm/kontakt/list.html', {'kons': kons})
    else:
        form = SearchKontaktForm()
    return render(request, 'orgmgm/kontakt/search.html', {'form': form})


# Views for Activity Model


@login_required
def activity_add(request):
    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        if request.GET.get('organisation'):
            fk = request.GET.get('organisation')
            form = AddActivityForm(initial={'organisation': fk})
        else:
            form = AddActivityForm()
    return render(request, 'orgmgm/activity/add.html', {'form': form})


@login_required
def activity_list(request):
    act_list = Activity.objects.all().order_by('activitydate')
    paginator = Paginator(act_list, 25)

    page = request.GET.get('page')

    try:
        acts = paginator.page(page)
    except PageNotAnInteger:
        acts = paginator.page(1)
    except EmptyPage:
        acts = paginator.page(paginator.num_pages)

    return render(request, 'orgmgm/activity/list.html', {'acts': acts})


@login_required
def activity_edit(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = AddActivityForm(request.POST, instance=activity)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = AddActivityForm(instance=activity)
    return render(request, 'orgmgm/activity/edit.html', {'form': form})


@login_required
def activity_search(request):
    if request.method == 'POST':
        form = SearchActivityForm(request.POST)
        if form.is_valid():
            al = Activity.objects.filter(
                titel__icontains=form.cleaned_data['titel'],
                activitydate__icontains=form.cleaned_data['activitydate'],
                description__icontains=form.cleaned_data['description'],
                activitytype__activitytype__icontains=form.cleaned_data['activitytype'],
                #organisation__name__icontains=form.cleaned_data['organisation'],
            )

            paginator = Paginator(al, 25)
            page = request.GET.get('page')

            try:
                acts = paginator.page(page)
            except PageNotAnInteger:
                acts = paginator.page(1)
            except EmptyPage:
                acts = paginator.page(paginator.num_pages)


            return render(request, 'orgmgm/activity/list.html', {'acts': acts})
    else:
        form = SearchActivityForm()
    return render(request, 'orgmgm/activity/search.html', {'form': form})


@login_required
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('kontakt_add')
    return render(request, 'orgmgm/activity/delete.html', {'activity': activity})


@login_required
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'orgmgm/activity/detail.html',
                  {'activity': activity})

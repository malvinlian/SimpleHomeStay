from __future__ import unicode_literals
from django.shortcuts import render, redirect
import datetime
from .models import Room,Reservation
from .forms import ReserveForm

from bootstrap_datepicker_plus import DatePickerInput


from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

import calendar


from .forms import ReserveForm

# Create your views here.

def Roompage(request):
    Roompage = Room.objects.all()
    template = 'Room/rooms.html'
    context = {
        'Roompage' : Roompage ,
    }
    return render(request , template , context)


#    def BookingTotalCalculation(CheckIn,CheckOut,TotalCost,nights):
#        price = Room.price
#        CheckOut = datetime.strptime(str(CheckOut), "%m/%d/%Y")
#        CheckIn = datetime.strptime(str(CheckIn), "%m/%d/%Y")
#        timedeltaSum = CheckOut - CheckIn
#        nights = timedeltaSum.days
#        TotalCost = nights * price
#        context = {
#            'nights': nights,
#            'TotalCost' : TotalCost ,
#        }
#        return render(context)

##### Here's code for the view to look up the event objects for to put in
# the context for the template. It goes in your app's views.py file (or
# wherever you put your views).
#####
import datetime
from django.shortcuts import redirect, render
from django.views import generic
from .forms import BS4ScheduleForm, SimpleScheduleForm
from .models import Schedule
from . import mixins


class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'Room/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class WeekCalendar(mixins.WeekCalendarMixin, generic.TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'Room/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class WeekWithScheduleCalendar(mixins.WeekWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの週間カレンダーを表示するビュー"""
    template_name = 'Room/week_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView,):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'Room/month_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'Room/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('Room:mycalendar', year=date.year, month=date.month, day=date.day)


class MonthWithFormsCalendar(mixins.MonthWithFormsMixin, generic.CreateView):
    """フォーム付きの月間カレンダーを表示するビュー"""
    template_name = 'Room/month_with_forms.html'
    model = Schedule
    model = Room
    date_field = 'date'
    form_class = SimpleScheduleForm

    def get(self, id, request, **kwargs):
        context = self.get_month_calendar()
        context['Room'] = Room.objects.get(id=id)
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        context = self.get_month_calendar()
        formset = context['month_formset']
        if formset.is_valid():
            formset.save()
            return redirect('Room:month_with_forms')

        return render(request, self.template_name, context)


def calendar(request):
  context = locals()
  template = 'Room/calendar.html'
  return render(request,template,context)

#def event(request, event_id=None):
#    instance = Event()
#    if event_id:
#        instance = get_object_or_404(Event, pk=event_id)
#    else:
#        instance = Event()

#    form = EventForm(request.POST or None, instance=instance)
#    if request.POST and form.is_valid():
#        form.save()
#        return HttpResponseRedirect(reverse('cal:calendar'))
#    return render(request, 'cal/event.html', {'form': form})

#def Booking(request,id):
#    room  = Room.objects.get(id=id)
#    template_name =  'Room/booking.html'
#
#    if request.method == 'POST':
#        reserve_form = ReserveForm(request.POST)
#
#        if reserve_form.is_valid():
#            reserve = reserve_form.save(commit=False)
#            reserve.reserve_form = room
#            reserve.save()
#            return HttpResponseRedirect('/room/')
#
#        else:
#            reserve_form = ReserveForm()
#
#            return render(request , template , context)

class Booking(mixins.MonthWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'Room/booking.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, id, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        context['Room'] = Room.objects.get(id=id)
        return context

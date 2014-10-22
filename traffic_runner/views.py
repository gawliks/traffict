from django.shortcuts import render
from django.forms.formsets import formset_factory
from traffict.tools.views import ViewProcessor
from api_manager.models import Api
from traffic_runner import models
from traffic_runner import forms

def index(request):
    return render(request, 'traffic_runner/index.html')

def plans(request):
    plans = models.TestPlan.objects.all()
    PlanFormSet = formset_factory(forms.TestPlanForm)
    return render(request, 'traffic_runner/plans.html', {
        'formset': PlanFormSet(initial= [
            {'name': p.name, 'query': p.query, 'test_time': p.test_time, 'interval': p.interval}
            for p in models.TestPlan.objects.all()
        ])
    })

def plan(request, plan_id=None):
    vp = ViewProcessor(request, model=models.TestPlan)

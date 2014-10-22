from django import forms
from traffic_runner.models import TestPlan

class TestPlanForm(forms.ModelForm):
    class Meta:
        model = TestPlan
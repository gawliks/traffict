from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, render_to_response

from api_manager import models
from api_manager import forms
from traffict.tools.views import ViewProcessor

def index(request):
    apis = models.Api.objects.all()
    return render(request, 'api_manager/index.html', {'apis': apis})

def template(request, template):
    return render_to_response('api_manager/{0}.html'.format(template))



def api(request, api_id=None):
    vp = ViewProcessor(
        request, models.Api, forms.ApiForm, {'apis': models.Api.objects.all()}
    )
    form = None
    if request.method == 'POST':
        if vp.save(object_id=api_id, redirect_to=('api_manager:index',),
            success_message='Api saved'
        ):
            return vp.response
        else:
            form = vp.response
    context = vp.get_context(form=form, object_id=api_id, prefix='api')
    return vp.render(
        'api_manager/api_details.html', context
    )

def delete_api(request, api_id):
    api = get_object_or_404(models.Api, pk=api_id)
    api.delete()
    messages.success(request, u'Api deleted')
    return redirect('api_manager:index')

def queries(request, api_id):
    vp = ViewProcessor(
        request, models.Api, forms.ApiForm, {'apis': models.Api.objects.all()}
    )
    context = vp.get_context(form=None, object_id=api_id, prefix='api')
    context.update({
        'queries': models.Query.objects.all()
    })
    return render(request, 'api_manager/queries.html', context)

def query(request, api_id=None, query_id=None):
    api_vp = ViewProcessor(
        request, models.Api, forms.ApiForm, {'apis': models.Api.objects.all()}
    )
    context = api_vp.get_context(form=None, object_id=api_id, prefix='api')
    vp = ViewProcessor(
        request, models.Query, forms.QueryForm,
    )
    form = None
    if request.method == 'POST':
        if vp.save(object_id=query_id, redirect_to=('api_manager:queries', api_id),
            success_message=u'Query saved'
        ):
            return vp.response
        else:
            form = vp.response
    ctx = vp.get_context(form=form, object_id=query_id, prefix='query')
    context.update(ctx)
    return vp.render('api_manager/query_form.html', context)


def delete_query(request, query_id):
    query = get_object_or_404(models.Query, pk=query_id)
    api_id = query.api.id
    query.delete()
    messages.success(request, u'Query deleted')
    return redirect('api_manager:queries', api_id)
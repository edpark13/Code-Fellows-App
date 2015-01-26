from django.shortcuts import render, render_to_response, RequestContext
from signapps.models import Info
from .forms import InfoForm

def home(request):
    
    form = InfoForm(request.POST)
    
    if form.is_valid():
        save = form.save(commit=False)
        save.save()
    
    return render_to_response("info.html", locals(), RequestContext(request))

def accounts(request):
    infoList = Info.objects.order_by('first_name')
    accountInfos = {'infos':infoList}
    
    return render_to_response('accounts.html', accountInfos, RequestContext(request))
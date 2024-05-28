from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# @login_required(login_url='login')
def home_sig(request):
    msg = "Hello World :: SIG Home"
    return render(request, 'sig.index.html', context={"msg": msg})
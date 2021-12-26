from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
import datetime
from .models import teamPerson

def makeMailDataLectro(name, mail, sub, msg):
    data = {'name': name, 'mail': mail, 'sub': sub, 'msg': msg}
    MSG = '''
Webmail van:        {}
Mail adres:             {}
            
Message: 
{}
    '''.format(data['name'], data['mail'], data['msg'])

    send_mail(data['sub'], MSG, 'webmail@datalectro.nl', ['info@datalectro.nl'],
              fail_silently=False, auth_user='webmail@datalectro.nl', auth_password='W@rmweer.22')


def makeMailPhone(name, phone):
    data = {'name': name, 'phone': phone}
    MSG = '''
Verzoek om terug te bellen van:

Naam:        {}
Nummer:    {}
    '''.format(data['name'], data['phone'])

    send_mail('Call Request', MSG, 'webmail@datalectro.nl', ['info@datalectro.nl'],
              fail_silently=False, auth_user='webmail@datalectro.nl', auth_password='W@rmweer.22')

def makeMailClient(mail):
    MSG = '''
    Bedankt voor het invullen van ons contact formulier! Hierbij is bevestigd dat
    wij uw mail ontvangen hebben. Wij zullen zo spoedig mogelijk contact met
    u opnemen!

    Vriendelijke groet,
    DataLectro
    '''
    send_mail('Bevestiging WebForm DataLectro', MSG, 'noreply@datalectro.nl', [mail],
              fail_silently=False, auth_user='noreply@datalectro.nl', auth_password='W@rmweer.22')

def homeView(request):
    # Footer
    x = datetime.datetime.now()
    copyYear = x.strftime("%Y")
    data = {'page': 'home.html', 'copyYear': copyYear}

    # Siteforms
    if request.method == 'POST' and 'submitPhone' in request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        makeMailPhone(name, phone)
        success = {'page': 'phoneSuccess.html', 'backPage': '/home', 'copyYear': copyYear}
        return render(request, 'index.html', success)
    else:
        return render(request, 'index.html', data)

def portfolioView(request):
    # Footer
    x = datetime.datetime.now()
    copyYear = x.strftime("%Y")
    data = {'page': 'portfolio.html', 'copyYear': copyYear}

    # Siteforms
    if request.method == 'POST' and 'submitPhone' in request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        makeMailPhone(name, phone)
        success = {'page': 'phoneSuccess.html', 'backPage': '/portfolio', 'copyYear': copyYear}
        return render(request, 'index.html', success)
    else:
        return render(request, 'index.html', data)

def teamView(request):
    # Footer
    x = datetime.datetime.now()
    copyYear = x.strftime("%Y")
    person = teamPerson.objects.all()
    data = {'page': 'team.html', 'copyYear': copyYear, 'person': person}

    # Siteforms
    if request.method == 'POST' and 'submitPhone' in request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        makeMailPhone(name, phone)
        success = {'page': 'phoneSuccess.html', 'backPage': '/het-team', 'copyYear': copyYear, 'person': person}
        return render(request, 'index.html', success)
    else:
        return render(request, 'index.html', data)

def contactView(request):
    # Footer
    x = datetime.datetime.now()
    copyYear = x.strftime("%Y")
    data = {'page': 'contact.html', 'copyYear': copyYear}

    #Siteforms
    if request.method == 'POST' and 'submitPhone' in request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        makeMailPhone(name, phone)
        success = {'page': 'phoneSuccess.html', 'backPage': '/contact', 'copyYear': copyYear}
        return render(request, 'index.html', success)
    elif request.method == 'POST' and 'submitMail' in request.POST:
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        makeMailDataLectro(name, mail, sub, msg)
        makeMailClient(mail)
        mailSuccess = {'page': 'mailSuccess.html', 'name': name, 'mail': mail, 'sub': sub, 'msg': msg,
                   'backPage': '/contact', 'copyYear': copyYear}
        if request.method == 'POST' and 'invalidInfo' in request.POST:
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            sub = 'INCORRECT FORM DATA'
            msg = request.POST.get('message')
            makeMailDataLectro(name, mail, sub, msg)
            mailDeleted = {'page': 'mailDeleted.html', 'backPage': '/contact', 'copyYear': copyYear}
            return render(request, 'index.html', mailDeleted)
        return render(request, 'index.html', mailSuccess)
    else:
        return render(request, 'index.html', data)

def solarView(request):
    data = {
        'page': 'solar.html',
    }
    return render(request, 'index.html', data)
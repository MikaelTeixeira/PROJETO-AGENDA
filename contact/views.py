from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q 
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('id')

    paginator = Paginator(contacts,25)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'page_object': page_object,
        'search_title': 'Contacts',
    }

    return render(
        request, 'contact/index.html',
        context
        )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact': single_contact,
        'page_object': None,
    }

    return render( request, 'contact/contact.html', context)


def search(request):

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter( 
            Q(first_name__icontains=search_value) | 
            Q(last_name__icontains=search_value)
                )\
        .order_by('id')

    paginator = Paginator(contacts,25)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object,
        'search_value': search_value
    }

    return render(
        request,
        'contact/index.html',
        context
    )
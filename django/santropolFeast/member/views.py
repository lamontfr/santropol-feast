# coding: utf-8

from django.views import generic
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from member.models import Client, Member, Note


class ClientList(generic.ListView):
    # Display the list of clients
    model = Client
    template_name = 'client/list.html'
    context_object_name = 'clients'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientList, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientList, self).get_context_data(**kwargs)

        # Here you add some variable of context to display on template
        context['myVariableOfContext'] = 0

        return context


class ClientInfoView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/information.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientInfoView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientInfoView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientReferentView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/referent.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientReferentView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientReferentView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientAddressView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/address.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientAddressView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientAddressView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientPaymentView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/payment.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientPaymentView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientPaymentView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientAllergiesView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/allergies.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientAllergiesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientAllergiesView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientPreferencesView(generic.DetailView):
    # Display detail of one client
    model = Client
    template_name = 'client/view/preferences.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientPreferencesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ClientPreferencesView, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class MemberUpdate(generic.UpdateView):
    # Display the form to update a member
    model = Member
    template_name = "client/update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # Here you need to check if the client exist
        # You can use for example get_object_or_404()
        # note: self.kwargs["pk"] is the ID of the client given by the urls.py

        return super(MemberUpdate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        # Here you redirect to the next page
        # You can use for example reverse_lazy()

        return 0

    def get_context_data(self, **kwargs):
        context = super(MemberUpdate, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientAllergiesUpdate(generic.UpdateView):
    # Display the form to update allergies of a client
    model = Client
    template_name = "client/update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # Here you need to check if the client exist
        # You can use for example get_object_or_404()
        # note: self.kwargs["pk"] is the ID of the client given by the urls.py

        return super(ClientAllergiesUpdate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        # Here you redirect to the next page
        # You can use for example reverse_lazy()

        return 0

    def get_context_data(self, **kwargs):
        context = super(ClientAllergiesUpdate, self).get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class ClientPreferencesUpdate(generic.UpdateView):
    # Display the form to update preference of a client
    model = Client
    template_name = "client/update.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # Here you need to check if the client exist
        # You can use for example get_object_or_404()
        # note: self.kwargs["pk"] is the ID of the client given by the urls.py

        return super(ClientPreferencesUpdate, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        # Here you redirect to the next page
        # You can use for example reverse_lazy()

        return 0

    def get_context_data(self, **kwargs):
        context = super(ClientPreferencesUpdate, self).\
            get_context_data(**kwargs)

        """
        Here we need to add some variable of context to send to template :
         1 - A string active_tab who can be:
            'info'
            'referent'
            'address'
            'payment'
            'allergies'
            'preferences'
        """
        context['myVariableOfContext'] = 0

        return context


class NoteList(generic.ListView):
    # Display the list of clients
    model = Note
    template_name = 'notes/list.html'
    context_object_name = 'notes'


def mark_as_read(request, id):
    note = get_object_or_404(Note, pk=id)
    note.mark_as_read()
    return HttpResponseRedirect(reverse_lazy("member:notes"))

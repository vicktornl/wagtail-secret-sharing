from django.http import Http404
from django.template.response import TemplateResponse
from django.utils.crypto import get_random_string
from django_secret_sharing import settings as django_secret_sharing_settings
from django_secret_sharing.exceptions import SecretNotFound
from django_secret_sharing.forms import CreateSecretForm
from django_secret_sharing.utils import create_secret, get_secret_by_url_part
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page


class AbstractSecretsPage(RoutablePageMixin, Page):
    create_page_template = "wagtail_secret_sharing/create.html"
    retrieve_page_template = "wagtail_secret_sharing/retrieve.html"
    view_page_template = "wagtail_secret_sharing/view.html"

    class Meta:
        abstract = True

    @route(r"^$", name="create")
    def create(self, request):
        context = super().get_context(request)

        if request.method == "POST":
            form = CreateSecretForm(request.POST)
            if form.is_valid():
                secret, url_part = create_secret(
                    value=form.cleaned_data.get("value"),
                    expires_in=form.cleaned_data.get("expires"),
                    view_once=form.cleaned_data.get("view_once"),
                )

                context["secret"] = secret
                context["secret_url"] = self.full_url + self.reverse_subpage(
                    "retrieve", args=(url_part,)
                )
        else:
            form = CreateSecretForm()

        context["form"] = form

        return TemplateResponse(
            request,
            self.get_create_page_template(),
            context,
        )

    @route(r"^(\w+)/$", name="retrieve")
    def retrieve(self, request, url_part):
        try:
            secret, value = get_secret_by_url_part(url_part)
        except SecretNotFound:
            raise Http404()

        context = super().get_context(request)
        context["secret"] = secret
        context["url_part"] = url_part

        return TemplateResponse(
            request,
            self.get_retrieve_page_template(),
            context,
        )

    @route(r"^(\w+)/view/$", name="view")
    def view(self, request, url_part):
        try:
            secret, value = get_secret_by_url_part(url_part)
        except SecretNotFound:
            raise Http404()

        secret.erase()

        context = super().get_context(request)
        context["value"] = value
        context["secret"] = secret

        return TemplateResponse(
            request,
            self.get_view_page_template(),
            context,
        )

    @route(r"^generate-password/$", name="generate-password")
    def generate_password(self, request):
        form = CreateSecretForm(
            initial={
                "value": get_random_string(
                    django_secret_sharing_settings.PASSWORD_LENGTH
                )
            }
        )

        context = super().get_context(request)
        context["form"] = form

        return TemplateResponse(
            request,
            self.get_create_page_template(),
            context,
        )

    def get_create_page_template(self):
        return self.create_page_template

    def get_retrieve_page_template(self):
        return self.retrieve_page_template

    def get_view_page_template(self):
        return self.view_page_template

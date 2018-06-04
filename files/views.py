# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class FileList(SelectRelatedMixin, generic.ListView):
    model = models.File
    select_related = ('user', 'datafile', 'created_at', )


class UserFiles(generic.ListView):
    model = models.File
    template_name = "files/user_file_list.html"

    def get_queryset(self):
        try:
            self.file_user = User.objects.prefetch_related("files").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.file_user.files.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["file_user"] = self.file_user
        return context


class FileDetail(SelectRelatedMixin, generic.DetailView):
    model = models.File
    select_related = ('user', )

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreateFile(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('datafile', 'user')
    model = models.File

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteFile(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.File
    select_related = ('user', )
    success_url = reverse_lazy("files:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "File Deleted")
        return super().delete(*args, **kwargs)

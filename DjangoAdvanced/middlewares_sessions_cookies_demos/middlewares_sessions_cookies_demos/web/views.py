import time
from asyncio import sleep

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views

class MeasureExecuteBeforeRequest:
    def dispatch(self, request, *args, **kwargs):
        start_time = time.time()

        dispatch_result = super().dispatch(request, *args, **kwargs)

        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")

        return dispatch_result

class IndexView(MeasureExecuteBeforeRequest, views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        sleep(5)
        return super().get_context_data(**kwargs)


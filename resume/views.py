from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from . import models
from .forms import ContactForm

class ResumeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        form = ContactForm()
        me = models.PersonalDetail.objects.all().first()
        experience = models.WorkExperience.objects.all()
        skills = models.Skill.objects.all()
        education = models.Education.objects.all()
        project = models.Project.objects.all()

        length = len(skills)//2

        template_data = {'form':form, 'me':me, 'experiences':experience, 'skills_1':skills[:length],
                         'educations':education, 'project':project, 'skills_2':skills[length:]}
        return render(request, self.template_name, template_data)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks, I have received your message')
        # return HttpResponse('Thanks, I have received your message')

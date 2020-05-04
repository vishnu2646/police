from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Police
import uuid
# Create your view(s here.
class HomePageView(View):
    template_name ="police/index.html"
    def get(self,request):
        return render(request,self.template_name)

class AddPoliceView(View):
    template_name ="police/addpolice.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        police = Police()
        police.unique_id =uuid.uuid4()
        police.posting =data['posting']
        police.name = data['name']
        police.station = data['station']
        police.encounters = int(data['encounters'])
        police.save()
        return redirect("view")
        return render(request,self.template_name)

class PoliceView(View):

    template_name ="police/viewpolice.html"
    def get(self,request):
        polices = Police.objects.all()
        return render(request,self.template_name ,{"polices":polices})

class PoliceDeleteView(View):
    def get(self,request,pk):
        police = Police.objects.get(pk=pk)
        police.delete()
        return redirect("view")
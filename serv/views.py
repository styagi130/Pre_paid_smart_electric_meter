from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from serv.models import police
from serv.forms1 import submitRecharge,regForm,loginForm
import socket
host="127.0.0.1"
port=8081
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind((host,port))
#sock.listen(5)
class recharge(TemplateView):
	def get(self,request, *args, **kwargs):
		form1=submitRecharge()
		context={
			"form":form1
		}
		template = "serv/home.html"
		return render(request, template, context)

	def post(self,request,*args, **kwargs):
		form1=submitRecharge(request.POST)
		context={
			"form":form1
		}
		template="serv/home.html"
		if form1.is_valid():
			ip=form1.cleaned_data.get("ip")
			money=form1.cleaned_data.get("money")
			object1=police.objects.get(add=ip)
			print object1.add
			template="serv/done.html"
			if object1:
				object1.add_money(money)
				context={
				"ip":object1.add,
				"money":object1.money
				}
			message=[]

			print "k\n"
			message.append(object1.money)
			print "l\n"
			print "p\n"
			message=str(message)
			while (True):
				sen=sock.sendto("yo",(host,port))
				print host
				if (sen):
					print "done"
					break
				
				sock.close()
		return render(request,template,context)

class register(TemplateView):

	def get(self,request, *args, **kwargs):
		form1=regForm()
		context={"head":'Registration',"form":form1}
		template='serv/register.html'

		return render(request, template, context)
	def post(self,request, *args, **kwargs):
		form1=regForm(request.POST)
		context={
		"form":form1
		}
		template="serv/register.html"
		if form1.is_valid():
			ip=form1.cleaned_data.get("add")
			username=form1.cleaned_data.get("username")
			password=form1.cleaned_data.get("password")
			obj=police()
			obj.user=username
			obj.add=ip
			obj.passwd=password
			obj.save()
			template='serv/registrationdone.html'
			context={'Registration':'Sucessful'}
		return render(request, template, context)
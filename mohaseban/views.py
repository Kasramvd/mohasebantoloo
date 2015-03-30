from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import Context
from django.template.context import Context, RequestContext
from django.template.loader import get_template
#from mohaseban.models import ContactForm
from django.http import HttpResponseRedirect
from mohaseban.forms import NameForm
from django.core.mail import send_mail
from mohaseban.forms import Employee

def main_page(request):

  form_emp = Employee()
  form = NameForm()
  if request.method == 'POST':
  	form = NameForm(request.POST)
  	if form.is_valid():

		message = form.cleaned_data['message']
		sender = form.cleaned_data['sender']
		#cc_myself = form.cleaned_data['cc_myself']

		#recipients = ['kasra.ahmadvand@gmail.com']
		
		#recipients.append(sender)
		send_mail('Mohaseban Tolo',message, sender,[sender])
		return render_to_response(template_name='thankyou.html',context_instance = RequestContext(request))

		template=get_template('index.html')
		variables = Context({
		'head_title': 'Django Bookmarks',
		'page_title': 'Welcome to Django Bookmarks',
		'page_body': 'Where you can store and share bookmarks!',
		'name': form.cleaned_data['your_name'],
		'form': form
		})
		return render_to_response(template_name='thankyou.html',dictionary=variables,context_instance = RequestContext(request))

  if request.method=='POST' and not form.is_valid():

  		form_emp = Employee(request.POST)
  		if form_emp.is_valid():
			resume = form_emp.cleaned_data['resume']
			first_name= form_emp.cleaned_data['first_name']
			last_name = form_emp.cleaned_data['last_name']
			mail = form_emp.cleaned_data['email']
			#cc_myself = form.cleaned_data['cc_myself']

			#recipients = ['kasra.ahmadvand@gmail.com']
			
			#recipients.append(sender)
			send_mail('Mohaseban Tolo',resume, mail,[mail])
			return render_to_response(template_name='thankyou.html',context_instance = RequestContext(request))

			template=get_template('index.html')
			variables = Context({
			'head_title': 'Mohaseban',
			'page_title': 'Welcome to Django Bookmarks',
			'page_body': 'thankyou for employee!',
			'name': form_emp.cleaned_data['first_name'],
			'form_emp': form_emp
			})
			return render_to_response(template_name='thankyou.html',dictionary=variables,context_instance = RequestContext(request))
  
  variables = Context({
	'head_title': 'Django Bookmarks',
	'page_title': 'Welcome to Django Bookmarks',
	'page_body': 'Where you can store and share bookmarks!',
	'form': form,
	'form_emp': form_emp
	})
  return render_to_response(template_name='index.html',dictionary=variables,context_instance = RequestContext(request))


def contactview(request):
		subject = request.POST.get('name', '')
		message = request.POST.get('message', '')
		from_email = request.POST.get('email', '')

		if subject and message and from_email:
		        try:
					send_mail(subject, message, from_email, ['kasra.ahmadvand@gmail.com'])
        		except BadHeaderError:
            			return HttpResponse('Invalid header found.')
        		return HttpResponseRedirect('/contact/thankyou/')
		else:
			return render_to_response('contacts.html', {'form': ContactForm()})
	
		return render_to_response('contacts.html', {'form': ContactForm()},
			RequestContext(request))

def thankyou(request):
		return render_to_response('thankyou.html')


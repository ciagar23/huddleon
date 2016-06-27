from django.shortcuts import render

from .models import Message


def view(request):

	message_list = Message.objects.all()
	return render(request, 'message/index.html',
			{ 'message_list' : message_list })




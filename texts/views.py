from django.shortcuts import render
from django.http import JsonResponse

from . import models
from . import helpers

# Create your views here.
def home(request):
	return render(request, 'texts/home.html', {})

def translate(request):
	context_dict = {
		'success': False,
		'msg': ''
	}
	if request.method == 'POST':
		# Get all data from form
		textToTranslate = request.POST.get('text')
		fromLangCode = request.POST.get('fLang')
		toLangCode = request.POST.get('tLang')
		try:
			# get translation by hitting API
			translation = helpers.GetTextAndTranslate(textToTranslate, 
				fromLangCode, toLangCode)
			# save the translation to database
			new_t = models.Translation(
				text=textToTranslate,
				translatedText=translation,
				toLangCode=toLangCode,
				fromLangCode=fromLangCode)
			new_t.save()
			context_dict['id'] = new_t.id
			context_dict['text'] = new_t.text
			context_dict['translation'] = new_t.translatedText
			context_dict['success'] = True
			context_dict['msg'] = 'Success'

		except Exception as e:
			context_dict['msg'] = str(e)

		return JsonResponse(context_dict)


def error_report(request):
	context_dict = {
		'success': False,
		'msg': ''
	}
	if request.method == 'POST':
		return JsonResponse(context_dict)


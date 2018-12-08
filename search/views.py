# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import SearchForm
import requests
import json

# Create your views here.

api_token = 'a6d35bf0d2e1e36f4de7d54b800fb689'


def home(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			url = 'https://api.themoviedb.org/3/search/movie?api_key='+api_token+'&page=1&'
			query= form.cleaned_data['movie']
			url+='query='+query
			response = requests.get(url)
			data= json.loads(json.dumps(response.json()))
			count = data["total_results"]
			results = data["results"]
			movie_names = {}
			for result in results:
				movie_names[result["vote_count"]]=[result["original_title"],result["id"]]
			movies = []
			for key,value in sorted(movie_names.items(),reverse=True):
				#print "Popularity: "+str(key)+" Movie: "+value[0]+" Id: "+str(value[1]) #print in popularity order
				movies.append(value)
			return render(request, 'index.html', {'form':form, 'movies':movies})

	else:
		form = SearchForm()
		movie_id =request.GET.get("id")
		if movie_id is None:
			pass
		else:
			return redirect("/details.html")
			
	return render(request, 'index.html', {'form':form})

def details(request):
	path=request.path
	path=path[8:]
	url = "https://api.themoviedb.org/3/movie/"+path+"?api_key="+api_token
	response = requests.get(url)
	data= json.loads(json.dumps(response.json()))
	return render(request,"details.html",data)
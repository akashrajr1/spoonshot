# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import SearchForm	#custom made django template 
import requests
import json


#tmdb api token
api_token = 'a6d35bf0d2e1e36f4de7d54b800fb689'

#renders the search page and handles the search functionality
def home(request):
	if request.method == 'POST':	#search is done through post
		form = SearchForm(request.POST)
		if form.is_valid():
			#api search call
			url = 'https://api.themoviedb.org/3/search/movie?api_key='+api_token+'&page=1&'
			query= form.cleaned_data['movie']
			url+='query='+query
			response = requests.get(url)
			data= json.loads(json.dumps(response.json()))
			count = data["total_results"]
			results = data["results"]

			movie_names = {} #data structure is a dict => { popularity : [title,id] }
			for result in results:
				movie_names[result["vote_count"]]=[result["original_title"],result["id"]]

			movies = []	#processed movie details will be stored here and later sent to index.html
			#sorting according to popularity (descending)
			#only the list movies [] => {title,id} is passed to the template
			for key,value in sorted(movie_names.items(),reverse=True):
				#print "Popularity: "+str(key)+" Movie: "+value[0]+" Id: "+str(value[1]) #print in popularity order
				movies.append(value)
			return render(request, 'index.html', {'form':form, 'movies':movies})
	#normal GET request for the page and the search form
	else:
		form = SearchForm()
		movie_id =request.GET.get("id")
		#on a particular movie selection the movie details are generated through movie id in the GET param
		if movie_id is None:	#normal GET request
			pass
		#redirect with id
		else:
			return redirect("/details.html")
			
	return render(request, 'index.html', {'form':form})

#makes api call for movie details based on movie_id passed in the GET request
def details(request):
	path=request.path
	path=path[8:]	#the movie id in form of a number is trimmed here; length of /search/ is 8
	url = "https://api.themoviedb.org/3/movie/"+path+"?api_key="+api_token
	response = requests.get(url)
	data= json.loads(json.dumps(response.json()))	#get json data
	return render(request,"details.html",data)	#json data is sent to template render engine as it is in details.html

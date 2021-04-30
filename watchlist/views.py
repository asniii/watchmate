# from django.http.response import JsonResponse, HttpResponse
# from django.shortcuts import render
#
# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from watchlist.models import Movie
#
#
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(data)
#
# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
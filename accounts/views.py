from django.http import JsonResponse
from django.shortcuts import render
from .models import Part
import re
from django.db import connection
# Create your views here.

# vulnerable code
# def search_parts(request):
#     term = request.GET.get("name")

#     query = "SELECT * FROM parts WHERE name LIKE '%" + term + "%'"

#     print("Running query:", query)

#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         rows = cursor.fetchall()

#     return JsonResponse(list(rows), safe=False)


def parts_search_page(request):
    return render(request, 'parts_search.html')


# SAFE version: backend validation and Django ORM

def search_parts(request):
    term = request.GET.get('name', '').strip()

    if not term:
        return JsonResponse(
            {'error': 'Search term is required'},
            status=400
        )

    if len(term) > 50:
        return JsonResponse(
            {'error': 'Search term must not exceed 50 characters'},
            status=400
        )

    if not re.fullmatch(r'[A-Za-z0-9 ]+', term):
        return JsonResponse(
            {
                'error': (
                    'Search term may only contain letters, '
                    'numbers and spaces'
                )
            },
            status=400
        )

    parts = Part.objects.filter(
        name__icontains=term
    ).values(
        'id',
        'name',
        'price'
    )

    return JsonResponse(list(parts), safe=False)
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
projects = []; clients = []; contacts = []; subscribers = []
def index(request): return render(request, 'core/index.html')
def admin_panel(request): return render(request, 'core/admin.html')
def get_projects(request): return JsonResponse(projects, safe=False)
@csrf_exempt
def add_project(request): data = json.loads(request.body); projects.append(data); return JsonResponse({'status':'project added'})
def get_clients(request): return JsonResponse(clients, safe=False)
@csrf_exempt
def add_client(request): data = json.loads(request.body); clients.append(data); return JsonResponse({'status':'client added'})
@csrf_exempt
def submit_contact(request): data = json.loads(request.body); contacts.append(data); return JsonResponse({'message':'contact received'})
@csrf_exempt
def subscribe_email(request): data = json.loads(request.body); subscribers.append(data['email']); return JsonResponse({'message':'subscribed'})

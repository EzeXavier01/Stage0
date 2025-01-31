from django.http import JsonResponse
from datetime import datetime

def info(request):
    data = {
        'email': 'ezeifeanyichukwu103@gmail.com',
        'current_datetime': datetime.now().isoformat(),
        'github_url': 'https://github.com/EzeXavier01/Stage0'
    }
    return JsonResponse(data)
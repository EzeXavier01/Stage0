from django.http import JsonResponse # type: ignore
from datetime import datetime, timezone

def info(request):
    data = {
        'email': 'ezeifeanyichukwu103@gmail.com',
        'current_datetime':  datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        'github_url': 'https://github.com/EzeXavier01/Stage0'
    }
    return JsonResponse(data)
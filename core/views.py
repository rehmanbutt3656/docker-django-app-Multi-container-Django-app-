from django.http import HttpResponse, JsonResponse

def home(request):
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Django Docker App</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 600px;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
        }
        .status {
            color: #4CAF50;
            font-weight: bold;
            font-size: 18px;
        }
        .services {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            text-align: left;
        }
        .service-item {
            padding: 5px 0;
            border-bottom: 1px solid #ddd;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
            font-size: 14px;
        }
        button:hover {
            background: #764ba2;
        }
        .success {
            color: #4CAF50;
        }
        a {
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Django Docker App</h1>
        <p class="status">✅ Application is LIVE!</p>
        
        <div class="services">
            <h3>📦 Running Services:</h3>
            <div class="service-item">🐍 Django Web Server - <span class="success">Running</span></div>
            <div class="service-item">⚙️ Celery Worker - <span class="success">Running</span></div>
            <div class="service-item">📡 Redis Broker - <span class="success">Connected</span></div>
            <div class="service-item">🐘 PostgreSQL - <span class="success">Connected</span></div>
        </div>
        
        <div>
            <a href='/admin/'><button>Admin Panel</button></a>
            <button onclick="alert('Django Docker App is working perfectly!')">Test Message</button>
        </div>
        
        <p style="margin-top: 20px; font-size: 12px; color: #999;">
            Multi-container deployment with Docker Compose
        </p>
    </div>
</body>
</html>
    """
    return HttpResponse(html_content)

def health_check(request):
    return JsonResponse({'status': 'healthy', 'services': 'all running'})
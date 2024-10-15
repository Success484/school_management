from .views import get_admin_notification

def notifications(request):
    all_notifications, total_notifications = get_admin_notification(request.user)
    return {
        'all_notifications': all_notifications,
        'total_notifications': total_notifications,
    }
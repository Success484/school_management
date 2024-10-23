from .views import get_admin_notification

def notifications(request):
    all_notification, total_notifications = get_admin_notification(request.user)
    return {
        'all_notification': all_notification,
        'total_notifications': total_notifications,
    }
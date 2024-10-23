from .views import get_user_notifications

def notifications(request):
    if request.user.is_authenticated:
        all_notifications, unread_notifications_count = get_user_notifications(request.user)
        return {
            'all_notifications': all_notifications,
            'unread_notifications_count': unread_notifications_count,
        }
    return {
        'all_notifications': [],
        'unread_notifications_count': 0,
    }
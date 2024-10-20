from .views import get_user_notifications

def notifications(request):
    notifications, grade_notifications, unread_notifications_count = get_user_notifications(request.user.id)
    return {
        'notifications': notifications,
        'unread_notifications_count': unread_notifications_count,
        'grade_notifications': grade_notifications,
    }
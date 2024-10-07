# from django.contrib.auth.models import Group
# from django.contrib.auth import get_user_model

# User = get_user_model()

# # Get the groups
# student_group, _ = Group.objects.get_or_create(name='Student')
# teacher_group, _ = Group.objects.get_or_create(name='Teacher')

# # Assuming you have users to add
# users_to_add = User.objects.filter(is_active=True)

# for user in users_to_add:
#     if not user.groups.filter(name='Student').exists():
#         student_group.user_set.add(user) 
#     if not user.groups.filter(name='Teacher').exists():
#         teacher_group.user_set.add(user)  

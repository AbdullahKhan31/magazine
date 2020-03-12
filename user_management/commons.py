import pdb


# Check if user is from admin group
def has_admin_group(user):
    if user:
        return user.groups.filter(name='Admins').count() > 0
    return False


# Check if user is from admin group
def has_tutor_group(user):
    if user:
        return user.groups.filter(name='Tutors').count() > 0
    return False
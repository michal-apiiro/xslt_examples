from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

class NameClass(API):
    var_permissions = [permissions.IsAuthenticated]
    


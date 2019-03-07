from app01.models import Token, User
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.throttling import BaseThrottle


# 认证
class AuthToken(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('认证失败')
        return token_obj.user.username, token_obj.token



# 在检查权限之前，就已经经过了认证处理，认证处理获取的2个值，已经存在request中了，能获取，用来验证权限
# request.user = token_obj.user.username,
# request.auth = request.token_obj.token
# 权限
class SVIPPermission(BasePermission):
    def has_permission(self, request, view):
        username = request.user
        user_type = User.objects.filter(username=username).first().user_type

        if user_type == 3:
            return True
        else:
            return False



# 频率
import time
# 访问记录
visit_recode = {}
class Thorttle(BaseThrottle):
    def __iter__(self):
        self.history = None

    def allow_request(self, request, view):
        # 获取访问端的ip
        remote_add = self.get_ident(request)
        # 当前时间
        ctime = time.time()
        # 如果当前ip不在访问记录里，则添加到访问记录中
        if remote_add not in visit_recode:
            visit_recode[remote_add] = [ctime,]
            return True
        # 获取当前ip的访问记录
        history = visit_recode[remote_add]
        # 初始化访问记录
        self.history = history

        # 如果有访问记录，并且最早一次的访问记录离当前时间超过60s，就删除最早的那个访问记录，
        # 一直循环删除
        while history and history[-1] < ctime - 60:
            history.pop()

        # 如果访问记录小于3次，就将当前访问记录插到第一个位置
        if len(history) < 3:
            history.insert(0, ctime)
            return True

    def wait(self):
        # 还需要等多久才能访问
        ctime = time.time()
        return 60 - (ctime - self.history[-1])


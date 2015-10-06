from rest_framework import routers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import views


class ApiRouter(routers.DefaultRouter):

    def __init__(self, *args, **kwargs):
        super(ApiRouter, self).__init__(*args, **kwargs)

        self.trailing_slash = "/?"

    def get_api_root_view(self):
        """
        Return a view to use as the API root.
        """

        from django.core.urlresolvers import NoReverseMatch
        from rest_framework import views

        api_root_dict = {}
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        class APIRoot(views.APIView):
            _ignore_model_permissions = True

            def get(self, request, format=None):
                ret = {}
                for key, url_name in api_root_dict.items():
                    try:
                        ret[key] = reverse(url_name, request=request,
                                           format=format)
                    except NoReverseMatch:
                        pass
                return Response(ret)

        return APIRoot.as_view()

router = ApiRouter()

router.register(r"photos", views.PhotoViewSet)
router.register(r"menus", views.MenuViewSet)
router.register(r"comments", views.CommentViewSet)

urlpatterns = router.urls

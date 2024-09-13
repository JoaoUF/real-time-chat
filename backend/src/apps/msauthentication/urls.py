from django.urls import path, include
from msauthentication.views import GoogleLogin, CustomUserListAvailable

urlpatterns = [
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google_login"),
    path(
        "custom-user/available/",
        CustomUserListAvailable.as_view(),
        name="custom-user-available",
    ),
]

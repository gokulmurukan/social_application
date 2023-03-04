from django.urls import path
from postweb import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('',views.LogInView.as_view(),name="signin"),
    path('home/',views.HomeView.as_view(),name="index"),
    path('createprofile/',views.ProfileCreateView.as_view(),name="profile_create"),
    path('profile/<int:id>/',views.ProfileView.as_view(),name="profile_detail"),
    path('profile/<int:id>/change/',views.ProfileEditView.as_view(),name="profile_edit"),
    path('profile/<int:id>/revome/',views.UserProfileDeleteView.as_view(),name="profile_delete"),
    path('posts/<int:id>/comment/add/',views.AddCommentsView.as_view(),name="cmt_add"),
    path('post/<int:id>/remove/',views.PostDeleteView.as_view(),name="delete_post"),
    path('comments/<int:id>/remove/',views.CommentsDeleteView.as_view(),name="delete_comment"),
    path('comment/<int:id>/upvote/add/',views.CommentUpvoteView.as_view(),name="c_upvote_add"),
    path('comment/<int:id>/upvote/remove/',views.CommentUpvoteRemoveView.as_view(),name="c_upvote_remove"),
    path('post/<int:id>/like/add/',views.PostUpvoteView.as_view(),name="p_upvote_add"),
    path('post/<int:id>/dislike/remove/',views.PostUpvoteRemoveView.as_view(),name="p_upvote_remove"),
    path('signout/',views.LogOutView.as_view(),name="signout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
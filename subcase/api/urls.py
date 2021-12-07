from django.urls import path
from subcase.api import views as api_view



urlpatterns = [
    # get all users
    path('users/', api_view.user_list_create_api_view, name="user-listesi" ),
    # get selected user
    path('users/<int:pk>', api_view.user_list_create_api_view, name="user" ),
    # get organizations
    path('organizations/', api_view.organization_list_create_api_view, name="organization-listesi" ),
    # get selected organization
    path('organizations/<int:pk>', api_view.organization_list_create_api_view, name="organization" ),
    # get users in selected organizations
    path('<slug:organization_slug>/users/', api_view.organization_2_users_list_view, name="organization-users" ),
    # # get user in selected organizations
    path('<slug:organization_slug>/users/<int:pk>', api_view.organization_2_users_list_view, name="organization-user" ),
    # get token
    path('token/<slug:organization_slug>/users/<int:pk>', api_view.genarate_user_token, name="genarate-user-token" ),
    # get deposit for user
    path('deposit/<slug:organization_slug>/users/<int:pk>', api_view.transaction_deposit, name="get-deposit-for-user" ),



]
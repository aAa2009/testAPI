import requests
import pytest
from Environment.env import Env
from Test_data.test_data_json import Credentials
from Test_data.test_data_json import Users
from Test_data.parameters import Parameters
import Results.GET.actual_result_get as ar_get
import Results.GET.expected_result_get as er_get
import Results.POST.actual_result_post as ar_post
import Results.POST.expected_result_post as er_post
import Results.PUT.actual_result_put as ar_put
import Results.PUT.expected_result_put as er_put
import Results.PATCH.actual_result_patch as ar_patch
import Results.PATCH.expected_result_patch as er_patch
import Results.DELETE.actual_result_delete as ar_delete
import Results.DELETE.expected_result_delete as er_delete


@pytest.mark.regression
class TestCases:

    @pytest.mark.smoke
    def test_get_list_users(self):
        url = f'{Env.baseurl}api/users?page={Parameters.page}'
        response = requests.get(url)
        expected_result = er_get.base_expected_result() | er_get.base_expected_result_get_list() | er_get.base_expected_result_get_user() | er_get.base_expected_result_support() | {"page": 2}
        actual_result = ar_get.base_actual_result(response) | ar_get.base_actual_result_get_list(response) | ar_get.base_actual_result_get_user(response) | ar_get.base_actual_result_support(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_get_single_user(self):
        url = f'{Env.baseurl}api/users/{Parameters.id_for_user}'
        response = requests.get(url)
        expected_result = er_get.base_expected_result() | er_get.base_expected_result_support() | er_get.expected_result_for_user()
        actual_result = ar_get.base_actual_result(response) | ar_get.base_actual_result_support(response) | ar_get.actual_result_for_user(response)
        assert expected_result == actual_result

    def test_get_user_not_founded(self):
        url = f'{Env.baseurl}api/users/{Parameters.incorrect_id}'
        response = requests.get(url)
        expected_result = er_get.expected_result_for_get_404()
        actual_result = ar_get.actual_result_for_get_404(response)
        assert expected_result == actual_result

    def test_get_list_resources(self):
        url = f'{Env.baseurl}api/unknown'
        response = requests.get(url)
        expected_result = er_get.base_expected_result() | er_get.base_expected_result_get_list() | er_get.base_expected_result_get_resource() | er_get.base_expected_result_support() | {"page": 1}
        actual_result = ar_get.base_actual_result(response) | ar_get.base_actual_result_get_list(response) | ar_get.base_actual_result_get_resource(response) | ar_get.base_actual_result_support(response)
        assert expected_result == actual_result

    def test_get_single_resource(self):
        url = f'{Env.baseurl}api/unknown/{Parameters.id_for_resource}'
        response = requests.get(url)
        expected_result = er_get.base_expected_result() | er_get.base_expected_result_support() | er_get.expected_result_for_resource()
        actual_result = ar_get.base_actual_result(response) | ar_get.base_actual_result_support(response) | ar_get.actual_result_for_resource(response)
        assert expected_result == actual_result

    def test_get_resource_not_founded(self):
        url = f'{Env.baseurl}api/unknown/{Parameters.incorrect_id_for_resource}'
        response = requests.get(url)
        expected_result = er_get.expected_result_for_get_404()
        actual_result = ar_get.actual_result_for_get_404(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_create_user(self):
        url = f'{Env.baseurl}api/users'
        response = requests.post(url, json=Users.new_user)
        expected_result = er_post.base_expected_result_for_create() | er_post.expected_result_for_successful_create_user(Users.new_user)
        actual_result = ar_post.base_actual_result(response) | ar_post.actual_result_for_successful_create_user(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_rewrite_user(self):
        url = f'{Env.baseurl}api/users/{Parameters.id_for_user}'
        response = requests.put(url, json=Users.updated_user)
        expected_result = er_put.base_expected_result_for_rewrite() | er_put.expected_result_for_successful_rewrite_user(Users.updated_user)
        actual_result = ar_put.base_actual_result(response) | ar_put.actual_result_for_successful_rewrite_user(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_update_user(self):
        url = f'{Env.baseurl}api/users/{Parameters.id_for_user}'
        response = requests.patch(url, json=Users.updated_user)
        expected_result = er_patch.base_expected_result_for_update() | er_patch.expected_result_for_successful_update_user(Users.updated_user)
        actual_result = ar_patch.base_actual_result(response) | ar_patch.actual_result_for_successful_update_user(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_delete_user(self):
        url = f'{Env.baseurl}api/users/{Parameters.id_for_user}'
        response = requests.delete(url)
        expected_result = er_delete.base_expected_result_for_delete()
        actual_result = ar_delete.base_actual_result(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_register_successful(self):
        url = f'{Env.baseurl}api/register'
        response = requests.post(url, json=Credentials.tru_credentials_1)
        expected_result = er_post.base_expected_result_for_register() | er_post.base_expected_result_for_register_successful()
        actual_result = ar_post.base_actual_result(response) | ar_post.actual_result_for_register_successful(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_register_without_password(self):
        url = f'{Env.baseurl}api/register'
        response = requests.post(url, json=Credentials.false_credentials_1)
        expected_result = er_post.base_expected_result_for_register_without_password()
        actual_result = ar_post.base_actual_result(response) | ar_post.actual_result_for_register_without_password(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_login_successful(self):
        url = f'{Env.baseurl}api/login'
        response = requests.post(url, json=Credentials.tru_credentials_2)
        expected_result = er_post.base_expected_result_for_register() | er_post.base_expected_result_for_login_successful()
        actual_result = ar_post.base_actual_result(response) | ar_post.actual_result_for_login_successful(response)
        assert expected_result == actual_result

    @pytest.mark.smoke
    def test_login_without_password(self):
        url = f'{Env.baseurl}api/login'
        response = requests.post(url, json=Credentials.false_credentials_2)
        expected_result = er_post.base_expected_result_for_login_without_password()
        actual_result = ar_post.base_actual_result(response) | ar_post.actual_result_for_login_without_password(response)
        assert expected_result == actual_result

from Const.const import Const


def base_expected_result_for_create():
    expected_result = {
                       "status_code": 201,
                       "content-type": "application/json; charset=utf-8"
                       }
    return expected_result


def base_expected_result_for_register():
    expected_result = {
                       "status_code": 200,
                       "content-type": "application/json; charset=utf-8"
                       }
    return expected_result


def base_expected_result_for_register_successful():
    expected_result = {
                       "id": True,
                       "token": True,
                       "register_len": Const.register_len
                       }
    return expected_result


def expected_result_for_successful_create_user(data):
    name = data["name"]
    job = data["job"]
    expected_result = {
                       "name": name,
                       "job": job,
                       "id": True,
                       "createdAt": True,
                       "user_len": Const.user_len
                       }
    return expected_result


def base_expected_result_for_register_without_password():
    expected_result = {
                       "status_code": 400,
                       "content-type": "application/json; charset=utf-8",
                       "error": "Missing password"
                       }
    return expected_result


def base_expected_result_for_login_successful():
    expected_result = {
                       "token": True,
                       "login_len": Const.login_len
                       }
    return expected_result


def base_expected_result_for_login_without_password():
    expected_result = {
                       "status_code": 400,
                       "content-type": "application/json; charset=utf-8",
                       "error": "Missing password"
                       }
    return expected_result

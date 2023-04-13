from Const.const import Const


def base_expected_result_for_rewrite():
    expected_result = {
                       "status_code": 200,
                       "content-type": "application/json; charset=utf-8"
                       }
    return expected_result


def expected_result_for_successful_rewrite_user(data):
    name = data["name"]
    job = data["job"]
    expected_result = {
                       "name": name,
                       "job": job,
                       "updatedAt": True,
                       "user_len": Const.user_update_len
                       }
    return expected_result

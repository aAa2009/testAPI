from Const.const import Const
from Test_data.parameters import Parameters


def base_expected_result():
    expected_result = {
                       "status_code": 200,
                       "content-type": "application/json; charset=utf-8"
                       }
    return expected_result


def base_expected_result_get_list():
    expected_result = {
                       "per_page": Const.per_page,
                       "total": True,
                       "total_pages": True,
                       "data": True
                       }
    return expected_result


def base_expected_result_get_user():
    expected_result = {
                       "id": True,
                       "email": True,
                       "first_name": True,
                       "last_name": True,
                       "avatar": True,
                       "data_len": Const.data_len
                       }
    return expected_result


def base_expected_result_support():
    expected_result = {
                       "support": True,
                       "url": "https://reqres.in/#support-heading",
                       "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
                       "support_len": Const.support_len
                       }
    return expected_result


def expected_result_for_user():
    expected_result = {
                       "id": Parameters.id_for_user,
                       "email": "janet.weaver@reqres.in",
                       "first_name": "Janet",
                       "last_name": "Weaver",
                       "avatar": "https://reqres.in/img/faces/2-image.jpg",
                       "status_code": 200,
                       "content-type": "application/json; charset=utf-8",
                       "data_len": Const.data_len
                       }
    return expected_result


def expected_result_for_get_404():
    expected_result = {
                       "status_code": 404,
                       "content-type": "application/json; charset=utf-8",
                       "data_len": 0
                       }
    return expected_result


def base_expected_result_get_resource():
    expected_result = {
                       "id": True,
                       "name": True,
                       "year": True,
                       "color": True,
                       "pantone_value": True,
                       "data_len": Const.data_len
                       }
    return expected_result


def expected_result_for_resource():
    expected_result = {
                       "id": Parameters.id_for_resource,
                       "name": "fuchsia rose",
                       "year": 2001,
                       "color": "#C74375",
                       "pantone_value": "17-2031",
                       "data_len": Const.data_len
                       }
    return expected_result

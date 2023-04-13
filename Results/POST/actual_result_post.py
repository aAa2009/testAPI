def base_actual_result(response):
    status_code = response.status_code
    content_type = response.headers["Content-Type"]
    actual_result = {
                     "status_code": status_code,
                     "content-type": content_type
                     }
    return actual_result


def actual_result_for_successful_create_user(response):
    response_body = response.json()
    name = response_body["name"]
    job = response_body["job"]
    id = "id" in response_body
    created_at = "createdAt" in response_body
    user_len = len(response_body)
    actual_result = {
                     "name": name,
                     "job": job,
                     "id": id,
                     "createdAt": created_at,
                     "user_len": user_len
                     }
    return actual_result


def actual_result_for_register_successful(response):
    response_body = response.json()
    id = "id" in response_body
    token = "token" in response_body
    register_len = len(response_body)
    actual_result = {
                     "id": id,
                     "token": token,
                     "register_len": register_len
                     }
    return actual_result


def actual_result_for_register_without_password(response):
    response_body = response.json()
    error = response_body["error"]
    actual_result = {
                     "error": error
                     }
    return actual_result


def actual_result_for_login_successful(response):
    response_body = response.json()
    token = "token" in response_body
    login_len = len(response_body)
    actual_result = {
                     "token": token,
                     "login_len": login_len
                     }
    return actual_result


def actual_result_for_login_without_password(response):
    response_body = response.json()
    error = response_body["error"]
    actual_result = {
                     "error": error
                     }
    return actual_result

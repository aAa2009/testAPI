def base_actual_result(response):
    status_code = response.status_code
    content_type = response.headers["Content-Type"]
    actual_result = {
                     "status_code": status_code,
                     "content-type": content_type
                     }
    return actual_result


def actual_result_for_successful_update_user(response):
    response_body = response.json()
    name = response_body["name"]
    job = response_body["job"]
    updated_at = "updatedAt" in response_body
    user_len = len(response_body)
    actual_result = {
                     "name": name,
                     "job": job,
                     "updatedAt": updated_at,
                     "user_len": user_len
                     }
    return actual_result
def base_actual_result(response):
    status_code = response.status_code
    content_length = response.headers["Content-Length"]
    actual_result = {
                     "status_code": status_code,
                     "Content-Length": content_length
                     }
    return actual_result

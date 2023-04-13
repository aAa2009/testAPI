def base_actual_result(response):
    status_code = response.status_code
    content_type = response.headers["Content-Type"]
    actual_result = {
                     "status_code": status_code,
                     "content-type": content_type
                     }
    return actual_result


def base_actual_result_get_list(response):
    response_body = response.json()
    page = response_body["page"]
    per_page = response_body["per_page"]
    total = "per_page" in response_body
    total_pages = "total_pages" in response_body
    data = "data" in response_body
    actual_result = {
                     "page": page,
                     "per_page": per_page,
                     "total": total,
                     "total_pages": total_pages,
                     "data": data
                     }
    return actual_result


def base_actual_result_get_user(response):
    response_body = response.json()
    user_data = response_body["data"][0]
    id = "id" in user_data
    email = "email" in user_data
    first_name = "first_name" in user_data
    last_name = "last_name" in user_data
    avatar = "avatar" in user_data
    data_len = len(user_data)
    actual_result = {
                     "id": id,
                     "email": email,
                     "first_name": first_name,
                     "last_name": last_name,
                     "avatar": avatar,
                     "data_len": data_len
                     }
    return actual_result


def base_actual_result_support(response):
    response_body = response.json()
    support_data = response_body["support"]
    support = "support" in response_body
    url = support_data["url"]
    text = support_data["text"]
    support_len = len(support_data)
    actual_result = {
                     "support": support,
                     "url": url,
                     "text": text,
                     "support_len": support_len
                     }
    return actual_result


def actual_result_for_user(response):
    response_body = response.json()
    user_data = response_body["data"]
    id = user_data["id"]
    email = user_data["email"]
    first_name = user_data["first_name"]
    last_name = user_data["last_name"]
    avatar = user_data["avatar"]
    data_len = len(user_data)
    actual_result = {
                     "id": id,
                     "email": email,
                     "first_name": first_name,
                     "last_name": last_name,
                     "avatar": avatar,
                     "data_len": data_len
                     }
    return actual_result


def actual_result_for_get_404(response):
    response_body = response.json()
    status_code = response.status_code
    content_type = response.headers["Content-Type"]
    data_len =len(response_body)
    actual_result = {
                     "status_code": status_code,
                     "content-type": content_type,
                     "data_len": data_len
                     }
    return actual_result


def base_actual_result_get_resource(response):
    response_body = response.json()
    user_data = response_body["data"][0]
    id = "id" in user_data
    name = "name" in user_data
    year = "year" in user_data
    color = "color" in user_data
    pantone_value = "pantone_value" in user_data
    data_len = len(user_data)
    actual_result = {
                     "id": id,
                     "name": name,
                     "year": year,
                     "color": color,
                     "pantone_value": pantone_value,
                     "data_len": data_len
                     }
    return actual_result


def actual_result_for_resource(response):
    response_body = response.json()
    user_data = response_body["data"]
    id = user_data["id"]
    name = user_data["name"]
    year = user_data["year"]
    color = user_data["color"]
    pantone_value = user_data["pantone_value"]
    data_len = len(user_data)
    actual_result = {
                     "id": id,
                     "name": name,
                     "year": year,
                     "color": color,
                     "pantone_value": pantone_value,
                     "data_len": data_len
                     }
    return actual_result

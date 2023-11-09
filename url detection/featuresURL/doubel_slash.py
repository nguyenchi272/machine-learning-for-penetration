# Hàm kiểm tra vị trí cuối cùng của chuỗi "//" trong URL
def last_double_slash_position(url):
    last_position = url.rfind("//")
    return last_position

# Hàm đánh giá URL dựa trên quy tắc


def evaluate_url(url):
    last_slash_position = last_double_slash_position(url)
    if last_slash_position > 7:
        return "Phishing"
    else:
        return "Legitimate"


# Ví dụ sử dụng hàm đánh giá URL dựa trên quy tắc
url1 = "http://example.com"
result1 = evaluate_url(url1)
print("Result for", url1, ":", result1)  # Kết quả: Legitimate

url2 = "http://www.legitimate.com//http://www.phishing.com"
result2 = evaluate_url(url2)
print("Result for", url2, ":", result2)  # Kết quả: Phishing

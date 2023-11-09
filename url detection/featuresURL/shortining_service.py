import requests

# Hàm kiểm tra xem một URL có phải là TinyURL hay không


def is_tiny_url(url):
    response = requests.head(url)  # Gửi yêu cầu HEAD để kiểm tra redirection
    return "Location" in response.headers and "tinyurl.com" in response.headers["Location"]

# Hàm đánh giá URL dựa trên quy tắc


def evaluate_url(url):
    if is_tiny_url(url):
        return "Phishing"
    else:
        return "Legitimate"


# Ví dụ sử dụng hàm đánh giá URL dựa trên quy tắc
url1 = "http://portal.hud.ac.uk/"
result1 = evaluate_url(url1)
print("Result for", url1, ":", result1)  # Kết quả: Legitimate

url2 = "http://tinyurl.com/abcdef"
result2 = evaluate_url(url2)
print("Result for", url2, ":", result2)  # Kết quả: Phishing

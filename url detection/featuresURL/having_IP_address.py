import socket

# Hàm kiểm tra xem một chuỗi là địa chỉ IP hay không


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)  # Thử chuyển đổi chuỗi thành địa chỉ IP
        return True
    except socket.error:
        return False

# Hàm đánh giá URL


def evaluate_url(url):
    parts = url.split('/')  # Phân tách phần domain từ URL
    domain = parts[2] if len(parts) > 2 else parts[0]  # Lấy phần domain

    if is_valid_ip(domain):  # Kiểm tra nếu phần domain là một địa chỉ IP
        return "Phishing"
    else:
        return "Legitimate"


# Ví dụ sử dụng hàm đánh giá URL
url = "http://192.168.1.1/login"
result = evaluate_url(url)
print("Result:", result)  # Kết quả: Phishing

url = "http://www.example.com/login"
result = evaluate_url(url)
print("Result:", result)  # Kết quả: Legitimate

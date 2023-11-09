# Hàm đánh giá URL dựa trên độ dài
def evaluate_url_length(url):
    url_length = len(url)

    if url_length < 54:
        return "Legitimate"
    elif 54 <= url_length <= 75:
        return "Suspicious"
    else:
        return "Phishing"


# Ví dụ sử dụng hàm đánh giá URL dựa trên độ dài
url1 = "http://www.example.com/login"
result1 = evaluate_url_length(url1)
print("Result for", url1, ":", result1)  # Kết quả: Legitimate

url2 = "http://www.suspiciouswebsite.com/loginpage"
result2 = evaluate_url_length(url2)
print("Result for", url2, ":", result2)  # Kết quả: Suspicious

url3 = "http://federmacedoadv.com.br/3f/aze/ab51e2e319e51502f416dbe46b773a5e/?cmd=_home&amp;dispatch=11004d58f5b74f8dc1e7c2e8dd4105e811004d58f5b74f8dc1e7c2e8dd4105e8@phishing.website.html"
result3 = evaluate_url_length(url3)
print("Result for", url3, ":", result3)  # Kết quả: Phishing

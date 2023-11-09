# Hàm kiểm tra xem một URL có chứa ký tự "@" hay không
def has_at_symbol(url):
    return "@" in url

# Hàm đánh giá URL dựa trên quy tắc


def evaluate_url(url):
    if has_at_symbol(url):
        return "Phishing"
    else:
        return "Legitimate"


# Ví dụ sử dụng hàm đánh giá URL dựa trên quy tắc
url1 = "http://example.com"
result1 = evaluate_url(url1)
print("Result for", url1, ":", result1)  # Kết quả: Legitimate

url2 = "http://username:password@example.com"
result2 = evaluate_url(url2)
print("Result for", url2, ":", result2)  # Kết quả: Phishing

# Hàm kiểm tra xem phần domain của URL có chứa ký tự "-" hay không
def has_hyphen_in_domain(url):
    domain_start = url.find("//") + 2  # Tìm vị trí bắt đầu của domain
    domain_end = url.find("/", domain_start)  # Tìm vị trí kết thúc của domain
    domain = url[domain_start:domain_end]  # Lấy phần domain của URL
    return "-" in domain

# Hàm đánh giá URL dựa trên quy tắc


def evaluate_url(url):
    if has_hyphen_in_domain(url):
        return "Phishing"
    else:
        return "Legitimate"


# Ví dụ sử dụng hàm đánh giá URL dựa trên quy tắc
url1 = "http://example.com"
result1 = evaluate_url(url1)
print("Result for", url1, ":", result1)  # Kết quả: Legitimate

url2 = "http://example-domain.com"
result2 = evaluate_url(url2)
print("Result for", url2, ":", result2)  # Kết quả: Phishing

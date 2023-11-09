# Hàm kiểm tra số lượng subdomain trong URL
def count_subdomains(url):
    # Loại bỏ "www." và "http://", sau đó tách phần domain
    domain = url.replace("www.", "").replace("http://", "").split("/")[0]
    # Tách subdomain bằng dấu chấm và đếm số lượng subdomain
    subdomains = domain.split(".")
    return len(subdomains) - 1  # Trừ 1 để loại bỏ domain chính

# Hàm đánh giá URL dựa trên quy tắc


def evaluate_url(url):
    subdomain_count = count_subdomains(url)
    if subdomain_count <= 2:
        return "Legitimate"
    elif subdomain_count == 3:
        return "Suspicious"
    else:
        return "Phishing"


# Ví dụ sử dụng hàm đánh giá URL dựa trên quy tắc
url1 = "http://hud.ac.uk/students/"
result1 = evaluate_url(url1)
print("Result for", url1, ":", result1)  # Kết quả: Suspicious

url2 = "http://www.hud.ac.uk/students/"
result2 = evaluate_url(url2)
print("Result for", url2, ":", result2)  # Kết quả: Legitimate

url3 = "http://sub.domain.hud.ac.uk/students/"
result3 = evaluate_url(url3)
print("Result for", url3, ":", result3)  # Kết quả: Phishing

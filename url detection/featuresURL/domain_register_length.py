import whois


def is_phishing_domain(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        expiration_date = domain_info.expiration_date
        if expiration_date and (expiration_date - domain_info.creation_date).days <= 365:
            return True  # Domain hết hạn trong vòng 1 năm, có thể là lừa đảo
        return False
    except Exception as e:
        print("Error:", e)
        return False


# Ví dụ sử dụng
domain_name = "https://www.bet365.com/"
is_phishing = is_phishing_domain(domain_name)
if is_phishing:
    print(domain_name, "là tên miền lừa đảo.")
else:
    print(domain_name, "không phải là tên miền lừa đảo.")

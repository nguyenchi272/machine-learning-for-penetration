from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime
import socket
import ssl
from urllib.parse import urlparse


def get_ssl_certificate_info(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.connect((hostname, 443))
            der_cert = sock.getpeercert(True)
            x509_cert = x509.load_der_x509_certificate(
                der_cert, default_backend())
            issue_date = x509_cert.not_valid_before
            expiration_date = x509_cert.not_valid_after
            if (expiration_date - issue_date).days > 360:
                return True
            else:
                return False
    except Exception as e:
        print("Error:", e)
        return None, None


def check_protocol(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == 'https':
        return True
    else:
        return False


# Ví dụ sử dụng
url = "https://i88.io/"
isTrusted = get_ssl_certificate_info(url)
isHTPPS = check_protocol(url)
if isTrusted and isHTPPS:
    print(url, ": Legitimate")
elif isHTPPS and not isTrusted:
    print(url, ": Suspicious")
else:
    print(url, ": Phishing")

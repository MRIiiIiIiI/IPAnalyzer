
from analyzer import IPAnalyzer, extract_ip

user_input = input(">> Enter your IP address (e.g., 192.168.1.1): ")
ip_parts = extract_ip(user_input)

if ip_parts is None:
    print("Invalid IP address format.")
else:
    ip_analyzer = IPAnalyzer(ip_parts)
    ip_analyzer.analyze_ip()
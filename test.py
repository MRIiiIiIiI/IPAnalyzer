
from IPAnalyzer import *

question = input("Do you want to know the IP address or make groups? ")

if question.lower() == "know ip":
    user_input = input(">> Enter your IP address (e.g., 192.168.1.1): ")
    ip_parts = extract_ip(user_input)
    if ip_parts is None:
        print("Invalid IP address format.")
    ip_analyzer = IPAnalyzer(ip_parts)
    ip_analyzer.analyze_ip()
elif question.lower() == "make groups":
    dividing_instance = Dividing()
    dividing_instance.run()
else:
    print("Invalid choice.")

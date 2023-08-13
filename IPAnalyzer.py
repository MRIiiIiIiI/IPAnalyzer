from art import *

class IPAnalyzer:
    CLASS_A_MIN, CLASS_A_MAX = 1, 127
    CLASS_B_MIN, CLASS_B_MAX = 128, 191
    CLASS_C_MIN, CLASS_C_MAX = 192, 223
    #when you strat working or paly this code this must first thing  strat to make oop
    def __init__(self, ip_parts):
        #this to take ip form user in end of this code
        self.ip_parts = ip_parts

    #this to show subnet mask of prefix
    def calculate_subnet_mask(self, prefix):
        network_bits = "1" * prefix
        host_bits = "0" * (32 - prefix)
        subnet_mask_bin = network_bits + host_bits
        subnet_mask_decimal = ".".join(str(int(subnet_mask_bin[i:i+8], 2)) for i in range(0, 32, 8))
        return subnet_mask_decimal

    def calculate_Network_ID_broadcast_address(self,ip_parts, prefix):
        # ip address
        ip_parts1 = str(ip_parts[0])+'.'+str(ip_parts[1])+'.'+str(ip_parts[2])+'.'+str(ip_parts[3])
        # convert ip to binary
        ip_parts2=ip_parts1.split('.')
        binary_ip = ''.join([bin(int(part))[2:].zfill(8) for part in ip_parts2])
        # Calculate Network ID and Broadcast Address in binary
        network_id_binary = binary_ip[:prefix] + '0' * (32 - prefix)
        broadcast_binary = binary_ip[:prefix] + '1' * (32 - prefix)
        # Convert Network ID and Broadcast Address to decimal
        network_id_parts = [network_id_binary[i:i + 8] for i in range(0, len(network_id_binary), 8)]
        broadcast_parts = [broadcast_binary[i:i + 8] for i in range(0, len(broadcast_binary), 8)]
        network_id_decimal = '.'.join([str(int(part, 2)) for part in network_id_parts])
        broadcast_decimal = '.'.join([str(int(part, 2)) for part in broadcast_parts])
        # print Network ID and Broadcast Address
        print(f"Network ID: {network_id_decimal}")
        print(f"Broadcast Address: {broadcast_decimal}")

    def calculate_hosts_count(self,perfix):
        return 2 ** (32 - perfix) - 2
    def calculate_Network_count(self,perfix):
        Network_bin='1' * (perfix)
        Network_part=[int(Network_bin[i:i + 8],2) for i in range(0, len(Network_bin), 8)]
        Network_decma=sum(Network_part)
        return Network_decma

    def INFO(self,perfix_input):
        if 0 < perfix_input <= 32:
            self.calculate_Network_ID_broadcast_address(ip, perfix_input)
            subnet_mask = self.calculate_subnet_mask(perfix_input)
            Hosts = self.calculate_hosts_count(perfix_input)
            Network = self.calculate_Network_count(perfix_input)
            print(f"Subnet Mask of perfix: {subnet_mask}")
        else:
            print("Prefix not found.")
        print("Number of Network of this prefix:",Network)
        print("Number of Hosts Per Network of this prefix:",Hosts)

        return perfix_input
    def right_perfix(self,perfix_input):
        contiue = input("Notice this perfix not in the range do u want to continue or not (y/n)")
        if contiue == 'y':
            self.INFO(perfix_input)
        elif contiue == 'n':
            run_agin = input("do u want run again or not(y/n)")
            if run_agin == 'y':
                self.analyze()
            elif run_agin == 'n':
                print("good bye")
    def analyze(self):
        if self.CLASS_A_MIN <= self.ip_parts[0] <= self.CLASS_A_MAX:
            if self.ip_parts[0] == 127 and all(0 <= part <= 255 for part in self.ip_parts[1:]):
                self.class_C()
            else:
                self.class_A()
        elif self.CLASS_B_MIN <= self.ip_parts[0] <= self.CLASS_B_MAX:
            self.class_B()
        elif self.CLASS_C_MIN <= self.ip_parts[0] <= self.CLASS_C_MAX:
            self.class_C()

    def class_A(self):
        perfix_input = int(input("Enter your prefix (1-32): "))
        if 1 <= perfix_input <= 32:
            print("Class A")
            self.INFO(perfix_input)
        elif 1 >= perfix_input <= 32:
            print("Class A")
            self.right_perfix(perfix_input)
        if self.ip_parts[0] == 10:
            if all(0 <= part <= 255 for part in self.ip_parts[1:]):
                print("This IP is a private IP")
            else:
                print("Error 404")

        elif all(0 <= part <= 255 for part in self.ip_parts[1:]):
            print("This IP is a public IP")
        else:
            self.class_B()

    def class_B(self):
        perfix_input = int(input("Enter your prefix (16-32): "))
        if 16 <= perfix_input <= 32:
            print("Class B")
            self.INFO(perfix_input)
        elif 16 >= perfix_input <= 32:
            print("Class B")
            self.right_perfix(perfix_input)
        if self.ip_parts[0] == 172:
            if 16 <= self.ip_parts[1] <= 31 and all(0 <= part <= 255 for part in self.ip_parts[2:]):
                print("This IP is a private IP")
            else:
                print("This IP is a public IP")
        elif all(0 <= part <= 255 for part in self.ip_parts[1:]):
            print("This IP is a public IP")

    def class_C(self):
        perfix_input = int(input("Enter your prefix (24-32): "))
        if 24<= perfix_input <=32:
            print("Class C")
            self.INFO(perfix_input)
        elif 24>=perfix_input<=32:
            print("Class C")
            self.right_perfix(perfix_input)
        if self.ip_parts[0] == 192:
            if self.ip_parts[1] == 168 and all(0 <= part <= 255 for part in self.ip_parts[2:]):
                print("This IP is a private IP")
            else:
                print("This IP is a public IP")
        elif self.ip_parts[0] == 127:
            if all(0 <= part <= 255 for part in self.ip_parts[1:]):
                print("Special IP")
        elif all(0 <= part <= 255 for part in self.ip_parts[1:]):
            print("This IP is a public IP")


def extract_ip(part_str):
    parts = part_str.split(".")
    if len(parts) != 4:
        return None
    try:
        ip_parts = [int(part) for part in parts]
        return ip_parts
    except ValueError:
        return None




text = " MR.I"

print(text2art(text, font="speed"))


user_input = input("Enter your IP address (e.g., 192.168.1.1): ")
ip = extract_ip(user_input)

if ip is None:
    print("Invalid IP address format.")
else:
    ip_analyzer = IPAnalyzer(ip)
    ip_analyzer.analyze()


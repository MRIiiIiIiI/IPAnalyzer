from art import text2art
import time

class IPAnalyzer:
    CLASS_A_MIN = 1
    CLASS_A_MAX = 127
    CLASS_B_MIN = 128
    CLASS_B_MAX = 191
    CLASS_C_MIN = 192
    CLASS_C_MAX = 223

    def __init__(self, ip_parts):
        self.ip_parts = ip_parts
        self.ip_class = None


    def ip_converter(self,ip_parts):
        # ip address
        ip_parts1 = str(ip_parts[0])+'.'+str(ip_parts[1])+'.'+str(ip_parts[2])+'.'+str(ip_parts[3])
        # convert ip to binary
        ip_parts2=ip_parts1.split('.')
        binary_ip = ''.join([bin(int(part))[2:].zfill(8) for part in ip_parts2])
        return binary_ip
    

    def calculate_subnet_mask(self, prefix):
        network_bits = "1" * prefix
        host_bits = "0" * (32 - prefix)
        subnet_mask_bin = network_bits + host_bits
        subnet_mask_decimal = ".".join(str(int(subnet_mask_bin[i:i+8], 2)) for i in range(0, 32, 8))
        return subnet_mask_decimal

    def calculate_network_id(self,prefix):
        network_id_binary =self.ip_converter(self.ip_parts)[:prefix] + '0' * (32 - prefix)
        network_id_parts = [network_id_binary[i:i + 8] for i in range(0, len(network_id_binary), 8)]
        network_id_decimal = '.'.join([str(int(part, 2)) for part in network_id_parts])
        return network_id_decimal

    def calculate_broadcast_address(self,prefix):
        broadcast_binary =self.ip_converter(self.ip_parts)[:prefix] + '1' * (32 - prefix)
        broadcast_parts = [broadcast_binary[i:i + 8] for i in range(0, len(broadcast_binary), 8)]
        broadcast_decimal = '.'.join([str(int(part, 2)) for part in broadcast_parts])
        return broadcast_decimal

    def calculate_hosts_count(self, prefix):
        host_bin = "1" * (32 - prefix)
        host_parts = [int(host_bin[i:i + 8], 2) for i in range(0, len(host_bin), 8)]
        host_decimal = sum(host_parts)
        return host_decimal - 1

    def calculate_network_count(self, prefix):
        network_bin = '1' * prefix + '0' * (32 - prefix)
        network_parts = [int(network_bin[i:i + 8], 2) for i in range(0, len(network_bin), 8)]
        network_decimal = sum(network_parts)
        return network_decimal
    
    
    def INFO(self,perfix_input):
        if 0 < perfix_input <= 32:
            Network_Id= self.calculate_network_id(perfix_input)
            broadcast_address=self.calculate_broadcast_address(perfix_input)
            subnet_mask = self.calculate_subnet_mask(perfix_input)
            Hosts = self.calculate_hosts_count(perfix_input)
            Network = self.calculate_network_count(perfix_input)
            print(" [+] Network ID:",Network_Id)
            print(" [+] broadcast address:",broadcast_address)
            print(f" [+] Subnet Mask of perfix: {subnet_mask}")
        else:
            print("Prefix not found.")
        print(" [+] Number of Network of this prefix:",Network)
        print(" [+] Number of Hosts Per Network of this prefix:",Hosts)

        return perfix_input
    
    def explain(self, class_name, prefix):
        qu_explain = input("Do you want to explain why this result? (y/n): ")
        prefix_bin = '1' * prefix
        if qu_explain.lower() == 'y':
            print(f"1- why Class {class_name}")
            if class_name == 'A':
                print(f"B.c the Range is {self.CLASS_A_MIN} - {self.CLASS_A_MAX}")
            elif class_name == 'B':
                print(f"B.c the Range is {self.CLASS_B_MIN} - {self.CLASS_B_MAX}")
            elif class_name == 'C':
                print(f"B.c the Range is {self.CLASS_C_MIN} - {self.CLASS_C_MAX}")
            print(f"2- what is Network ID: {self.calculate_network_id(prefix)}")
            print("It means that the first 'ip' in the network and the Network ID is a fundamental concept in networking, "
                  "particularly in IP addressing. It refers to the unique identifier assigned to a network segment "
                  "within an IP network. This ID helps routers and switches distinguish between different network "
                  "segments and forward data packets to the correct destination.")
            print(f"3- what is broadcast address: {self.calculate_broadcast_address(prefix)}")
            print("The broadcast address is the last IP in the network. The broadcast address is a special address used"
                  " to send a message to all devices within a specific network segment. When a device sends a "
                  "broadcast message to the broadcast address, all devices in the same network segment receive and "
                  "process the message.")
            print(f"4- what is subnet mask: {self.calculate_subnet_mask(prefix)}")
            print("Any IP contains 4 octets, and each octet contains 8 bits, totaling 32 bits. The prefix is used to "
                  "divide the network.")
            print(f"The prefix /{prefix} means {prefix_bin} in binary, which converts to {self.calculate_subnet_mask(prefix)}.")
            time.sleep(60)
        elif qu_explain.lower() == 'n':
            print('Goodbye...')
        else:
            print("Please enter 'y' or 'n'.")
        pass

    def analyze_ip(self):
        self.classify_ip()  


        if self.ip_class == 'A':
            prefix_range = (8, 32)
            self.class_A(prefix_range)
        elif self.ip_class == 'B':
            prefix_range = (17, 30)
            self.class_B(prefix_range)
        elif self.ip_class == 'C':
            prefix_range = (24, 30)
            self.class_C(prefix_range)
    def classify_ip(self):
        first_octet = self.ip_parts[0]
        if self.CLASS_A_MIN <= first_octet <= self.CLASS_A_MAX:
            self.ip_class = 'A'
        elif self.CLASS_B_MIN <= first_octet <= self.CLASS_B_MAX:
            self.ip_class = 'B'
        elif self.CLASS_C_MIN <= first_octet <= self.CLASS_C_MAX:
            self.ip_class = 'C'
        else:
            self.ip_class = 'Unknown'
        pass

    def class_A(self, prefix_range):
            perfix_input = int(input(">> Enter your prefix (8-32): "))
            if 8 <= perfix_input <= 32:
                print("Class ",self.ip_class)
                self.INFO(perfix_input)
            elif 8 >= perfix_input <= 32:
                print("Class ",self.ip_class)
                self.right_perfix(perfix_input)
            else:
                print("perfix this not right")
            if self.ip_parts[0] == 10:
                if all(0 <= part <= 255 for part in self.ip_parts[1:]):
                    print("This IP is a private IP")
                else:
                    print("Error 404")

            elif all(0 <= part <= 255 for part in self.ip_parts[1:]):
                print("This IP is a public IP")
            else:
                self.class_B(self.ip_class)

            self.explain(self.ip_class,perfix_input)
            pass

    def class_B(self, prefix_range):
            perfix_input = int(input(">> Enter your prefix (17-30): "))
            if 17 <= perfix_input <= 30:
                print("Class ",self.ip_class)
                self.INFO(perfix_input)
            elif 17 >= perfix_input <= 32:
                print("Class ",self.ip_class)
                self.right_perfix(perfix_input)
            else:
                print("perfix this not right")
            if self.ip_parts[0] == 172:
                if 16 <= self.ip_parts[1] <= 31 and all(0 <= part <= 255 for part in self.ip_parts[2:]):
                    print("This IP is a private IP")
                else:
                    print("This IP is a public IP")
            elif all(0 <= part <= 255 for part in self.ip_parts[1:]):
                print("This IP is a public IP")
            else:
                self.class_C(self.ip_class)
            self.explain(self.ip_class,perfix_input)
            pass

    def class_C(self, prefix_range):
            perfix_input = int(input(">> Enter your prefix (24-30): "))
            if 24<= perfix_input <=30:
                print("Class ",self.ip_class)
                self.INFO(perfix_input)
            elif 24>=perfix_input<=30:
                print("Class ",self.ip_class)
                self.right_perfix(perfix_input)
            else:
                print("perfix this not right")
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
            else:
                print("enter a valid IP")
            self.explain(self.ip_class,perfix_input)
            pass

            pass

def extract_ip(part_str):
    parts = part_str.split(".")
    if len(parts) != 4:
        return None
    try:
        ip_parts = [int(part) for part in parts]
        return ip_parts
    except ValueError:
        return None
    pass

text = " MR.I"
print('')
print(text2art(text, font="speed"))

    

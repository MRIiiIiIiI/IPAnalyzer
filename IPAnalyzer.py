from art import *

class IPAnalyzer:
    CLASS_A_MIN, CLASS_A_MAX = 1, 127
    CLASS_B_MIN, CLASS_B_MAX = 128, 191
    CLASS_C_MIN, CLASS_C_MAX = 192, 223
    Class = ['A', 'B', 'C']
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
    def ip_converter(self,ip_parts):
        # ip address
        ip_parts1 = str(ip_parts[0])+'.'+str(ip_parts[1])+'.'+str(ip_parts[2])+'.'+str(ip_parts[3])
        # convert ip to binary
        ip_parts2=ip_parts1.split('.')
        binary_ip = ''.join([bin(int(part))[2:].zfill(8) for part in ip_parts2])
        return binary_ip
    def calculate_Network_ID(self,ip_parts, prefix):
        # Calculate Network ID and Broadcast Address in binary
        network_id_binary =self.ip_converter(ip_parts)[:prefix] + '0' * (32 - prefix)
        # Convert Network ID and Broadcast Address to decimal
        network_id_parts = [network_id_binary[i:i + 8] for i in range(0, len(network_id_binary), 8)]
        network_id_decimal = '.'.join([str(int(part, 2)) for part in network_id_parts])
        # print Network ID and Broadcast Address
        return network_id_decimal
    def calculate_broadcast_address(self,ip_parts, prefix):
        broadcast_binary =self.ip_converter(ip_parts)[:prefix] + '1' * (32 - prefix)
        broadcast_parts = [broadcast_binary[i:i + 8] for i in range(0, len(broadcast_binary), 8)]
        broadcast_decimal = '.'.join([str(int(part, 2)) for part in broadcast_parts])
        return broadcast_decimal
    def calculate_hosts_count(self,perfix):
        host_bin = "1" * (32 - perfix)
        host_part = [int(host_bin[i:i + 8], 2) for i in range(0, len(host_bin), 8)]
        host_decma = sum(host_part)
        return host_decma-1
    def calculate_Network_count(self,perfix):
        Network_bin='1' * (perfix)
        Network_part=[int(Network_bin[i:i + 8],2) for i in range(0, len(Network_bin), 8)]
        Network_decma=sum(Network_part)
        return Network_decma

    def INFO(self,perfix_input):
        if 0 < perfix_input <= 32:
            Network_Id= self.calculate_Network_ID(ip, perfix_input)
            broadcast_address=self.calculate_broadcast_address(ip,perfix_input)
            subnet_mask = self.calculate_subnet_mask(perfix_input)
            Hosts = self.calculate_hosts_count(perfix_input)
            Network = self.calculate_Network_count(perfix_input)
            print(" [+] Network ID:",Network_Id)
            print(" [+] broadcast address:",broadcast_address)
            print(f" [+] Subnet Mask of perfix: {subnet_mask}")
        else:
            print("Prefix not found.")
        print(" [+] Number of Network of this prefix:",Network)
        print(" [+] Number of Hosts Per Network of this prefix:",Hosts)

        return perfix_input
    def right_perfix(self,perfix_input):
        contiue = input(">> ?? Notice this prefix not in the range do u want to continue or not (y/n)")
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
                self.class_C(self.Class[2])
            else:
                self.class_A(self.Class[0])
        elif self.CLASS_B_MIN <= self.ip_parts[0] <= self.CLASS_B_MAX:
            self.class_B(self.Class[1])
        elif self.CLASS_C_MIN <= self.ip_parts[0] <= self.CLASS_C_MAX:
            self.class_C(self.Class[2])

    def class_A(self,Class):
        perfix_input = int(input(">> Enter your prefix (8-32): "))
        if 8 <= perfix_input <= 32:
            print("Class ",Class)
            self.INFO(perfix_input)
        elif 8 >= perfix_input <= 32:
            print("Class ",Class)
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
            self.class_B(Class)

        self.explian(self.Class[0],perfix_input)

    def class_B(self,Class):
        perfix_input = int(input(">> Enter your prefix (17-30): "))
        if 17 <= perfix_input <= 30:
            print("Class ",Class)
            self.INFO(perfix_input)
        elif 17 >= perfix_input <= 32:
            print("Class ",Class)
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
            self.class_C(Class)
        self.explian(self.Class[1],perfix_input)

    def class_C(self,Class):
        perfix_input = int(input(">> Enter your prefix (24-30): "))
        if 24<= perfix_input <=32:
            print("Class ",Class)
            self.INFO(perfix_input)
        elif 24>=perfix_input<=32:
            print("Class ",Class)
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
        self.explian(self.Class[2],perfix_input)

    def explian(self,Class,perifx):
        qu_explian=input("do you want to explain why this result (y/n)")
        perifx_bin=perifx*'1'
        if qu_explian =='Y' or qu_explian =='y' :
            print("1- why Class",Class)
            if Class=='A':
                print("B.c the Range is ",self.CLASS_A_MIN,"-",self.CLASS_A_MAX)
                print("2- why Network ID :")
            elif Class=='B':
                print("B.c the Range is ",self.CLASS_B_MIN,"-",self.CLASS_B_MAX)
            elif Class=='C':
                print("B.c the Range is ",self.CLASS_C_MIN,"-",self.CLASS_C_MAX)
            print("3- what is Network ID:",self.calculate_Network_ID(ip,perifx))
            print("its mean first i in network and know u the strat and end ip in network")
            print("4- what is broadcast address:",self.calculate_broadcast_address(ip,perifx))
            print("broadcast address is last ip in network and "
                  "The broadcast address is a special address used to send a message to all devices within a"
                  " specific network segment. When a device sends a broadcast message to the broadcast"
                  " address, all devices in the same network segment receive and process the message ")
            print("5- what is subnet mask :",self.calculate_subnet_mask(perifx))
            print("Any Ip contain 4 octal and 1 Octal contain 8bits and total is 32 bit "
                  "32bits is perfix what ???????? and prefix to divide network  ")
            print("perifx is /"+str(perifx)+" mean "+perifx_bin+" convert to banriy "+self.calculate_subnet_mask(perifx))
        elif qu_explian=='N'or qu_explian =='n':
            print('good bye ---')
        else:
            print("please enter y or n not any thing other")
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
print('')
print(text2art(text, font="speed"))


user_input = input(">> Enter your IP address (e.g., 192.168.1.1): ")
ip = extract_ip(user_input)

if ip is None:
    print("Invalid IP address format.")
else:
    ip_analyzer = IPAnalyzer(ip)
    ip_analyzer.analyze()






# wait for upgrade this code to ipv6

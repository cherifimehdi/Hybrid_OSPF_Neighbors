def hybrid_neighbors(device, ip='ipv4'):
    # Connect to the device via SSH
    net_connect = ConnectHandler(**device)
    # Retrieve the result of "show ip/ipv6 ospf neighbor" command
    output = net_connect.send_command(f"show {'ipv6' if ip!='ipv4' else 'ip'} ospf neighbor")
    # Display the result
    print(output)
    # End the SSH session for the device
    net_connect.disconnect()
    return print(f"This is {ip} data")

if __name__ == "__main__":
    # Import the ConnectHandler Function to create an Object for R1
    from netmiko import ConnectHandler
    # Parameters of R1
    password = "cisco"
    R1 = {
    "device_type": "cisco_ios",
    "host": "192.168.1.251",
    "username": "Admin",
    "password": password,
    }
    hybrid_neighbors(R1, ip='ipv6')

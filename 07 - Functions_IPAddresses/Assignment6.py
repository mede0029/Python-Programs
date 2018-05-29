import socket

# Task 1:
# Write a python function getClassOfIp that receives a valid IP v4 address in a string format and that returns the class of the IP.
def getClassOfIp(addr):
    a,b,c,d = addr.split(".")
    a = int(a)
    if a <= 126:
        cl = "A"
    if (a >= 128) and (a <= 191):
        cl = "B"
    if a >= 192:
        cl = "C"
    return cl

# Write a python function getDefaultMask that receives a valid IP v4 address in a string format and that returns the default subnet mask of the IP in string format.
def getDefaultMask(addr):
    a, b, c, d = addr.split(".")
    a = int(a)
    if a <= 126:
        subnet = "255.0.0.0"
    if (a >= 128) and (a <= 191):
        subnet = "255.255.0.0"
    if a >= 192:
        subnet = "255.255.255.0"
    return subnet

# Write a python function getNetworkNumber that receives a valid IP v4 address in a string format and a valid subnet mask and that returns the network number in string format.
def getNetworkNumber(addr,subnet):
    a, b, c, d = addr.split(".")
    a1, b1, c1, d1 = subnet.split(".")
    a = int(a)
    b = int(b)
    c = int(c)
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    d1 = int(d1)
    if (a != 0) and (a1 != 0):
        e = a
    else:
        e = 0
    if (b != 0) and (b1 != 0):
        f = b
    else:
        f = 0
    if (c != 0) and (c1 != 0):
        g = c
    else:
        g = 0
    if (d != 0) and (d1 != 0):
        h = d
    else:
        h = 0
    networkNumber = ("{}.{}.{}.{}".format(e,f,g,h))
    return networkNumber

# Write a python function getHostId that receives a valid IP v4 address in a string format and a valid subnet mask and that returns the host id in string format.
def getHostId(addr,subnet):
    a, b, c, d = addr.split(".")
    a1, b1, c1, d1 = subnet.split(".")
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    d1 = int(d1)
    list = []
    if (a != 0) and (a1 != 0):
        e = 0
    else:
        e = a
        list.append(e)
    if (b != 0) and (b1 != 0):
        f = 0
    else:
        f = b
        list.append(f)
    if (c != 0) and (c1 != 0):
        g = 0
    else:
        g = c
        list.append(g)
    if (d != 0) and (d1 != 0):
        h = 0
    else:
        h = d
        list.append(h)
    list = [str(item) for item in list]
    return (".".join(list))

# Task 2:
# Write a python program that:
# prompts the user for a IP v4 address.
# displays an error message if the IP is not a valid IP v4 address.
# displays the class of the IP as well as its default subnet mask if it is a valid one.
# displays the network number and host id of the IP.
# keeps prompting the user for IP addresses until the user decides to quit.
y = 2
while y == 2:
    addr = str(input("Please type the IP address or press 'Q' to quit: > "))
    addr = addr.upper()
    if addr == "Q":
        y = 3
        print("Goodbye!")
    else:
        if addr.count('.') != 3:
            print("This is not a valid IP address formatting!")
        else:
            try:
                socket.inet_aton(addr)
                HOST = addr
                cl = getClassOfIp(addr)
                print("This IP belongs to class '{}'.".format(cl))
                subnet = getDefaultMask(addr)
                print("The default subnet mask for this IP number is: {} ".format(subnet))
                netNumber = getNetworkNumber(addr,subnet)
                print("The network number for this IP is: {} ".format(netNumber))
                hostID = getHostId(addr, subnet)
                print("The host ID for this IP is: {} ".format(hostID))
            except socket.error:
                print("This is an invalid IP address")
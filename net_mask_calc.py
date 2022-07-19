#ip_address = input("Type your Ip Address: ")
#net_mask = input("Type your Net Mask: ")


#ip_address = "192.168.10.1"
ip_address = input("Type ip address: \n")
#net_mask = "255.255.248.0"
net_mask = input("Type network mask: \n")

bits = 0
octets = ""
markup = 0

for i, n in zip(net_mask.split('.'), range(1,5)):

    bin_num = bin(int(i))
    #print(f"{n} oct: {i} {bin_num}  ")
    
    bin_num = bin_num.split(sep='0b')
    #print(bin_num[1])
    
    
    if n < 4:
        s = "."
    else:
        s = ""
    
    octets = octets + bin_num[1].zfill(8) + s
    
    
    for b in bin_num[1]:
        bits = bits + int(b, 10)


for b in octets:
    if b == "0":
        break
    else:
        markup = markup + 1
        

print("----------")
print(f"ip address: {ip_address} \nmask bits: {bits} \nmask: {net_mask} \noctets: {octets}")
print("^".rjust(markup+8," "))

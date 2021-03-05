import os
import socket
import time
import re

def argument(arg):
    switcher = {
        1: "-A -sC -sV -vvv -script/all", #Os scanning,Version detection,scripts,traceroute
        2: "-O -V ", #OS Detection ,Version scanning
        3: "-F --open -Pn", #Fast Mode scan for open ports
        4: "nm.command_line()", #Custom Payload or argument
        5: "-p1-65535 --open  -Pn", #Scan for Open Tcp Ports
        6: "-p1-65535 --open -sU -Pn" #Scan for Open Udp Ports 
    }
    return switcher.get(arg, "Invalid argument")


#Website information
website=input("Enter The Website to scan: ")
ip_of_website = socket.gethostbyname(website)
print("Ip of "+website+" is:"+ip_of_website)
time.sleep(0.7)
#Choice to start nmap or not
print("\n Want to start nmap scanning \n1.Yes \n2.No ")
nmap_on_off=int(input("Choice:"))
if(nmap_on_off == 1):
    #Starting nmap
    print("\nFiring up Nmap\n")
    print("1.Os scanning,Version detection,scripts,traceroute \n2.OS Detection ,Version scanning \n3.Fast Mode scan for open ports \n4.Custom Payload or argument \n5.Scan for Open Tcp Ports \n6.Scan for Open Udp Ports ")
    choice=int(input("\n Enter The Choice:"))
    if(choice == 4):
        nmap_command=input("Enter Nmap Command u want \n")
        os.system(nmap_command+" "+ip_of_website)
    else:
        arg=argument(choice)
        print("Command="" nmap "+arg+" <ip of website> \n")
        os.system("nmap "+arg+" "+ip_of_website)

    #print(arg)
else:
    print("Skipping Nmap Scan")

#Finding subdomains and finding alive host
os.system("assetfinder --subs-only "+website+" >> all_host.txt")
os.system("cat all_host.txt | httprobe >> alive_host.txt")

#Checking for wordpress site
os.system("wpscan --stealthy --url "+website)


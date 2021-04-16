import os
import socket
import time
from colorama import Fore, Back, Style


def argument(arg):
    switcher = {
        1: "-A -sC -sV -vvv -oN Output/nmap", #Os scanning,Version detection,scripts,traceroute
        2: "-O -V -oN Output/nmap", #OS Detection ,Version scanning
        3: "-F --open -Pn -oN Output/nmap", #Fast Mode scan for open ports
        4: "nm.command_line()", #Custom Payload or argument
        5: "-p1-65535 --open  -Pn -oN Output/nmap", #Scan for Open Tcp Ports
        6: "-p1-65535 --open -sU -Pn -oN Output/nmap" #Scan for Open Udp Ports 
    }
    return switcher.get(arg, "Invalid argument")


#Website information
#Making a folder if not Exists
os.system("clear")
os.system("rmdir Output && mkdir Output")
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
        os.system(nmap_command+" -oN Output/nmap "+ip_of_website)
    else:
        arg=argument(choice)
        print("Command="" nmap "+arg+" <ip of website> \n")
        os.system("nmap "+arg+" "+ip_of_website)

    #print(arg)
else:
    print("Skipping Nmap Scan")

#Finding Certificate of a website

#Finding subdomains and finding alive host
print("\n**************Finding all sudomain*****************")
os.system("assetfinder --subs-only "+website+" >> Output/all_host.txt")
print("\nDone and save output to all_host.txt")
print("\n************Finding alive sudomain*****************")
os.system("cat all_host.txt | httprobe  >> Output/alive_host.txt")
print("\nDone and save output to alive_host.txt")

#Finding hidden Directory 
print("\nWant to start checking hidden dir,files \n1.Yes\n2.No")
dir_start=int(input("Enter choice:"))
if (dir_start == 1):
    print("Finding hidden Directory")
    os.system("ffuf -w small.txt -u http://"+website+"/FUZZ -mc all -fs 42 -c -fc 404 -o Output/hidden_directories")
    os.system("cat hidden_directories|jq >> Output/Hidden_Directory")
    os.system("rm Output/hidden_directories")
else:
    print("Skipping Directory search")

#Checking for wordpress site
print("\n***********Scanning website is Wordpress site or not***********")
os.system("wpscan --stealthy --url "+website)
os.system("wpscan -f json --url+ "+website+" >> Output/wpscan")

#Firing up the Sqlmap
print("\nStarting Sqlmap \n")
print(Fore.RED + 'WARNING:Only use sqlmap for attacking with mutual consent with the site owner or company')
print(Style.RESET_ALL)
sql_start_stop=int(input("Want to continue with SqlMap:"))
print("\n 1.Start \n2.Stop")
if(sql_start_stop == '1' ):
    sql_level=int(input("Level of tests to perform (1-5) \nEnter the level of Sqlmap:"))
    sql_site=input("Enter the endpoint where u want to test sql injection:")
    os.system("sqlmap -u "+sql_site+" --dbs --level="+str(sql_level))
elif(sql_start_stop == '2'):
    print("Stopping Nmap And Continue script")
else:
    print("Skipping Sqlmap")


exit()
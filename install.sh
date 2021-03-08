!bin/bash
#Author= Abhinav Saxena
bgreen='\033[1;32m'
printf "\n\n${bgreen}***********************************************************************\n"
printf "${bgreen} GoldenEye Installation Script ${reset}\n\n"
echo "Installing required tools"
echo "Make sure u are root user"



apt_install()
{
    #Requirements installation
    eval $install_apt apt install python3 python3-pip python figlet ruby nokogiri 
    #Installing tools using apt install
    eval $install_apt apt install nmap dirb curl shodan sqlmap wpscan
}

go_install()
{
    eval $go_get  go get -u github.com/tomnomnom/assetfinder github.com/tomnomnom/httprobe github.com/tomnomnom/waybackurls 
}

if [[ $(id -u) = 0 ]]; then 
    echo "Starting installation"
    install_apt=" "
    go_get=" "
else
    echo "Start script again"
    sudo su
fi
#Installing Python requirements 
pip install requests colorama
pip3 install requests colorama

#Checking if Go installed or not
if [[$(which go | grep -o go > /dev/null &&  echo 0 || echo 1) == 0]]; then
    echo "Go is already installed"
else
    echo "GO is Not installed"
    wget -c https://golang.org/dl/go1.16.linux-amd64.tar.gz #latest version(March 5,2021)
    tar -C /usr/local -xvzf go1.16.linux-amd64.tar.gz
    rm go1.16.linux-amd64.tar.gz #Removing package after installing
    #Setting Env for go
    if [[$(uname -a | grep Linux &&  echo 0 || echo 1) == 0]]; then
        export PATH=$PATH:/usr/local/go/bin >> $HOME/.profile
        export GOROOT=$HOME/go
        export PATH=$PATH:$GOROOT/bin   
        source ~/.profile
    else 
        export PATH=$PATH:/usr/local/go/bin >> $HOME/.bash_profile 
        export GOROOT=$HOME/go
        export PATH=$PATH:$GOROOT/bin  
        source ~/.bash_profile
    fi
fi


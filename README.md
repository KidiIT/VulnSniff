#  VulnSniff
Vulnerability detection and packet sniffing Tool
VulnSniff is a network packet sniffer integrated with vulnerability detection, designed to enhance network security by analyzing traffic and identifying potential vulnerabilities.
Leveraging Nmap for vulnerability scanning. However, VulnSniff allows users to capture and inspect network packets while providing insights into  security risks,making it a valuable tool for penetration testers, network administrators, and security enthusiasts.

**key Features:**
1. Real-Time packet capture and analysis
2. Seamless integration with Nmap for Vulnerability detection
3. Customizable filters for targeted packet sniffing
4. user-friendly GUI for easy interaction
5. supports multiple network protocols
VulnSniff is built with security in mind,ensuring reliable network monitoring while offering advanced vulnerability detection capabilities.

**How to Use:**
##  Prerequisites:
>[ !NOTE]
> The following are strictly required to run this Tool on your local machine
> python 3.8 or higher
> ubuntu/Linux or windows
> Nmap (for vulnerability scanning)
> user must have administrative privileges (e.g., 'sudo'access)

## installation Instructions:
1. **Clone the Repository**:```bash
 git clone https://github.com/KidiIT/VulnSniff.git
cd VulnSniff
2.  set up a virtual Environement(Optional but Recommended)
**For Linux/MacOS:**
python3 -m venv venv
source venv/bin/activate
**For Windows:**
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Install Nmap(if not already installed):
# For Linux:
sudo apt-get install nmap  
# For macOS
brew install nmap 

##  Usage
To start using VulnSniff, run the following command:
sudo python3 packet_sniffer.py --interface eth0 --scan-target 192.168.1.1
## Command-lin Options:
.--interface: Specify the network interface to sniff packets.
.--scan-target:Provide the IP address or network range to scan for vulnerabilities
##  Example Workflow
1. Identify your network interface:
ifconfig
2.  Run VulnSniff on your chosen interface:
   sudo python3 packet_sniffer.py --interface eth0

##  License and Contribution Guidelines
VulnSniff project is an open-source and free to use under MIT License. Contributions are welcome. please fork the repository and submit pull request.

##  Troubleshooting
1.  if you get a "permission denied" error, try running the tool with `sudo`
2.  if the tool doesn't recognize Nmap, ensure it is installed and available in your path.
3.  most importantly, this error "No module named scapy" you'll often experience this error.
   #  Solution 
   Run this code on your command-line to install the right scapy.all on your Ubuntu Linux machine:  `sudo apt-get install python3-scapy`
4.  lastly,please  I'll recommend you update your Ubuntu from wls1 to wls2. 
## Steps to update your ubuntu from wls1 to wls2 on Windows(Recommended if you're running wls1 on your Linux machine)
1. On your Windows, open the powershell terminal as an adminstrator
2. when done, like wls  after which you'll logged in as the root-user just like on your Linux operating system.
3. ## run this command: `wsl --set-version ubuntu 2 in Powershell.
# this command sets the WSL version for your ubuntu distribution from the windows side. Make sure to run PowerShell as an administrator for the command to work.

##   Uninstallation instructions
1. Deactivate the virtual environemnt(if activated):

$ deactivate

Remove the cloned directory:
$ rm -rf VulnSniff

In conclusion, I'm so overwhelmed sharing this tremendous and proactive Tool with the Open Source community. I hope y'all wll enjoy and have the best vulneriability spart canning experience with my Tool. Thanks for being part of my career journey as a cybersecurity professionals and a security researcher.




















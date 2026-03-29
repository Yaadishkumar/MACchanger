import subprocess
import optparse

parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="help to change its MAC address")
parser.add_option("-m","--new_mac",dest="new_mac",help="enter new mac address")
parser.parse_args()



interface=input("interface>")
new_mac=input("new_mac>")

subprocess.run(["ifconfig",interface,"down"])
subprocess.run(["ifconfig",interface,"hw","ether",new_mac])
subprocess.run(["ifconfig",interface,"up"])

import subprocess
import optparse

parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="help to change its MAC address")
parser.parse_args()

subprocess.run("ifconfig")

interface=input("interface>")
new_mac=input("new_mac>")

subprocess.run(["ifconfig",interface,"down"])
subprocess.run(["ifconfig",interface,"hw","ether",new_mac])
subprocess.run(["ifconfig",interface,"up"])
subprocess.run("ifconfig")
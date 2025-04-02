from os import system
import logging
import argparse
import subprocess

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

log = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description="Development Environment")

parser.add_argument("-o", "--option", type=str, help="Option")

args = parser.parse_args()

ansible_inventory = "inventories/hosts.yml"

try:
    log.info("Checking Ansible...")
    subprocess.run(["ansible", "--version"], check=True, capture_output=True)
    log.info("Ansible is installed.")
except subprocess.CalledProcessError:
    raise Exception("Ansible is not installed.")
except FileNotFoundError:
    raise Exception("Ansible is not installed.")

log.info(args.option)
if args.option == "Ping Hosts":
    system(f"ansible nodes -i {ansible_inventory} -m ping")
elif args.option == "Add SSH key":
    system(
        f"ansible-playbook -i {ansible_inventory} playbooks/hosts/onboard.yml --user=root -k -K")
elif args.option == "Update Hosts":
    system(f"ansible-playbook -i {ansible_inventory} playbooks/hosts/main.yml")
elif args.option == "Install Hadoop Cluster":
    system(
        f"ansible-playbook -i {ansible_inventory} playbooks/hadoop/main.yml")
elif args.option == "Launch Hadoop Cluster":
    system(
        f"ansible-playbook -i {ansible_inventory} playbooks/hadoop/restart.yml")
elif args.option == "Uninstall Hadoop Cluster":
    system(
        f"ansible-playbook -i {ansible_inventory} playbooks/hadoop/uninstall.yml")
else:
    print("Please, press F5 on Visual Studio Code to debug and choose a valid option.")

from .Request import Request
from .ProxyPool import ProxyPool
from .UserAgentPool import UserAgentPool
import re

import subprocess

class ProxyRequest(Request):
    def __init__(self, proxy=None):
        self.proxy_pool = ProxyPool()
        self._useragent_database = UserAgentPool()
        if proxy is None:
            proxy = self.proxy_pool.get_best_proxy()
        super().__init__(timeout=10, proxy=proxy, user_agent=self._useragent_database.get_random_user_agent())

    def get(self, page, data={}):
        return super().get(page=page, data=data)

    def post(self, page, data={}):
        return super().post(page=page, data=data)
    


    def verify_sender_ip():
        try:
            # Run the ifconfig command and capture the output
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
            
            # Check if the command was successful
            if result.returncode != 0:
                raise Exception("Error running ifconfig command")
            
            # Get the output of the ifconfig command
            output = result.stdout
            
            # Regular expression to find IP addresses
            ip_pattern = re.compile(r'inet (\d+\.\d+\.\d+\.\d+)')
            
            # Find all IP addresses in the ifconfig output
            ip_addresses = ip_pattern.findall(output)
            
            external_ip_from_local_interface = None

            # Filter out private IP addresses
            for ip in ip_addresses:
                if not (ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("127.") or ip.startswith("169.254.")):
                    external_ip_from_local_interface = ip
            
            current_ip_external_verification_remote_service = super().get_current_ip()
            return  (current_ip_external_verification_remote_service == external_ip_from_local_interface)
            
            
            # If no external IP address is found
            raise ValueError("No external IP address found")
        
        except Exception as e:
            print(f"An error occurred obtaining the ip address locally{e}")
            return None
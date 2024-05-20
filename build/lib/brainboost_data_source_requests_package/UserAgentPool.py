import random

class UserAgentPool:
    def __init__(self,user_agents_list_path=None) -> None:
        self.user_agent_list_path = user_agents_list_path
        

    def get_random_user_agent(self):
        if self.user_agent_list_path == None:
            file_path = 'src/brainboost_data_source_requests_package/resources/user_agents.txt'
        else:
            file_path = self.user_agent_list_path
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if lines:
                    return random.choice(lines).strip()  # Choose a random line and strip any extra whitespace
                else:
                    return "File is empty"  # If file is empty
        except FileNotFoundError:
            return f"File not found: {file_path}"  # If file not found
        except Exception as e:
            return f"Error occurred: {str(e)}"  # Other exceptions
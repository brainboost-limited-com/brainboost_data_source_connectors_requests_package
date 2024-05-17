import random

class UserAgentPool:
    def __init__(self) -> None:
        pass

    def get_random_user_agent(self):
        file_path = 'src/resources/user_agents.txt'
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
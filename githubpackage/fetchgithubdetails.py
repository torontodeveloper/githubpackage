import requests
import yaml

class GitHubAPI():
    '''
    this is github API calss to be call github api and fetch user 
    details
    
    Parameters
    ---------
    None
    Returns
    -----
    user details through method call of class
    
    Examples
    >>> api = GitHubAPI()
    >>> user_List = api.fetch_users_list_most_followers()
    '''
    
    def __init__(self) -> None:
        '''
        This is initialization aka constructor 
        '''
    
    def fetch_users_list_most_followers(self) -> dict:
        """ 
        This function fetches github user details by calling github API 

        Parameters:
            user (str): github user 
        Returns:
            github user details as dictionary object
        
        Example:
        --------
        fetch_users_list_most_followers()
        """    
        with open('config.yml','r') as file:
            config_data = yaml.safe_load(file)
        
        headers = {'Authorization'+'Bearer '+config_data['token']}
        url = config_data['url']
        endpoint = url
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print('Retry: 2nd time API**')
            response = requests.get(endpoint,headers=headers)
        return response.json()
  
  
class SayHello():
    def __init__():
        pass
    def say_hello():
        print('Hello World!!')
    
api = GitHubAPI()
user_list = api.fetch_users_list_most_followers()
# uncomment to invoke this class object
for user in user_list[0]:
    print('github user',user)

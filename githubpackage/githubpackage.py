import requests

url = 'https://api.github.com/users/'
token = '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'

class GitHubAPI():
    '''
    this is github API calss to be call github and get user 
    details
    
    parameters
    ---------
    None
    Returns
    -----
    None
    Usage
    api = GitHubAPI()
    api.get_github_user('karpathy')
    '''
    
    def __init__(self) -> None:
        '''
        This is initialization aka constructor 
        '''
    
    def get_github_user(self,user:str) -> dict:
        """ 
        This function fetches github user details by calling github API 

        Parameters:
            user (str): github user 
        Returns:
            github user details as dictionary object
        
        Example:
        --------
        get_github_user('toronotdeveloper')
        """    
        headers = {'Authorization'}
        user_details = {}
        endpoint = url+user
        try:
            response = requests.get(url+user)
        except requests.exceptions.ConnectionError:
            print('Retry: 2nd time API**')
            response = requests.get(endpoint,headers=headers)
        # json_response = json.loads(response.text)
        # user_details.update(json_response)
        return response.json()


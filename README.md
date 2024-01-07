# githubpackage

github api details package

this is github API calss to be call github and get user
details

    Usage

1.  api = GitHubAPI()
    user1 = api.get_github_user('karpathy')

2.  api = GitHubAPI()
    user2 = api.get_github_user('getify')

for key,value in user1.items():
print(f'item is {key} and {value}')

for key,value in user2.items():
print(f'GitHub User details: Item: {key} and value: {value}')

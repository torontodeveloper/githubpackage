from fetchgithubdetails import GitHubAPI

def test_valid_github_api():
    api = GitHubAPI()
    user_list = api.fetch_users_list_most_followers()
    assert len(user_list)>0,'Invalid List of Users'
    
def test_match_git_hub_api():
    api = GitHubAPI()
    expected_user = {
        "login":'abc',
        "id":123
    }
    user_list = api.fetch_users_list_most_followers()
    for expected,actual in zip(expected_user,user_list[0]):
        assert expected==actual

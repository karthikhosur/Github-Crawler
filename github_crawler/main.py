from github_crawler.user_profile_main import user_profile_parser
from github_crawler.user_repos_main import user_repos_parser

def user_profile(username):
    profile_url = "https://github.com/"+ username
    user_profile_results = user_profile_parser(profile_url,username)
    return user_profile_results

def repo_info(url):
    user_repos_results = user_repos_parser(url)
    return user_repos_results


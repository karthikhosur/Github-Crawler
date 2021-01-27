import requests
from bs4 import BeautifulSoup

def user_profile_parser(profile_url,username):
    URL = profile_url + '?tab=repositories'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    user_followers = user_followers_parser(soup,username)
    user_following = user_following_parser(soup,username)
    user_stars = user_stars_parser(soup,username)
    user_repositories_urls = user_repositories_parser(soup,username)
    user_profile_results = {
        "followers" : user_followers,
        "following" : user_following,
        "stars" : user_stars,
        "repositories" : user_repositories_urls
    }
    return user_profile_results


def user_followers_parser(soup,username):
    user_followers = soup.find('a', href= '/'+ username+'?tab=followers')
    user_followers = int(user_followers.find('span').text)
    return user_followers


def user_following_parser(soup,username):
    user_following = soup.find('a', href='/'+ username+ '?tab=following')
    user_following = int(user_following.find('span').text)
    return user_following

def user_stars_parser(soup,username):
    user_stars = soup.find('a', href='/'+ username+'?tab=stars')
    user_stars = int(user_stars.find('span').text)
    return user_stars

def user_repositories_parser(soup,username):
    user_repositories_text = soup.find('div', id = 'user-repositories-list')
    user_repositories_urls = user_repositories_text.find_all('a', itemprop = "name codeRepository")
    for i in range(len(user_repositories_urls)):
        user_repositories_urls[i] = user_repositories_urls[i].get('href')

    return user_repositories_urls
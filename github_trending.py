import requests
import datetime


def get_json_response(url, params=None):
    response = requests.get(url, params)
    return response.json()


def get_trending_repositories(top_size):
    period_of_days = 7
    last_week = str(datetime.date.today() - datetime.timedelta(days=period_of_days))
    search_repo_url = 'https://api.github.com/search/repositories'
    url_params = {'q': 'created:>=' + last_week, 'sort': 'stars', 'per_page': top_size}
    return get_json_response(search_repo_url, url_params)['items']


def get_open_issues_amount(repo_owner, repo_name):
    issues_url = 'https://api.github.com/repos/{owner}/{name}'.format(owner=repo_owner, name=repo_name)
    issues_list = get_json_response(issues_url)
    return issues_list['open_issues_count']


def main():
    top_size = 20
    trending_rep = get_trending_repositories(top_size)

    for repository in trending_rep:
        repo_owner_name = repository['owner']['login']
        repo_name = repository['name']
        repo_url = repository['name']
        repo_stars = repository['stargazers_count']
        open_issues_amount = get_open_issues_amount(repo_owner_name, repo_name)
        print('Repository: {name}, owner: {owner} - has {stars} stars and {issues} open issues. URL: {url}'.format(
            name=repo_name, owner=repo_owner_name, stars=repo_stars, issues=open_issues_amount, url=repo_url))


if __name__ == '__main__':
    main()

import requests
import datetime


def get_json_response(url, params):
    response = requests.get(url, params)
    return response.json()


def get_trending_repositories(top_size):
    last_week = str(datetime.date.today() - datetime.timedelta(days=7))
    search_repo_url = 'https://api.github.com/search/repositories'
    url_params = {'q': 'created:>=' + last_week, 'sort': 'stars', 'per_page':top_size}

    return get_json_response(search_repo_url, url_params)['items']


def get_open_issues_amount(repo_owner, repo_name):
    issues_url = 'https://api.github.com/repos/{owner}/{name}/issues'.format(owner=repo_owner, name=repo_name)
    url_params = {'state': 'open'}
    issues_list = get_json_response(issues_url, url_params)
    return issues_list


def main():
    top_size = 20
    trending_rep = get_trending_repositories(top_size)

    for repository in trending_rep:
        repo_owner = repository['owner']['login']
        repo_name = repository['name']
        print('-------------')
        print(repo_owner, '-', repo_name, repository['stargazers_count'])

        if repository['open_issues_count'] > 0:
            print(repository['open_issues_count'])
            try:
                issues_list = get_open_issues_amount(repo_owner, repo_name)
                for issue in issues_list:
                    print(issue['title'], issue['url'])
            except TypeError:
                print('ОШИБКА:  - Превышен лимит подключений, попробуйте завтра')
        else:
            print('Открытых вопросов нет')


if __name__ == '__main__':
    main()

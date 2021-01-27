

# Github Crawler

```
A web spider to crawl public github repositories
```

Built with ❤︎ and :coffee: by  [Karthik Hosur](https://github.com/karthikhosur)

---
```
A web spider to crawl public github repositories to collect data of github user profiles,repositories and user social counts for educational purpose only. The project was earlier built to collect data from github for academic data analysis project.
```

# Features

- Extract User Social Status 
- Extract Repository Names
- Extract User Activity
- Extract Repository Social Information
- Extract Repository Data

# Installation

- You can install this package using

```bash
pip install github-crawler
```

# Usage

### Extract the profile information of a github user

- Import it in your Python project

```python
from github_crawler import user_profile

github_crawler.user_profile("karthikhosur") # Use the username of the user
```


### Result

The module would return a dictionary with result as follows:

```
{'followers': 2,
 'following': 4,
 'stars': 5,
 'repositories': ['/karthikhosur/Github-Crawler',
  '/karthikhosur/FairCV',
  '/karthikhosur/Stop-Words-Remover-API',
  '/karthikhosur/BlogsParser-API',
```


### Extract a Repository information 

- Import it in your Python project

```python
from github_crawler import repo_info

github_crawler.repo_info("/karthikhosur/Github-Crawler")# Use the username with the repository name in the format given

```

### Result

The module would return a dictionary with result as follows:

```
{'watchers': 1, 'stargazers': 1, 'forks': 1}
```



# References 


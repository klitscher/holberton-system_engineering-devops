#!/usr/bin/python3
"""Module to grab data from reddit"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Function that querries an api
    to return the a list of all the hot posts
    for a subreddit, recursively"""
    user_agent = (
        "python:This_is_a_student_weee:1.8"
    )
    headers = {"User-Agent": user_agent}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after
    )
    reddit_data = requests.get(url, headers=headers, allow_redirects=False)
    if reddit_data.status_code in (302, 404):
        return None
    json_data = reddit_data.json()
    next_page = json_data.get('data').get('after')
    json_data_children = json_data.get('data').get('children')
    for li in json_data_children:
        hot_list.append(li.get('data').get('title'))
    if next_page is None:
        return hot_list
    return recurse(subreddit, hot_list, next_page)

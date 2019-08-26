#!/usr/bin/python3
"""Script to fetch a url"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read(300)
    print(type(html))
    print(html)
    print(response.__dict__)
    print(response.headers)
    print(response.info())

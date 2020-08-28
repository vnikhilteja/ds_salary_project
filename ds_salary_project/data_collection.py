# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:07:20 2020

@author: Nikhil teja V
url: https://github.com/vnikhilteja/ds_salary_project/tree/master/ds_salary_project
"""

import glassdoor_scrapper as gs
import pandas as pd

path="D:/Data science Project/ds_salary_project/chromedriver"

df=gs.get_jobs('data scientist',15,False, path,15)

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:15:39 2022

@author: jeremy.hue
"""

from planner import *
import pandas as pd

resource_df = pd.read_csv('resources.csv')
rp = ResourcePool(resource_df)

tasks = []
task_info = {1:{'name':'analysis',
                'effort_left': 10,
                'resource_type': 'analyst'},
             2: {'name':'development',
                'effort_left': 7,
                'resource_type': 'developer'},
             3: {'name':'test',
                'effort_left': 5,
                'resource_type': 'tester'}}
for i in range(5):
    tasks.append(Task(f'Table {i}', task_info))

plan = Planner(rp, tasks)
plan.plan()

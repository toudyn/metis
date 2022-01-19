# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:12:53 2021

@author: jeremy.hue
"""
import sys
sys.path.append('..')
from planner import *
import pandas as pd

resource_df = pd.DataFrame()
resource_df['day_index'] = list(range(1,101))
resource_df['analyst'] = 4
resource_df['developer'] = 2
resource_df['tester'] = 0

def test_resource_pool_initializes():
    # Tests that a resource pool object can be created
    rp = ResourcePool(resource_df)
    assert rp

def test_resource_pool_reads_resouce_df_correctly():
    # Tests that the resource dataframe can be read correctly
    rp = ResourcePool(resource_df)
    assert rp.resources[10]['developer'] == 2

def test_resource_pool_assignable_resources():
    # Tests whether the resource pool considers a task as assignable - with resources available
    rp = ResourcePool(resource_df)
    day_index = 1
    task_duration = 5
    resource_type = 'analyst'
    assert rp.assignable(day_index, task_duration, resource_type) is True

def test_resource_pool_assignable_no_resources():
    # Tests whether the resource pool considers work assignable - with no resources available
    rp = ResourcePool(resource_df)
    day_index = 1
    task_duration = 5
    resource_type = 'tester'
    assert rp.assignable(day_index, task_duration, resource_type) is False

def test_resources_assigned():
    # Tests that the number of available resources reduces correctly when work is assigned
    rp = ResourcePool(resource_df)
    day_index = 1
    task_duration = 5
    resource_type = 'developer'
    rp.assign(day_index, task_duration, resource_type) # Book one developer
    rp.assign(day_index, task_duration, resource_type) # Book the other developer
    assert rp.assignable(day_index, task_duration, resource_type) is False


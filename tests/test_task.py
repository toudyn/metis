# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 17:12:53 2021

@author: jeremy.hue
"""
import sys
sys.path.append('..')
from planner import *

table_subtasks = {1: {'name': 'analysis',
                   'resource_type': 'analyst',
                   'effort_left': 7},
               2: {'name': 'build',
                   'resource_type': 'developer',
                   'effort_left': 5},
               3: {'name': 'test',
                   'resource_type': 'tester',
                   'effort_left': 5}}

def test_table_creation():
    # Tests that a table object can be created
    t = Task('test_table', table_subtasks)
    assert t

def test_table_subtasks_create_properly():
    # Tests that the tasks set during table creation work properly
    t = Task('test_table', table_subtasks)
    name1 = t.efforts_left[1]['name']
    resource_type2 = t.efforts_left[2]['resource_type']
    effort_left3 = t.efforts_left[3]['effort_left']
    
    assert (name1, resource_type2, effort_left3) == ('analysis', 'developer', 5)

def test_table_initiates_as_unassigned():
    # Tests that a new table starts off as unassigned
    t = Task('test_table', table_subtasks)
    assert t.assigned is False

def test_setting_assigned():
    # Tests to see whether tables can be successfully set to assigned
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    assert t.assigned is True

def test_getting_current_subtask_unstarted():
    # Tests whether an unstarted table returns the first task as the current task
    t = Task('test_table', table_subtasks)
    assert t.get_current_subtask() == 1

def test_recording_work_done():
    # Tests whether recording work done correctly - only 1 day of analysis, starting at 7
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    t.record_work_done()
    assert t.efforts_left[1]['effort_left'] == 6

def test_recording_work_unassigned():
    # Tests that work is not recorded when the task is not assigned - analysis 7 days remains 7 days
    t = Task('test_table', table_subtasks)
    t.record_work_done()
    assert t.efforts_left[1]['effort_left'] == 7

def test_getting_current_task_started():
    # Tests whether a table where work has been started on returns the first task as the current task
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    t.record_work_done()
    t.record_work_done()
    assert t.get_current_subtask() == 1

def test_unassignment_at_task_completion():
    # Tests that the table is correctly set to unsassigned when the current task completes
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done()
    assert t.assigned is False

def test_getting_current_task_almost_done():
    # Tests whether a table that is farther in development returns the correct current task
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    t.set_assigned()
    t.record_work_done() # Start on build
    assert t.get_current_subtask() == 2

def test_table_complete_not_done():
    # Tests whether the table is correctly considered not done when there are tasks left to do
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    t.set_assigned()
    t.record_work_done() # Start on build
    assert t.is_complete() is False

def test_table_complete_done():
    # Tests whether the table is correctly considered done when there are no tasks left to do
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete build
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete test
    assert t.is_complete() is True

def test_get_current_requirement_unstarted():
    # Tests the current task requirements for an unstarted table
    t = Task('test_table', table_subtasks)
    assert t.get_current_subtask_requirements() == ('analysis', 'analyst', 7)
    
def test_get_current_requirement_started():
    # Tests the current task requirements for an unstarted table
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    t.record_work_done()
    assert t.get_current_subtask_requirements() == ('analysis', 'analyst', 6)

def test_get_current_requirement_second_task():
    # Tests the current task requirements for an unstarted table
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    assert t.get_current_subtask_requirements() == ('build', 'developer', 5)

def test_get_current_requirement_completed():
    # Tests the current task requirements for a completed table are null
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete build
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete test
    assert t.get_current_subtask_requirements() == (None , None, 0)

def test_completed_table_unassignable():
    # Tests that a completed table is unassignable
    t = Task('test_table', table_subtasks)
    t.set_assigned()
    for i in range(7):
        t.record_work_done() # Complete analysis
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete build
    t.set_assigned()
    for i in range(5):
        t.record_work_done() # Complete test
    t.set_assigned()
    assert t.assigned is False
    


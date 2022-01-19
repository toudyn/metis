# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:56:51 2021

@author: jeremy.hue
"""

from copy import deepcopy

class Task:
    """
    Object that simulates a task that has multiple subtasks.
    """
    
    def __init__(self, name, subtasks):
        """
        subtasks should be a dictionary of subtasks
        eg.
        {1:{'name':'analysis',
            'effort_left': 10,
            'resource_type': 'analyst'},
         2: {'name':'development',
            'effort_left': 7,
            'resource_type': 'developer'},
         3: {'name':'test',
            'effort_left': 5,
            'resource_type': 'tester'}}
        """
        self.name = name
        self.subtasks = subtasks
        self.efforts_left = deepcopy(subtasks)
              
        self.assigned = False

    def __repr__(self):
        return f'<Task> {self.name}'

    def set_assigned(self):
        """
        Sets the table to assigned, to indicate that a resource has been
        assigned to complete the current subtask in progress.
        """
        if not self.is_complete():
            self.assigned = True
        else:
            print('Tried assigning task, but it is already complete')
    
    def get_current_subtask(self):
        """
        Returns the id of the current subtask - the first unfinished subtask.
        If the task is completed return None
        """
        for subtask_id, subtask_info in self.efforts_left.items():
            if subtask_info['effort_left'] != 0:
                return subtask_id
        return None
    
    def get_current_subtask_requirements(self):
        """
        Returns the name, type of resource, and number of days required to
        complete the first unifinished subtask.
        """
        current_subtask = self.get_current_subtask()
        if current_subtask is not None:
            subtask_info = self.efforts_left[current_subtask]
            return (subtask_info['name'], subtask_info['resource_type'], subtask_info['effort_left'])
        else:
            return (None, None, 0)
    
    def record_work_done(self):
        """
        If assigned, this reduces the required days for the current subtask by
        1 day. If the task is completed in this day then the task is set to
        unassigned.
        """
        if not self.assigned:
            return
        current_subtask = self.get_current_subtask()
        self.efforts_left[current_subtask]['effort_left'] -= 1
        
        if self.efforts_left[current_subtask]['effort_left'] == 0:
            # Current task is complete, unassign the table to be picked up for next task
            self.assigned = False
    
    def is_complete(self):
        """
        Returns true if the task is completed.
        """
        if self.get_current_subtask() is None:
            return True
        else:
            return False
        
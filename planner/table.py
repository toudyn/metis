# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:56:51 2021

@author: jeremy.hue
"""

from copy import deepcopy

class Table:
    """
    Object that simulates a table that needs to be designed,
    built, and tested.
    """
    
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.efforts_left = deepcopy(tasks)
              
        self.assigned = False

    def __repr__(self):
        return f'<Table> {self.name}'

    def set_assigned(self):
        """
        Sets the table to assigned, to indicate that a resource has been
        assigned to complete the current task in progress.
        """
        if not self.is_complete():
            self.assigned = True
        else:
            print('Tried assigning completed task')
    
    def get_current_task(self):
        """
        Returns the id of the current task - the first unfinished task.
        If the task is completed return None
        """
        for task_id, task_info in self.efforts_left.items():
            if task_info['effort_left'] != 0:
                return task_id
        return None
    
    def get_current_task_requirement(self):
        """
        Returns the name, type of resource, and number of days required to
        complete the first unifinished task.
        """
        current_task = self.get_current_task()
        if current_task is not None:
            task_info = self.efforts_left[current_task]
            return (task_info['name'], task_info['resource_type'], task_info['effort_left'])
        else:
            return (None, None, 0)
    
    def record_work_done(self):
        """
        If assigned, this reduces the required days for the current task by
        1 day. If the task is completed in this day then the task is set to
        unassigned.
        """
        if not self.assigned:
            return
        current_task = self.get_current_task()
        self.efforts_left[current_task]['effort_left'] -= 1
        
        if self.efforts_left[current_task]['effort_left'] == 0:
            # Current task is complete, unassign the table to be picked up for next task
            self.assigned = False
    
    def is_complete(self):
        """
        Returns true if the task is completed.
        """
        if self.get_current_task() is None:
            return True
        else:
            return False
        
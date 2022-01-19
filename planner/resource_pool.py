# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:08:19 2021

@author: jeremy.hue
"""

from copy import deepcopy

class ResourcePool:
    """
    Class that manages the allocation of available resources towards tasks
    that need doing.
    """
    
    def __init__(self, resource_df):
        self.resources = dict()
        self.original_resources = None
        self.day = None
        self.load_resources(resource_df)
    
    def load_resources(self, resource_df):
        """
        Parses the provided resource dataframe.
        """
        for row in resource_df.to_dict(orient='records'):
            if self.day is None:
                self.day = row['day_index']
            self.resources[row['day_index']] = row
        
        self.original_resources = deepcopy(self.resources)
    
    def assignable(self, day_index, task_duration, resource_type):
        """
        Checks to see if there is availability for the task
        """
        for i in range(day_index, day_index + task_duration):
            if self.resources[i][resource_type] < 1:
                return False
        return True
    
    def assign(self, day_index, task_duration, resource_type):
        """
        Assigns a task by booking out resources for a certain number of days.
        Does not check if task is assignable - could end up with negative
        availability if assignable() is not run first.
        """
        for i in range(day_index, day_index + task_duration):
            self.resources[i][resource_type] -= 1
    
    def get_resource_types(self):
        """
        Returns a list of the difference resource types in the resources.
        """
        types = []
        for _, day in self.resources.items():
            types += list(day.keys())
        types = list(set(types))
        types.remove('day_index')
        return types
    
    def get_number_of_used_days(self, final_day_index):
        """
        For every day, gets the number of each resource type that is assigned
        to a task up to the final_day_index
        """
        resource_types = self.get_resource_types()
        used_days = dict()
        for i, day in self.resources.items():
            if i > final_day_index:
                break
            day_usage = dict()
            day_usage['day_index'] = day['day_index']
            for resource_type in resource_types:
                originally_available = self.original_resources[i][resource_type]
                available_after_assignment = self.resources[i][resource_type]
                day_usage[resource_type] = originally_available - available_after_assignment
            used_days[i] = day_usage
        return used_days
            


    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 16:31:49 2022

@author: jeremy.hue
"""

class Planner:
    
    def __init__(self, resource_pool, tasks, start_day=None):
        """
        resource_pool should a ResourcePool object.
        tasks should a list of Task objects
        """
        self.rp = resource_pool
        self.tasks = tasks
        self.day_index = 1
        self.start_day = start_day
    
    def schedule(self):
        # Go through all tables, if any are unassigned and assignable, assign it
        for task in self.tasks:
            if not task.assigned and not task.is_complete():
                subtask_name, resource_type, duration = task.get_current_subtask_requirements()
                if self.rp.assignable(self.day_index, duration, resource_type):
                    self.rp.assign(self.day_index, duration, resource_type)
                    task.set_assigned()

    def plan(self):
        while len([t for t in self.tasks if not t.is_complete()]) > 0:
            self.run()
        # results = self.analyze()
        # return results
    
    def analyse(self):
        # total_days 
        pass
    
    def increment_day(self):
        self.day_index += 1
    
    def run(self):
        self.schedule()
        for task in self.tasks:
            task.record_work_done()
        self.increment_day()


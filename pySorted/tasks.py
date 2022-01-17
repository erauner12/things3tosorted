#!/usr/bin/env python3.8

"""Add or modify Tasks."""

import pySorted.parameters as p
import pySorted.sorted as s

class AddTask: #pylint: disable=too-many-instance-attributes, too-few-public-methods
    '''
    Create a call to add a Task to Sorted.
    All parameters are optional.
    If neither the when nor list-id are specified, the to-do will be added to the inbox.
    '''
    def __init__( #pylint: disable=too-many-arguments, too-many-locals
        self,
        title=None,
        date=None,
        list=None):

        self.__name__ = "add"
        self.title = p.Title(title).title
        self.date = p.Date(date).date
        self.list = p.List(list).list
        
        
        self.callback_url = s.callback_from_obj(self)

        self = s.x_call_handler(self) #pylint: disable=self-cls-assignment

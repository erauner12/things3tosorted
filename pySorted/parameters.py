#!/usr/bin/env python3.8

"""Create parameters for Tasks and Events"""

import re
import urllib.parse

# SUPPORT ITEMS FOR PARAMS

def is_string(string, usage):
    '''Verify given variable is a string.'''
    if not isinstance(string, str):
        raise Exception("{} must be a string.".format(usage))
    return True

def is_list(values, usage):
    '''Verify given variable is a list.'''
    if not isinstance(values, list):
        raise Exception("{} must be a string.".format(usage))
    return True

def url_encode(text):
    '''Encode given variable as url encoded string.'''
    return urllib.parse.quote(text)

def is_iso_8601(date, usage):
    '''Check if given variable is a ISO8601 format.'''
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$' #pylint: disable=line-too-long
    match_iso8601 = re.compile(regex).match
    try:
        if match_iso8601(date) is not None:
            return True
    except Exception as issue:
        print("{} must be a ISO8601 formatted string.".format(usage))
        raise issue
    return False


class Title: #pylint: disable=too-few-public-methods
    ''''
    String. The title of the to-do to add.
    Ignored if titles is also specified.
    '''
    def __init__(self, title):
        if title is None:
            self.title = None
            return
        if title is False:
            self.title = ""
            return
        is_string(title, "Title")
        self.title =  url_encode(title)
        
        
class Date: #pylint: disable=too-few-public-methods
    '''
    ISO8601 date time string.
    The date to set as the creation date for the to-do in the database.
    Ignored if the date is in the future.
    '''
    def __init__(self, date):
        if date is None:
            self.date = None
            return
        is_iso_8601(date, "StartDate")

        self.date = date
        

class List: #pylint: disable=too-few-public-methods
    '''
    Comma separated strings corresponding to the titles of tags.
    Replaces all current tags.
    Does not apply a tag if the specified tag doesn’t exist.
    '''
    def __init__(self, list=None):
        if not list:
            self.list = None
            return

        self.list = url_encode(list)


class EarlyAlert: #pylint: disable=too-few-public-methods
    '''
    earlyAlert (optional)
    Early Alert of item in minutes. Set to ‘none’ for No Alert.
    '''
    def __init__(self, earlyAlert):
        if earlyAlert is None:
            self.earlyAlert = None
            return
        is_string(earlyAlert, "EarlyAlert")

        self.earlyAlert = earlyAlert
        
class Duration: #pylint: disable=too-few-public-methods
    '''
    duration (optional)
    Duration of item in minutes, also used to calculate end date for event.
    '''
    def __init__(self, duration):
        if duration is None:
            self.duration = None
            return
        is_string(duration, "duration")

        self.duration = duration
        

class Tags: #pylint: disable=too-few-public-methods
    '''
    tags (optional):
    A list of tag titles separated by comma.
    ''' 
    def __init__(self, tags=None):
        if not tags:
            self.tags = None
            return
        tags_string = ''
        for tag in tags:
            is_string(tag, "{}".format(tag))
            if tags_string == '':
                tags_string += tag
            else:
                tags_string += ','
                tags_string += tag

        self.tags = url_encode(tags_string)
# Copyright (C) 2009 - 2021 Jason Scheunemann <jason.scheunemann@gmail.com>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# -*- coding: utf-8 -*-
"""Class PySubscribe

Class used to supply a publish/subscribe framework. Allows observers to
subscribe to events. The publisher will notify observers and execute registered
callback. All subscribers should register their callbacks in the form of
def callback(**kwargs) to allow for a variable number of keyword arguments.
"""

class PySubscribe:
    def __init__(self):
        self.__listeners = []

    def notify_listeners(self, event, **kwargs):
        """This function doesn't return any value (returns None).

        Keyword arguments:
        event  -- String representing an event that just fired.
        kwargs -- Key/value collection supplied as arguments to registerd
                  callback function.

        Notify subscribers the indicated event has fired, the callback function
        will be called using kwargs as arguments.
        """

        for listener in self.__listeners:
            if listener['event'] == event:
                if kwargs.__len__() == 0:
                    listener['callback']()
                elif kwargs.__len__() == 1:
                    listener['callback'](kwargs[list(kwargs.keys())[0]])
                else:
                    listener['callback'](**kwargs)

    def add_event_listener(self, event, callback):
        """Return object added to listeners if not aleady registered, else None.

        Keyword arguments:
        event    -- String representing event requested for subscription.
        callback -- Callback function to be called when registerd event is
                    fired.

        Register subscriber to be notified of specified event, callback will be
        used as callback.
        """

        add_event = True
        new_listener = None

        for listener in self.__listeners:
            if listener['event'] == event:
                if listener['callback'] == callback:
                    add_event = False

        if add_event:
            new_listener = {
                "event": event,
                "callback": callback
            }

            self.__listeners.append(new_listener)

        return new_listener

    def on(self, event, callback):
        """Passthrough funciton for add_event_listener, added for convenience"""
        return self.add_event_listener(event, callback)

    def remove_event_listener(self, event, callback):
        """This function doesn't return any value (returns None).

        Keyword arguments:
        event    -- String representing the event requested for unsubscription.
        callback -- Callback function registered with event.

        Unregister subscriber using event and callback as signature for removal.
        """

        subject = {
            "event": event,
            "callback": callback
        }

        for listener in self.__listeners:
            if listener == subject:
                self.__listeners.remove(listener)

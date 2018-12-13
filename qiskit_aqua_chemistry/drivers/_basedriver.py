# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

"""
This module implements the abstract base class for driver modules.

To create add-on driver modules subclass the BaseDriver class in this module.
Doing so requires that the required driver interface is implemented.
"""

from abc import ABC, abstractmethod
import copy


class BaseDriver(ABC):
    """
    Base class for Drivers.

    This method should initialize the module and its configuration, and
    use an exception if a component of the module is available.

    """
    @abstractmethod
    def __init__(self):
        if not self.check_driver_valid():
            raise ImportError("{} is not available since missing dependent packages.".format(
                self.__class__.__name__))

        self._configuration = copy.deepcopy(self.CONFIGURATION)
        self._work_path = None

    @property
    def configuration(self):
        """Return driver configuration."""
        return self._configuration

    @staticmethod
    def check_driver_valid():
        """Checks if drivers is ready for use"""
        return True

    @property
    def work_path(self):
        return self._work_path

    @work_path.setter
    def work_path(self, new_work_path):
        self._work_path = new_work_path

    @abstractmethod
    def run(self, section):
        pass

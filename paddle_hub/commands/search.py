# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from paddle_hub.common.logger import logger
from paddle_hub.commands.base_command import BaseCommand, ENTRY
from paddle_hub.common import utils
from paddle_hub.common.hub_server import default_hub_server
import argparse


class SearchCommand(BaseCommand):
    name = "search"

    def __init__(self, name):
        super(SearchCommand, self).__init__(name)
        self.show_in_help = True
        self.description = "Search a paddle hub module with keyword."
        self.parser = self.parser = argparse.ArgumentParser(
            description=self.__class__.__doc__,
            prog='%s %s <key>' % (ENTRY, name),
            usage='%(prog)s',
            add_help=False)

    def exec(self, argv):
        if not argv:
            print("ERROR: Please specify a key\n")
            self.help()
            return False

        module_name = argv[0]
        module_list = default_hub_server.search_module(module_name)
        text = "\n"
        text += "  %-20s\t\t%s\n" % ("ModuleName", "ModuleVersion")
        text += "  %-20s\t\t%s\n" % ("--", "--")
        for module_name, module_version in module_list:
            text += "  %-20s\t\t%s\n" % (module_name, module_version)
        print(text)
        return True


command = SearchCommand.instance()

"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from programy.utils.logging.ylogger import YLogger

from programy.config.section import BaseSectionConfigurationData
from programy.config.brain.service import BrainServiceConfiguration


class BrainServicesConfiguration(BaseSectionConfigurationData):
    def __init__(self):
        BaseSectionConfigurationData.__init__(self, "services")
        self._services = {}

    def exists(self, name):
        return bool(name in self._services)

    def service(self, name):
        if name in self._services:
            return self._services[name]
        return None

    def services(self):
        return self._services.keys()

    def load_config_section(self, configuration_file, configuration, bot_root):
        services = configuration_file.get_section("services", configuration)
        if services is not None:
            service_keys = configuration_file.get_keys(services)

            for name in service_keys:
                service = BrainServiceConfiguration(name)
                service.load_config_section(configuration_file, services, bot_root)
                self._services[name] = service

        else:
            YLogger.warning(self, "Config section [services] missing from Brain, no services loaded")

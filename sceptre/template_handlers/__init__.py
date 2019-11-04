# -*- coding: utf-8 -*-
import abc
import logging

import six


@six.add_metaclass(abc.ABCMeta)
class TemplateHandler:
    """
    TemplateHandler is an abstract base class that should be inherited
    by all Template Handlers.

    :param arguments: The arguments of the template handler
    :type argument: object
    :param stack: The associated stack of the template handler
    :type stack: sceptre.stack.Stack
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, arguments=None, stack=None):
        self.logger = logging.getLogger(__name__)
        self.arguments = arguments
        self.stack = stack

    def setup(self):
        """
        This method is called at during stack initialisation.
        Implementation of this method in subclasses can be used to do any
        initial setup of the object.
        """
        pass  # pragma: no cover

    @abc.abstractmethod
    def handle(self):
        """
        An abstract method which must be overwritten by all inheriting classes.
        This method is called to retrieve the template.
        Implementation of this method in subclasses must return a string that
        can be interpreted by Sceptre (CloudFormation YAML / JSON, Jinja or Python)
        """
        pass  # pragma: no cover

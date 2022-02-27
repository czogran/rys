# This Python file uses the following encoding: utf-8

from shared.stack_widget.stack_widget import StackWidget

from .joystick_widget import JoystickWidget


class JoystickStack(StackWidget):
    def __init__(self, node=None, plugin=None):
        super(JoystickStack, self).__init__()

        self.mainChildWidget = JoystickWidget(node=node, plugin=self, stack=self)
        self.stack.addWidget(self.mainChildWidget)

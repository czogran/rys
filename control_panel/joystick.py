from rqt_gui_py.plugin import Plugin

from .joystick1 import Joystick1


class Joystick(Plugin):

    def __init__(self, context):
        super(Joystick, self).__init__(context)
        self._node = context.node

        super(Joystick, self).__init__(context)
        self.setObjectName('Test')

        self._widget = Joystick1(context.node, self)

        if context.serial_number() > 1:
            self._widget.setWindowTitle(
                self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        context.add_widget(self._widget)

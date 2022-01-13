# This Python file uses the following encoding: utf-8
import os

import rclpy

from std_msgs.msg import String

from python_qt_binding import QtCore
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtWidgets import QPushButton, QWidget
from ament_index_python import get_resource
from python_qt_binding import loadUi

from .elements.button import Button


import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class ControlPanelWidget(QWidget):
    def __init__(self, node, plugin=None):
        super(ControlPanelWidget, self).__init__()

        self.node = node

        _, package_path = get_resource('packages', 'control_panel')
        ui_file = os.path.join(package_path, 'share', 'control_panel', 'resource', 'control_panel.ui')
        loadUi(ui_file, self)

        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()

        self.defineButtons()

        self.subscription = self.node.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        # self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print(msg.data)
        # self.get_logger().info('I heard: "%s"' % msg.data)

        # node = rclpy.create_node('emulate_kobuki_node')
        #
        # self.pub  = node.create_publisher(String, 'topic', 10)
        #
        # self.hello_str = String()
        # self.hello_str.data = 'hello world'
        # self.pub.publish(self.hello_str)

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key == QtCore.Qt.Key_W:
            self.forwardButtonElement.pressedKeyState()
        elif event.key() == QtCore.Qt.Key_D:
            self.rightButtonElement.pressedKeyState()
        elif event.key() == QtCore.Qt.Key_S:
            self.backwardButtonElement.pressedKeyState()
        elif event.key() == QtCore.Qt.Key_A:
            self.leftButtonElement.pressedKeyState()
        event.accept()

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        key = event.key()
        if key == QtCore.Qt.Key_W:
            self.forwardButtonElement.releasedKeyState()
        elif event.key() == QtCore.Qt.Key_D:
            self.rightButtonElement.releasedKeyState()
        elif event.key() == QtCore.Qt.Key_S:
            self.backwardButtonElement.releasedKeyState()
        elif event.key() == QtCore.Qt.Key_A:
            self.leftButtonElement.releasedKeyState()
        event.accept()

    def settingsClicked(self):
        parent=self.parent()
        parent.setCurrentIndex(1)

    def buttonClicked(self):
        self.pub.publish(self.hello_str)

    def defineButtons(self):
        self.forwardButtonElement = Button(self.findChild(QPushButton, 'forwardButton'))
        self.rightButtonElement = Button(self.findChild(QPushButton, 'rightButton'))
        self.backwardButtonElement = Button(self.findChild(QPushButton, 'backwardButton'))
        self.leftButtonElement = Button(self.findChild(QPushButton, 'leftButton'))

        self.settingsButton.clicked.connect(self.settingsClicked)
        self.forwardButton.clicked.connect(self.buttonClicked)



    def resizeEvent(self, event):
        self.setIconSize()

    def setIconSize(self):
        width = self.backwardButton.size().width() * 0.9
        height = self.backwardButton.size().height() * 0.9
        self.forwardButtonElement.resizeIcon(width, height)
        self.leftButtonElement.resizeIcon(width, height)
        self.rightButtonElement.resizeIcon(width, height)
        self.backwardButtonElement.resizeIcon(width, height)
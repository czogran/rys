# from python_qt_binding.QtWidgets import QWidget
from python_qt_binding.QtCore import QObject
from python_qt_binding.QtWidgets import QWidget


class PidWidget(QWidget):
    def __init__(self, widget):
        super(PidWidget, self).__init__()
        self.widget = widget
        data = self.widget.data

        pidData = data.get('pid', {})
        self.setPidAngle(pidData.get('pidAngle', {}))
        self.setPidSpeed(pidData.get('pidSpeed', {}))

    #     self.connectElements()
    #
    # def connectElements(self):
    #     self.widget.pidAngleKpUI.valueChanged.connect(self.test)
    #     self.widget.pidAngleKiUI.valueChanged.connect(self.test)
    #     self.widget.pidAngleKdUI.valueChanged.connect(self.test)
    #
    #     self.widget.pidSpeedKpUI.valueChanged.connect(self.test)
    #     self.widget.pidSpeedKiUI.valueChanged.connect(self.test)
    #     self.widget.pidSpeedKdUI.valueChanged.connect(self.test)

    def setPidAngle(self, pidAngleData):
        self.widget.pidAngleKpUI.setValue(pidAngleData.get('Kp', 0))
        self.widget.pidAngleKiUI.setValue(pidAngleData.get('Ki', 0))
        self.widget.pidAngleKdUI.setValue(pidAngleData.get('Kd', 0))

    def setPidSpeed(self, pidSpeedData):
        self.widget.pidSpeedKpUI.setValue(pidSpeedData.get('Kp', 0))
        self.widget.pidSpeedKiUI.setValue(pidSpeedData.get('Ki', 0))
        self.widget.pidSpeedKdUI.setValue(pidSpeedData.get('Kd', 0))

    def savePidData(self):
        self.widget.data['pid'] = {
            "pidSpeed": {},
            "pidAngle": {}
        }

        self.widget.data['pid']["pidSpeed"]["Kp"]=self.widget.pidSpeedKpUI.value()
        self.widget.data['pid']["pidSpeed"]["Ki"]=self.widget.pidSpeedKiUI.value()
        self.widget.data['pid']["pidSpeed"]["Kd"]=self.widget.pidSpeedKdUI.value()

        self.widget.data['pid']["pidAngle"]["Kp"] = self.widget.pidAngleKpUI.value()
        self.widget.data['pid']["pidAngle"]["Ki"] = self.widget.pidAngleKiUI.value()
        self.widget.data['pid']["pidAngle"]["Kd"] = self.widget.pidAngleKdUI.value()

    def test(self, event):
        print("event12325")
        print("event")
        print(event)
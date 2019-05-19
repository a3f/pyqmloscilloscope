#!/usr/bin/env python3

"""
Copyright (C) 2016 The Qt Company Ltd.
Contact: https://www.qt.io/licensing/
Copyright (C) 2019 Ahmad Fatoum

This file is based on the Qt Charts module of the Qt Toolkit.

$QT_BEGIN_LICENSE:GPL$
Commercial License Usage
Licensees holding valid commercial Qt licenses may use this file in
accordance with the commercial license agreement provided with the
Software or, alternatively, in accordance with the terms contained in
a written agreement between you and The Qt Company. For licensing terms
and conditions see https://www.qt.io/terms-conditions. For further
information use the contact form at https://www.qt.io/contact-us.

GNU General Public License Usage
Alternatively, this file may be used under the terms of the GNU
General Public License version 3 or (at your option) any later version
approved by the KDE Free Qt Foundation. The licenses are as published by
the Free Software Foundation and appearing in the file LICENSE.GPL3
included in the packaging of this file. Please review the following
information to ensure the GNU General Public License requirements will
be met: https://www.gnu.org/licenses/gpl-3.0.html.

$QT_END_LICENSE$
"""

import sys
from os import path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication, QColor
from PyQt5.QtQml import QQmlContext, QQmlEngine
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QDir, QUrl

import datasource

def main():
    global app

    # sys.argv.extend(['-platform', 'eglfs'])

    # Qt Charts uses Qt Graphics View Framework for drawing, therefore QApplication must be used.
    app = QApplication(sys.argv)

    viewer = QQuickView()

    # The following are needed to make examples run without having to install the module
    # in desktop environments.
    extraImportPath = QGuiApplication.applicationDirPath()
    if sys.platform == 'win32':
        extraImportPath += "/../../../../qml"
    else:
        extraImportPath += "/../../../qml"

    viewer.engine().addImportPath(extraImportPath)
    viewer.engine().quit.connect(app.quit)

    viewer.setTitle("QML Oscilloscope")

    dataSource = datasource.DataSource(viewer)
    viewer.rootContext().setContextProperty("dataSource", dataSource)

    main_qml = path.dirname(__file__) + "/qml/qmloscilloscope/main.qml"
    viewer.setSource(QUrl(main_qml))
    viewer.setResizeMode(QQuickView.SizeRootObjectToView)
    viewer.setColor(QColor("#404040"))
    viewer.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())

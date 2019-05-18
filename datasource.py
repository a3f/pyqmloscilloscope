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

from PyQt5.QtCore import QObject, pyqtSlot, QPointF
from PyQt5.QtChart import QAbstractSeries, QXYSeries, QAreaSeries
from PyQt5.QtQuick import QQuickView, QQuickItem
from math import (sin, pi)
import random

class DataSource(QObject):

    def __init__(self, appViewer):
        QObject.__init__(self, appViewer)
        self.m_appViewer = appViewer
        self.m_index = -1
        self.m_data = []

        self.generateData(0, 5, 1024)

    @pyqtSlot(list)
    def update(self, series):
        if series[0] is None:
            return

        self.m_index += 1
        if (self.m_index > len(self.m_data) - 1):
            self.m_index = 0

        points = self.m_data[self.m_index]
        # Use replace instead of clear + append, it's optimized for performance
        series[0].replace(points)

    @pyqtSlot(int, int, int)
    def generateData(self, typ, rowCount, colCount):
        # Remove previous data
        self.m_data = []

        # Append the new data depending on the type
        for i in range(rowCount):
            points = []

            for j in range(colCount):
                if typ == 0: # data with sin + random component
                    point = QPointF(j, sin(pi / 50 * j) + 0.5 + random.uniform(0, 1))
                elif typ == 1: # linear data
                    point = QPointF(j, i / 10)
                else: # unknown, do nothing
                    point = QPointF(0, 0)

                points.append(point)

            self.m_data.append(points)

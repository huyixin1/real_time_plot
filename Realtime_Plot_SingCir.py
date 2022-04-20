# Import libraries
from numpy import *
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import serial
import time

# Create object serial port
portName = "COM36"                      # replace this port name by yours!143401
baudrate =115200
ser = serial.Serial(portName, baudrate)
#ser.write("0".encode())
# ser = serial.Serial('COM14', 19200, bytesize=8, parity='N', stopbits=1, timeout=1)

### START QtApp #####
app = QtGui.QApplication([])            # you MUST do this once (initialize things)

win = pg.GraphicsWindow(title="Signal from serial port") # creates a window
# pg.PlotWidget().setBackground('w')
p = win.addPlot(title="Realtime plot")  # creates empty space for the plot in the window
p.addLegend()
curve1 = p.plot(pen='#c875c4', name="SMD1001_HCHO")                        # create an empty "plot" (a curve to plot)
curve2 = p.plot(pen='#fe2c54', name="SMD1008_CH4")
curve3 = p.plot(pen='#ffffe4', name="SMD1005B_C2H5OH")
curve4 = p.plot(pen='#03719c', name="SQ2002(1)_CH4")
curve5 = p.plot(pen='#fac205', name="SQ2002(2)_CO")
curve6 = p.plot(pen='#9ffeb0', name="GM-602B_H2S")
curve7 = p.plot(pen='#82cafc', name="GM-102B_NO2")
curve8 = p.plot(pen='#feb308', name="GM-202B_SMOKE")
curve9 = p.plot(pen='#c4a661', name="GM-302B_C2H5OH")
curve10 = p.plot(pen='#ffda03', name="GM-502B_VOC")
curve11 = p.plot(pen='#63b365', name="GM-702B_CO&H2")
curve12 = p.plot(pen='#8b88f8', name="GM-512B_H2S")
curve13 = p.plot(pen='#6258c4', name="GM-402B_GAS")
curve14 = p.plot(pen='#ff7fa7', name="SMD1013_TVOC")
curve15 = p.plot(pen='#895b7b', name="SMD1003_CO")
curve16 = p.plot(pen='#d3494e', name="SMD1002_NH3")
# curve17 = p.plot(pen='#89537b', name="TEM")
# curve18 = p.plot(pen='#d3488e', name="HUM")

windowWidth = 50                       # width of the window displaying the curve
Xm1 = linspace(0,0,windowWidth)          # create array that will contain the relevant time series
Xm2 = linspace(0,0,windowWidth)
Xm3 = linspace(0,0,windowWidth)
Xm4 = linspace(0,0,windowWidth)
Xm5 = linspace(0,0,windowWidth)
Xm6 = linspace(0,0,windowWidth)
Xm7 = linspace(0,0,windowWidth)
Xm8 = linspace(0,0,windowWidth)
Xm9 = linspace(0,0,windowWidth)
Xm10 = linspace(0,0,windowWidth)
Xm11 = linspace(0,0,windowWidth)
Xm12 = linspace(0,0,windowWidth)
Xm13 = linspace(0,0,windowWidth)
Xm14 = linspace(0,0,windowWidth)
Xm15 = linspace(0,0,windowWidth)
Xm16 = linspace(0,0,windowWidth)
Xm15 = linspace(0,0,windowWidth)
Xm16 = linspace(0,0,windowWidth)
# Xm17 = linspace(0,0,windowWidth)
# Xm18 = linspace(0,0,windowWidth)

ptr = 0                      # set first x position

# Realtime data plot. Each time this function is called, the data display is updated
def update():
    global curve1, curve2, curve3, curve4, curve5, curve6, curve7, curve8,\
curve9, curve10, curve11, curve12, curve13, curve14, curve15, curve16,ptr, Xm1, Xm2, Xm3, Xm4, Xm5, Xm6, Xm7, Xm8, Xm9, Xm10, Xm11, Xm12, Xm13, Xm14,Xm15,Xm16,Xm17,Xm18
    Xm1[:-1] = Xm1[1:]                      # shift data in the temporal mean 1 sample left
    Xm2[:-1] = Xm2[1:]
    Xm3[:-1] = Xm3[1:]
    Xm4[:-1] = Xm4[1:]
    Xm5[:-1] = Xm5[1:]
    Xm6[:-1] = Xm6[1:]
    Xm7[:-1] = Xm7[1:]
    Xm8[:-1] = Xm8[1:]
    Xm9[:-1] = Xm9[1:]
    Xm10[:-1] = Xm10[1:]
    Xm11[:-1] = Xm11[1:]
    Xm12[:-1] = Xm12[1:]
    Xm13[:-1] = Xm13[1:]
    Xm14[:-1] = Xm14[1:]
    Xm15[:-1] = Xm15[1:]
    Xm16[:-1] = Xm16[1:]
    # Xm17[:-1] = Xm17[1:]
    # Xm18[:-1] = Xm18[1:]


    value = ser.readline().decode('utf-8')
    t = time.localtime()
    decoded_time = time.strftime('%H:%M:%S', t)
    dataArray = value.split(',')  # read line (single value) from the serial port
    # print(dataArray)
    print([decoded_time]+dataArray)
    Xm1[-1] = float(dataArray[0])                 # vector containing the instantaneous values
    Xm2[-1] = float(dataArray[1])
    Xm3[-1] = float(dataArray[2])
    Xm4[-1] = float(dataArray[3])
    Xm5[-1] = float(dataArray[4])
    Xm6[-1] = float(dataArray[5])
    Xm7[-1] = float(dataArray[6])
    Xm8[-1] = float(dataArray[7])
    Xm9[-1] = float(dataArray[8])
    Xm10[-1] = float(dataArray[9])
    Xm11[-1] = float(dataArray[10])
    Xm12[-1] = float(dataArray[11])
    Xm13[-1] = float(dataArray[12])
    Xm14[-1] = float(dataArray[13])
    Xm15[-1] = float(dataArray[14])
    Xm16[-1] = float(dataArray[15])

    ptr += 1                              # update x position for displaying the curve
    curve1.setData(Xm1)                     # set the curve with this data
    curve1.setPos(ptr,0)                   # set x position in the graph to 0
    curve2.setData(Xm2)                     # set the curve with this data
    curve2.setPos(ptr,0)                   # set x position in the graph to 0
    curve3.setData(Xm3)
    curve3.setPos(ptr, 0)
    curve4.setData(Xm4)
    curve4.setPos(ptr, 0)
    curve5.setData(Xm5)
    curve5.setPos(ptr, 0)
    curve6.setData(Xm6)
    curve6.setPos(ptr, 0)
    curve7.setData(Xm7)
    curve7.setPos(ptr, 0)
    curve8.setData(Xm8)
    curve8.setPos(ptr, 0)
    curve9.setData(Xm9)
    curve9.setPos(ptr, 0)
    curve10.setData(Xm10)
    curve10.setPos(ptr, 0)
    curve11.setData(Xm11)
    curve11.setPos(ptr, 0)
    curve12.setData(Xm12)
    curve12.setPos(ptr, 0)
    curve13.setData(Xm13)
    curve13.setPos(ptr, 0)
    curve14.setData(Xm14)
    curve14.setPos(ptr, 0)
    curve15.setData(Xm15)
    curve15.setPos(ptr, 0)
    curve16.setData(Xm16)
    curve16.setPos(ptr, 0)

    QtGui.QApplication.processEvents()    # you MUST process the plot now


### MAIN PROGRAM #####
# this is a brutal infinite loop calling your realtime data plot
while True:
    update()

### END QtApp ####
pg.QtGui.QApplication.exec_() # you MUST put this at the end
##################
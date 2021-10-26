# BLE-Devices-Distance-Calculator
Python project made in Linux environment. Nearby BLE devices are scanned and estimated distances are calculated using two different methods. Since the variables that the methods should use are different, both methods should be modified depending on the brand of the BLE device used.


<p align="center">

  <img src="https://user-images.githubusercontent.com/56837694/130447224-9ada87a0-0a75-4350-9593-d71348b32aea.gif">

</p>

Dependencies
------------
  1) Python Bluepy Lib
  2) 1-meter RSSI value of the BLE device to be used || Tx Power value of the BLE device to be used

Bluepy Installation
------------

The code needs an executable `bluepy-helper` to be compiled from C source. This is done
automatically if you use the recommended pip installation method (see below). Otherwise,
you can rebuild it using the Makefile in the `bluepy` directory.

To install the current released version, on most Debian-based systems:

    $ sudo apt-get install python-pip libglib2.0-dev
    $ sudo pip install bluepy

For Python 3, you may need to use `pip3`:

    $ sudo apt-get install python3-pip libglib2.0-dev
    $ sudo pip3 install bluepy

*If this fails* you should install from source.

    $ sudo apt-get install git build-essential libglib2.0-dev
    $ git clone https://github.com/IanHarvey/bluepy.git
    $ cd bluepy
    $ python setup.py build
    $ sudo python setup.py install

1-meter-RSSI Algorithm
------------

THIS METHOD NEEDS MEASURED RSSI POWER OF BLE DEVICES IS ALSO KNOWN AS "1 METER RSSI".
THESE MEASURED RSSI POWER MAY VARY FOR EVERY DIFFERENT BRAND BLE DEVICE.(iBEACON, EDDYSTONE, ETC...)
FOR THE MOST ACCURATE RESULT, EVERY BRAND TO BE USED MUST BE MEASURED BY IT'S OWN MEASUREMENT.
THE SHORTER THE INTERVAL, THE MORE STABLE THE SIGNAL.

Tx Power Algorithm
------------

NOT EVERY DEVICE DISPLAYS ITS TX POWER IN SCANNING AND THE DISPLAYERS ARE SHOWING WITH RETURNING CODES AS 0C, 08, ETC...
FOR USING, ALL DEVICE'S TX POWER VALUE MUST HAVE BEEN FOUND IN DBMs.
Not fully resolved

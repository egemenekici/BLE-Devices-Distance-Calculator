from bluepy import btle
import argparse
import sys

class ScanPrint(btle.DefaultDelegate):

    def __init__(self, opts):
        btle.DefaultDelegate.__init__(self)
        self.opts = opts

    def handleDiscovery(self, dev, isNewDev, isNewData):

        print ('    Device : %s (%s), %d dBm' % (dev.addr, dev.addrType, dev.rssi))

        # 1. METHOD TO GET DISTANCE OF BLE DEVICES.
        # THIS METHOD NEEDS BLUETOOTH DEVICE'S TX POWER SIGNAL IN DBM.
        # NOT EVERY DEVICE DISPLAYS ITS TX POWER IN SCANNING AND THE DISPLAYERS ARE SHOWING WITH RETURNING CODES AS 0C, 08, ETC...
        # 0C STANDS FOR AN INVALID CHARACTER EXCEPTION, 08 STANDS FOR INSUFFICIENT AUTHORIZATION.
        # FOR USING, ALL DEVICE'S TX POWER VALUE MUST HAVE BEEN FOUND IN DBMs.
        distance1 = abs(0.89976 * ((int(dev.rssi)/-70) ** 7.7095) + 0.111) # This -70 value needs to be Tx_Power of device.(Tx_power is automated in here.)
        short_distance1 = "%.2f" % distance1
        print('\t' + "First Method Distance(meters):" + str(short_distance1))

        # 2. METHOD TO GET DISTANCE OF BLE DEVICES.
        # THIS METHOD NEEDS MEASURED RSSI POWER OF BLE DEVICES IS ALSO KNOWN AS "1 METER RSSI".
        # THESE MEASURED RSSI POWER MAY VARY FOR EVERY DIFFERENT BRAND BLE DEVICE.(iBEACON, EDDYSTONE, ETC...)
        # FOR THE MOST ACCURATE RESULT, EVERY BRAND TO BE USED MUST BE MEASURED BY IT'S OWN MEASUREMENT.
        # THE SHORTER THE INTERVAL, THE MORE STABLE THE SIGNAL.

        #                       2. METHOD MUST BE USE IN HERE.                          #
        #-------------------------------------------------------------------------------#
        MEASURED_RSSI = -41 #(FOR EXAMPLE: EDDYSTONE BEACONS 1 METER RSSI IS -41 DBM)
        N = 2 #Constant depends on the Environmental factor. Range 2-4
        distance2 = 10 ** ((MEASURED_RSSI - dev.rssi)/(10 * N))
        short_distance2 = "%.2f" % distance2
        print('\t' + "Second Method Distance(meters):" + str(short_distance2))
        #-------------------------------------------------------------------------------#

        for (adtype, desc, value) in dev.getScanData():
            print ('\t' + str(adtype) + '. \'' + desc + ': \'' + value + '\'')

            #                       1. METHOD MUST BE USE IN HERE.                          #
            #-------------------------------------------------------------------------------#
            #if desc == "Tx Power":

                #distance1 = abs(0.89976 * ((int(dev.rssi)/int(value)) ** 7.7095) + 0.111)
                #short_distance1 = "%.2f" % distance1
                #print('\t' + "1. Method Distance(meters):" + str(short_distance1))
            #-------------------------------------------------------------------------------#
                

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--hci', action='store', type=int, default=0,
                        help='Interface number for scan')
    parser.add_argument('-t', '--timeout', action='store', type=int, default=4,
                        help='Scan delay, 0 for continuous')
    parser.add_argument('-s', '--sensitivity', action='store', type=int, default=-128,
                        help='dBm value for filtering far devices')
    parser.add_argument('-d', '--discover', action='store_true',
                        help='Connect and discover service to scanned devices')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Display duplicate adv responses, by default show new + updated')
    parser.add_argument('-n', '--new', action='store_true',
                        help='Display only new adv responses, by default show new + updated')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity')

    arg = parser.parse_args(sys.argv[1:])
    

    btle.Debugging = arg.verbose


    scanner = btle.Scanner(arg.hci).withDelegate(ScanPrint(arg))

    print ("Scanning for devices...")
    devices = scanner.scan(arg.timeout)


if __name__ == "__main__":
    main()

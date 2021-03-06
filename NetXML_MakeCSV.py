# !/usr/bin/python

"""
Author:  Thomas Laurenson
Email:   thomas@thomaslaurenson.com
Website: thomaslaurenson.com
Date:    2016/08/07

Description:
Convert a NetXML file into a CSV file using the NetXML.py API.

Copyright (c) 2016, Thomas Laurenson

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################

>>> CHANGELOG:
    0.1.0       Base functionality
"""

__version__ = "0.1.0"

import sys
import csv
import NetXML

################################################################################
if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description='''NetXML_MakeCSV.py''')
    parser.add_argument("netxml_file",
                        help = "Target NetXML file (e.g. Kismet-20150506-08-23-31-1.netxml)")
    args = parser.parse_args()

    # Parse NetXML file using NetXML.iterparse
    netxml = NetXML.iterparse(args.netxml_file)

    # Set up the CSV writer
    output = csv.writer(sys.stdout, delimiter='\t')
    
    # Write CSV headers
    output.writerow(("type",
                     "network_number",
                     "client_number",
                     "network_type",
                     "mac_address",
                     "essid",
                     "manuf",
                     "channel",
                     "freqmhz",
                     "max_rate",
                     "beacon_rate",
                     "cloaked",
                     "encryption",
                     "privacy",
                     "cipher",
                     "authentication",
                     "wpa_version",
                     "wps",
                     "ssid_frame_type",
                     "carrier",
                     "encoding",
                     "first_time",
                     "last_time",
                     "max_seen_rate",
                     "packets_beacons",
                     "packets_llc",
                     "packets_data",
                     "packets_crypt",
                     "packets_fragments",
                     "packets_retries",
                     "packets_total",
                     "data_size",
                     "min_lat",
                     "min_lon",
                     "min_alt",
                     "min_spd",
                     "max_lat",
                     "max_lon",
                     "max_alt",
                     "max_spd",
                     "peak_lat",
                     "peak_lon",
                     "peak_alt",
                     "avg_lat",
                     "avg_lon",
                     "avg_alt"))     
    
    # Print WirelessNetworks in CSV format to std.out
    current_network_mac = None
    for wn in netxml:
        if isinstance(wn, NetXML.WirelessNetwork):
            current_network_mac = wn.bssid
            output.writerow((wn.netxml_type,
                             wn.number,
                             "",
                             wn.network_type,
                             wn.bssid,
                             wn.ssid.essid,
                             wn.manuf,
                             wn.channel,
                             ";".join(wn.freqmhz),
                             wn.ssid.max_rate,
                             wn.ssid.beaconrate,
                             wn.ssid.cloaked,
                             ";".join(wn.ssid.encryption),
                             wn.ssid.privacy,
                             wn.ssid.cipher,
                             wn.ssid.authentication,
                             wn.ssid.wpa_version,
                             wn.ssid.wps,
                             wn.ssid.frame_type,
                             "",
                             "",                             
                             wn.first_time, 
                             wn.last_time,
                             wn.maxseenrate,
                             wn.ssid.packets,
                             wn._packets.llc,
                             wn._packets.data,
                             wn._packets.crypt,
                             wn._packets.fragments,
                             wn._packets.retries,
                             wn._packets.total,
                             wn.datasize,
                             wn._gps.min_lat,
                             wn._gps.min_lon,
                             wn._gps.min_alt,
                             wn._gps.min_spd,
                             wn._gps.max_lat,
                             wn._gps.max_lon,
                             wn._gps.max_alt,
                             wn._gps.max_spd,
                             wn._gps.peak_lat,
                             wn._gps.peak_lon,
                             wn._gps.peak_alt,
                             wn._gps.avg_lat,
                             wn._gps.avg_lon,
                             wn._gps.avg_alt))
        if isinstance(wn, NetXML.WirelessClient):
            if current_network_mac == wn.client_mac:
                continue
            output.writerow((wn.netxml_type,
                             wn.network_number,
                             wn.number,
                             wn.type,
                             wn.client_mac,
                             "",
                             wn.client_manuf,
                             wn.channel,
                             ";".join(wn.freqmhz),
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             wn.carrier,
                             wn.encoding,                            
                             wn.first_time, 
                             wn.last_time,
                             wn.maxseenrate,
                             "",
                             wn._packets.llc,
                             wn._packets.data,
                             wn._packets.crypt,
                             wn._packets.fragments,
                             wn._packets.retries,
                             wn._packets.total,
                             wn.datasize,
                             wn._gps.min_lat,
                             wn._gps.min_lon,
                             wn._gps.min_alt,
                             wn._gps.min_spd,
                             wn._gps.max_lat,
                             wn._gps.max_lon,
                             wn._gps.max_alt,
                             wn._gps.max_spd,
                             wn._gps.peak_lat,
                             wn._gps.peak_lon,
                             wn._gps.peak_alt,
                             wn._gps.avg_lat,
                             wn._gps.avg_lon,
                             wn._gps.avg_alt))


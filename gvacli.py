#!/usr/bin/python
import sys
from datetime import datetime, timedelta
import argparse
import httplib
import urllib
import logging
import anyjson
import cgi
import cgitb
from prettytable import PrettyTable

WSHOST = "gva.atipik.ch"
WSURI = "/api2/flights?lastSync=%s"
TIME_FORMAT = "%d-%m-%Y %H:%M:%S"

KEY_FLIGHTID = "sFlightIdentity"
KEY_DESTINATION = "sAirport"
KEY_DESTINATION_CODE = "sAirportCodeDestination"
KEY_AIRCRAFT = "sAircraft"
KEY_REGISTRATION = 'sAircraftRegistration'
KEY_STATUS = "sFlightStatus"
KEY_AIRLINE = "sCompany"
KEY_SCHED_DEP = "dScheduledDeparture"
KEY_ACTUAL_DEP = "dPublicDeparture"
KEY_AIRBORN = "dAirborn"
KEY_DOUANE = 'bControleDouane'
KEY_GATE = 'sGate'

DISPLAYED_KEYS = [
  KEY_DESTINATION,
  KEY_FLIGHTID,
  KEY_AIRLINE,
  KEY_GATE,
  KEY_AIRCRAFT,
  KEY_REGISTRATION,
  KEY_STATUS]

def fetch_departures(data):
  departures = []
  now = datetime.now()
  for flight in data['departures']:
    values = []
    sched_departure = datetime.strptime(flight[KEY_SCHED_DEP], TIME_FORMAT)
    if args.all and sched_departure.day != now.day:
      continue
    values.append(sched_departure.strftime("%H:%M"))
    if flight[KEY_ACTUAL_DEP] is not None:
      actual_departure = datetime.strptime(flight[KEY_ACTUAL_DEP], TIME_FORMAT)
      values.append(actual_departure.strftime("%H:%M"))
    else:
      values.append("ON TIME")
    if flight[KEY_DOUANE] == '1':
      flight[KEY_DESTINATION] = "%s [P]" % flight[KEY_DESTINATION]
    if not flight[KEY_STATUS]:
      flight[KEY_STATUS] = 'Scheduled'
    values.extend([flight[key] for key in DISPLAYED_KEYS])
    departures.append(values)

  return departures

def parse_arguments():
  parser = argparse.ArgumentParser()

  parser.add_argument('-a', '--all',
    action="store_true",
    help="Get all outgoing flights for the current day (slow)")

  args = parser.parse_args()
  return args

def main():
  global args
  args = parse_arguments()

  last_sync = ""
  if not args.all:
    now = datetime.now()
    last_sync = (now - timedelta(hours=3)).strftime("%Y-%m-%d %H:%M:%S")
    last_sync = urllib.quote_plus(last_sync)

  connection = httplib.HTTPConnection(WSHOST, 80)
  uri = WSURI % last_sync
  connection.request("GET", uri)
  response = connection.getresponse()

  if response.status != httplib.OK:
    logging.error("The webservice didn't return OK :(")
    return 1

  json = response.read()
  data = anyjson.deserialize(json)
  departures = fetch_departures(data)

  cgitb.enable()

  table = PrettyTable(['Scheduled',
    'Expected', 'Destination',
    'Flight', 'Airline', 'Gate',
    'Aircraft', 'Reg', 'Status'])
  table.align = 'l'
  for departure in sorted(departures):
    table.add_row(departure)
  print table

  return 0

if __name__ == "__main__":
  sys.exit(main())

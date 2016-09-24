# gvacli
CLI for the Geneva Airport departures/arrivals API

It currently prints only departures, next time I'm bored I will add support for
arrivals.

Example output:

```
~ $ gvacli
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
| Scheduled | Expected | Destination      | Flight  | Airline                  | Gate | Aircraft                  | Status    |
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
| 06:00     | 06:08    | ALICANTE         | EZS1425 | EASYJET                  | D23  | AIRBUS  A319              | Flying    |
| 06:00     | ON TIME  | PRAGUE           | LX1472  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 06:00     | ON TIME  | ZURICH           | LX2801  | SWISS                    |      | AVRO RJ100                | Scheduled |
| 06:05     | 06:00    | CATANIA          | EZS1561 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 06:10     | ON TIME  | MARRAKECH [P]    | LX2200  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 06:10     | ON TIME  | MUNICH           | LX1120  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 06:30     | 06:36    | NICE             | EZS1377 | EASYJET                  | F60  | AIRBUS  A320              | Flying    |
| 06:45     | 06:40    | NICE             | EZS1377 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 06:55     | ON TIME  | FRANKFURT        | LH1229  | LUFTHANSA                |      | BOEING 737-300            | Scheduled |
| 07:00     | 06:55    | MADRID           | EZS1415 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 07:00     | ON TIME  | ZURICH           | F7022   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 07:05     | ON TIME  | ISTANBUL IST [P] | TK1922  | TURKISH AIRLINES         |      | AIRBUS  A320              | Scheduled |
| 07:10     | ON TIME  | BARCELONA        | LX1940  | SWISS                    |      | AVRO RJ100                | Scheduled |
| 07:10     | ON TIME  | DUBLIN [P]       | LX410   | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 07:15     | 07:10    | PARIS ORY        | EZS1399 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 07:15     | ON TIME  | AMSTERDAM        | KL1924  | KLM ROYAL DUTCH AIRLINES |      | EMBRAER 190               | Scheduled |
| 07:20     | ON TIME  | PARIS CDG        | AF1243  | AIR FRANCE               |      | AIRBUS  A320              | Scheduled |
| 07:25     | ON TIME  | LISBON           | LX2092  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 07:25     | ON TIME  | ZURICH           | LX2805  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 07:30     | ON TIME  | LONDON LHR [P]   | BA723   | BRITISH AIRWAYS          |      | AIRBUS  A319              | Scheduled |
| 07:30     | ON TIME  | LONDON LHR [P]   | LX352   | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 08:15     | ON TIME  | MADRID           | IB3489  | IBERIA                   |      | AIRBUS  A320              | Scheduled |
| 08:30     | ON TIME  | OLBIA            | F7420   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 08:40     | ON TIME  | MOSCOW DME [P]   | LX1336  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 08:50     | ON TIME  | BARCELONA        | EZY1403 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 09:30     | ON TIME  | FRANKFURT        | LH1213  | LUFTHANSA                |      | AIRBUS  A319              | Scheduled |
| 09:40     | 09:42    | LONDON LGW [P]   | EZS8467 | EASYJET                  | C52  | AIRBUS  A320              | Flying    |
| 09:45     | ON TIME  | MUNICH           | LX1122  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 09:55     | ON TIME  | FLORENCE         | F7130   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 10:00     | ON TIME  | ZURICH           | LX2807  | SWISS                    |      | BOEING 777-300ER          | Scheduled |
| 10:15     | ON TIME  | PORTO            | EZY1451 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 10:20     | ON TIME  | PALMA MALLORCA   | LX2160  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 10:30     | ON TIME  | LONDON LTN [P]   | EZY2052 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 10:40     | ON TIME  | OSLO             | DY1603  | NORWEGIAN                |      | BOEING 737-800 (WINGLETS) | Scheduled |
| 10:45     | ON TIME  | COPENHAGEN       | EZS1465 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 10:50     | ON TIME  | BRISTOL [P]      | EZY6154 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 10:50     | ON TIME  | FRANKFURT        | LH1215  | LUFTHANSA                |      | BOEING 737-300            | Scheduled |
| 11:00     | ON TIME  | IBIZA            | F7380   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 11:00     | ON TIME  | ZURICH           | LX2809  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 11:20     | 11:30    | BASTIA           | EZS1301 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 11:35     | ON TIME  | BARCELONA        | EZS1405 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 11:35     | ON TIME  | NICE             | LX528   | SWISS                    |      | AVRO RJ100                | Scheduled |
| 11:45     | ON TIME  | NEW YORK [P]     | LX022   | SWISS                    |      | AIRBUS A330-300           | Scheduled |
| 12:20     | ON TIME  | ATHENS           | LX1822  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 12:25     | ON TIME  | PORTO            | EZS1453 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 12:45     | 12:54    | HURGHADA [P]     | EZS1569 | EASYJET                  | B44  | AIRBUS  A320              | Flying    |
| 12:55     | ON TIME  | LONDON LHR [P]   | LX354   | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 13:00     | ON TIME  | LONDON LGW [P]   | EZY8467 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 13:10     | 19:36    | CAGLIARI         | F71162  | ETIHAD REGIONAL (DARWIN) | A6   | SAAB 2000                 | Flying    |
| 13:30     | ON TIME  | MUNICH           | LX1124  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 13:30     | ON TIME  | PALMA MALLORCA   | F7392   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 13:30     | ON TIME  | VENICE           | F7190   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 13:40     | ON TIME  | LONDON LCY [P]   | LX434   | SWISS                    |      | AVRO RJ100                | Scheduled |
| 13:45     | ON TIME  | PALMA MALLORCA   | WK1486  | EDELWEISS AIR            |      | AIRBUS  A320              | Scheduled |
| 13:55     | ON TIME  | FRANKFURT        | LH1217  | LUFTHANSA                |      | AIRBUS  A319              | Scheduled |
| 13:55     | ON TIME  | ROME FCO         | LX1754  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 14:00     | 14:17    | REYKJAVIK        | FI565   | ICELANDAIR               | A7   | BOEING 757-200 (WINGLETS) | Flying    |
| 14:05     | 14:16    | REYKJAVIK        | EZS1521 | EASYJET                  | D71  | AIRBUS  A320              | Flying    |
| 14:30     | ON TIME  | NAPLES           | EZY1553 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 14:45     | ON TIME  | ZURICH           | LX2811  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 14:50     | 15:27    | ISTANBUL IST [P] | TK1330  | TURKISH AIRLINES         | B42  | BOEING 737-800 (WINGLETS) | Flying    |
| 14:55     | ON TIME  | FRANKFURT        | LH1219  | LUFTHANSA                |      | BOEING 737-300            | Scheduled |
| 15:10     | 15:19    | MYKONOS          | EZS1577 | EASYJET                  | A10  | AIRBUS  A319              | Flying    |
| 15:20     | 15:25    | MANCHESTER [P]   | EZY1952 | EASYJET                  | B43  | AIRBUS  A320              | Flying    |
| 15:25     | 15:41    | BRISTOL [P]      | EZY6154 | EASYJET                  | C52  | AIRBUS  A320              | Flying    |
| 15:35     | 15:48    | PORTO            | EZY1457 | EASYJET                  | D27  | AIRBUS  A320              | Flying    |
| 15:35     | 16:25    | TOULOUSE         | EZY1473 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 15:40     | 15:54    | LONDON LHR [P]   | LX348   | SWISS                    | C53  | BOMBARDIER Q400           | Flying    |
| 15:45     | ON TIME  | PORTO            | EZY1457 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 15:45     | ON TIME  | ZURICH           | LX2813  | SWISS                    |      | AVRO RJ100                | Scheduled |
| 15:50     | 16:14    | HERAKLION        | EZS1559 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 15:50     | ON TIME  | LONDON LHR [P]   | LX348   | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 15:55     | 17:22    | MARRAKECH [P]    | EZS1313 | EASYJET                  | C54  | AIRBUS  A320              | Flying    |
| 16:00     | 16:10    | MONASTIR [P]     | TU509   | TUNISAIR                 | B32  | AIRBUS  A320              | Flying    |
| 16:00     | 16:22    | LONDON LGW [P]   | EZY8477 | EASYJET                  | B34  | AIRBUS  A319              | Flying    |
| 16:00     | ON TIME  | LILLE            | EZS1471 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 16:00     | ON TIME  | LONDON LGW [P]   | EZS8475 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 16:05     | 17:04    | DUBLIN [P]       | EI685   | AER LINGUS               | B31  | AIRBUS  A320              | Flying    |
| 16:30     | ON TIME  | HAMBURG          | EZY3426 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 16:35     | 16:51    | FLORENCE         | F7130   | ETIHAD REGIONAL (DARWIN) | A7   | SAAB 2000                 | Flying    |
| 16:45     | 16:53    | ATHENS           | LX1820  | SWISS                    | A10  | AIRBUS  A319              | Flying    |
| 16:45     | 17:12    | LISBON           | EZY1447 | EASYJET                  | D25  | AIRBUS  A319              | Flying    |
| 16:45     | ON TIME  | VALENCIA         | F7350   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 17:00     | 18:35    | BIARRITZ         | F7470   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 17:00     | ON TIME  | ZURICH           | F7024   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 17:05     | 17:15    | MUNICH           | LX1126  | SWISS                    | A8   | AIRBUS  A319              | Flying    |
| 17:05     | ON TIME  | MUNICH           | LX1126  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 17:20     | 17:25    | AMSTERDAM        | KL1932  | KLM ROYAL DUTCH AIRLINES | A2   | EMBRAER 190               | Flying    |
| 17:20     | 17:31    | AMMAN [P]        | RJ149   | ROYAL JORDANIAN          | B43  | AIRBUS  A319              | Flying    |
| 17:20     | 17:36    | CASABLANCA [P]   | AT931   | ROYAL AIR MAROC          | B33  | BOEING 737-800 (WINGLETS) | Flying    |
| 17:20     | ON TIME  | BORDEAUX         | EZY1371 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 17:25     | 17:47    | MALAGA           | EZS1435 | EASYJET                  | D23  | AIRBUS  A319              | Flying    |
| 17:35     | 17:40    | PRISTINA [P]     | EZS1483 | EASYJET                  | C51  | AIRBUS  A319              | Flying    |
| 17:35     | 17:43    | LONDON LHR [P]   | BA733   | BRITISH AIRWAYS          | B32  | AIRBUS  A319              | Flying    |
| 17:35     | ON TIME  | EDINBURGH [P]    | EZY6906 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 17:40     | 17:50    | NICE             | LX528   | SWISS                    | F64  | AIRBUS  A319              | Flying    |
| 17:45     | 17:45    | VENICE           | EZY3326 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 17:45     | 18:34    | LONDON LHR [P]   | LX356   | SWISS                    | B42  | AVRO RJ100                | Flying    |
| 17:50     | 18:00    | CORFU            | LX2352  | SWISS                    | A9   | AIRBUS  A320              | Flying    |
| 17:50     | 18:04    | ZURICH           | LX2817  | SWISS                    | A4   | AVRO RJ100                | Flying    |
| 17:50     | 18:29    | MALTA            | EZS1495 | EASYJET                  | D71  | AIRBUS  A319              | Flying    |
| 17:50     | ON TIME  | LONDON LHR [P]   | LX356   | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 17:50     | ON TIME  | ZURICH           | LX2817  | SWISS                    |      | AVRO RJ100                | Scheduled |
| 17:55     | 17:58    | FRANKFURT        | LH1223  | LUFTHANSA                | A5   | BOEING 737-300            | Flying    |
| 17:55     | ON TIME  | FRANKFURT        | LH1223  | LUFTHANSA                |      | BOEING 737-300            | Scheduled |
| 17:55     | ON TIME  | MADRID           | EZS1417 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 17:55     | ON TIME  | MALAGA           | LX2104  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 18:00     | 18:11    | PARIS CDG        | AF1343  | AIR FRANCE               | F61  | AIRBUS  A319              | Flying    |
| 18:00     | 18:38    | DOHA [P]         | QR100   | QATAR AIRWAYS            | C53  | BOEING 787-8 DREAMLINER   | Flying    |
| 18:05     | ON TIME  | LONDON LCY [P]   | LX446   | SWISS                    |      | AVRO RJ100                | Scheduled |
| 18:10     | 18:08    | BRINDISI         | EZS1545 | EASYJET                  | A10  | AIRBUS  A319              | Flying    |
| 18:10     | 18:50    | ALGIERS [P]      | LX2206  | SWISS                    | B34  | AIRBUS  A320              | Flying    |
| 18:20     | 19:44    | OLBIA            | LX2370  | SWISS                    | A1   | AIRBUS  A320              | Flying    |
| 18:25     | 18:40    | LISBON           | TP953   | TAP PORTUGAL             | A3   | AIRBUS A320 (SHARKLETS)   | Flying    |
| 18:25     | 18:46    | ANTALYA [P]      | PC5638  | PEGASUS                  | B33  | BOEING 737-800 (WINGLETS) | Flying    |
| 18:25     | ON TIME  | PORTO            | LX2078  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 18:30     | 18:54    | ISTANBUL IST [P] | TK1920  | TURKISH AIRLINES         | B44  | AIRBUS A321 (SHARKLETS)   | Flying    |
| 18:30     | 19:08    | MADRID           | IB3493  | IBERIA                   | A4   | AIRBUS A320 (SHARKLETS)   | Flying    |
| 18:35     | ON TIME  | MADRID           | LX2048  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 18:45     | 18:53    | LONDON LHR [P]   | BA735   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 18:50     | 19:02    | IBIZA            | EZS1519 | EASYJET                  | D75  | AIRBUS  A320              | Flying    |
| 18:55     | 19:04    | FRANKFURT        | LH1225  | LUFTHANSA                | A1   | BOEING 737-300            | Flying    |
| 19:00     | 18:58    | ROME FCO         | AZ577   | ALITALIA                 | A2   | EMBRAER 175               | Flying    |
| 19:00     | 19:00    | LUGANO           | F7017   | ETIHAD REGIONAL (DARWIN) | D25  | SAAB 2000                 | Flying    |
| 19:05     | 19:56    | PALMA MALLORCA   | EZS1515 | EASYJET                  | A10  | AIRBUS  A320              | Departed  |
| 19:05     | 20:00    | PORTO            | TP943   | TAP PORTUGAL             | D23  | EMBRAER 190               | Departed  |
| 19:10     | 19:13    | BARCELONA        | EZS1409 | EASYJET                  | D21  | AIRBUS  A320              | Flying    |
| 19:10     | 19:15    | RHODOS           | A3485   | AEGEAN AIRLINES          | A8   | AIRBUS  A320              | Flying    |
| 19:15     | 19:19    | LONDON LTN [P]   | EZY2058 | EASYJET                  | B43  | AIRBUS  A320              | Flying    |
| 19:15     | 19:24    | ZURICH           | LX2815  | SWISS                    | A9   | AIRBUS  A319              | Flying    |
| 19:15     | ON TIME  | ZURICH           | LX2815  | SWISS                    |      | AIRBUS  A321              | Scheduled |
| 19:20     | 19:18    | BARCELONA        | LX1946  | SWISS                    | A5   | AIRBUS  A320              | Flying    |
| 19:20     | ON TIME  | BARCELONA        | LX1946  | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 19:25     | 19:35    | WARSAW           | LO416   | LOT POLISH AIRLINES      | A3   | EMBRAER 175               | Flying    |
| 19:35     | 19:41    | FRANKFURT        | LH1227  | LUFTHANSA                | D27  | BOMBARDIER CRJ-900        | Flying    |
| 19:40     | ON TIME  | BRUSSELS         | EZS1537 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 20:10     | 20:00    | VIENNA           | OS576   | AUSTRIAN                 | A2   | FOKKER 100                | Departed  |
| 20:10     | ON TIME  | PARIS ORY        | EZS1393 | EASYJET                  |      | AIRBUS  A319              | Scheduled |
| 20:25     | ON TIME  | BEIJING [P]      | CA862   | AIR CHINA                | C53  | AIRBUS A330-200           | Boarding  |
| 20:30     | ON TIME  | LUGANO           | F7017   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Scheduled |
| 20:30     | ON TIME  | PARIS CDG        | AF1043  | AIR FRANCE               | F61  | AIRBUS  A320              | Boarding  |
| 20:50     | ON TIME  | LONDON LHR [P]   | LX358   | SWISS                    |      | AIRBUS  A320              | Scheduled |
| 20:50     | ON TIME  | ZURICH           | LX2819  | SWISS                    |      | AIRBUS  A319              | Scheduled |
| 20:50     | ON TIME  | ZURICH           | LX2819  | SWISS                    | A9   | AIRBUS  A319              | Scheduled |
| 20:55     | ON TIME  | BARCELONA        | EZY1413 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 21:00     | ON TIME  | AMSTERDAM        | EZY1359 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 21:25     | ON TIME  | ABU DHABI [P]    | EY052   | ETIHAD AIRWAYS           | C55  | AIRBUS A330-300           | Scheduled |
| 21:35     | ON TIME  | LONDON LTN [P]   | EZY2062 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 21:45     | ON TIME  | DUBAI [P]        | EK084   | EMIRATES                 | C51  | BOEING 777-300ER          | Scheduled |
| 21:45     | ON TIME  | LONDON LGW [P]   | EZY8485 | EASYJET                  |      | AIRBUS  A320              | Scheduled |
| 21:50     | ON TIME  | MOSCOW SVO [P]   | SU2383  | AEROFLOT                 | B33  | AIRBUS  A320              | Scheduled |
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
```

If a *[P]* appears next to the name of the destination that means that's a
non-Schengen flight.

I have no affiliation with [Geneva International Airport](http://gva.ch) and
the software is provided without guarantee. Enjoy.

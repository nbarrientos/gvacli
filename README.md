**This project is no longer maintained**. It has been replaced by [go-gvacli](https://github.com/herver/go-gvacli).

# gvacli
CLI for the Geneva Airport departures/arrivals API

It currently prints only departures of the current day. Next time I'm bored I
will add support for arrivals.

Example output:

```
~ $ gvacli -a
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
| Scheduled | Expected | Destination      | Flight  | Airline                  | Gate | Aircraft                  | Status    |
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
| 06:00     | 06:05    | PRISTINA [P]     | LX1430  | SWISS                    | C54  | AIRBUS  A320              | Flying    |
| 06:00     | 06:06    | PORTO            | EZS1453 | EASYJET                  | D71  | AIRBUS  A319              | Flying    |
| 06:00     | 06:08    | ALICANTE         | EZS1425 | EASYJET                  | D23  | AIRBUS  A319              | Flying    |
| 06:00     | 06:10    | AJACCIO          | EZS1305 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 06:00     | ON TIME  | ZURICH           | LX2801  | SWISS                    |      | AVRO RJ100                | Cancelled |
| 06:10     | 06:21    | MUNICH           | LX1120  | SWISS                    | A6   | AIRBUS  A319              | Flying    |
| 06:10     | 06:23    | MALAGA           | EZS1431 | EASYJET                  | D25  | AIRBUS  A320              | Flying    |
| 06:15     | 06:19    | BUDAPEST         | EZS1333 | EASYJET                  | D27  | AIRBUS  A320              | Flying    |
| 06:15     | 06:24    | FARO             | EZS1461 | EASYJET                  | A2   | AIRBUS  A320              | Flying    |
| 06:20     | 06:30    | NANTES           | EZS1361 | EASYJET                  | F63  | AIRBUS  A320              | Flying    |
| 06:25     | 06:38    | SKOPJE [P]       | LX1438  | SWISS                    | B31  | AVRO RJ100                | Flying    |
| 06:30     | 06:36    | NICE             | EZS1377 | EASYJET                  | F60  | AIRBUS  A320              | Flying    |
| 06:30     | 06:40    | LISBON           | TP949   | TAP PORTUGAL             | A3   | AIRBUS  A320              | Flying    |
| 06:30     | 09:05    | SANTIAGO C       | EZS1337 | EASYJET                  | D71  | AIRBUS  A320              | Flying    |
| 06:45     | 06:48    | BARCELONA        | EZS1401 | EASYJET                  | D75  | AIRBUS  A319              | Flying    |
| 06:55     | 06:59    | STOCKHOLM        | LX1232  | SWISS                    | D73  | AIRBUS  A320              | Flying    |
| 06:55     | 07:08    | FRANKFURT        | LH1229  | LUFTHANSA                | D76  | BOEING 737-300            | Flying    |
| 07:00     | 07:04    | LONDON LGW [P]   | EZS8463 | EASYJET                  | B34  | AIRBUS  A319              | Flying    |
| 07:00     | 07:13    | ROME FCO         | AZ569   | ALITALIA                 | D72  | EMBRAER 175               | Flying    |
| 07:00     | 07:27    | ZURICH           | F7022   | ETIHAD REGIONAL (DARWIN) | D74  | SAAB 2000                 | Flying    |
| 07:05     | 07:05    | MADRID           | EZS1415 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 07:05     | 07:10    | ISTANBUL IST [P] | TK1922  | TURKISH AIRLINES         | B33  | AIRBUS  A319              | Flying    |
| 07:05     | 07:14    | BRUSSELS         | SN2726  | BRUSSELS AIRLINES        | A7   | AIRBUS  A319              | Flying    |
| 07:10     | 07:12    | LONDON LCY [P]   | CJ2280  | BRITISH AIRWAYS          | B43  | EMBRAER 190               | Flying    |
| 07:15     | 07:18    | VIENNA           | OS578   | AUSTRIAN                 | D23  | FOKKER 70                 | Flying    |
| 07:15     | 07:20    | CATANIA          | LX2386  | SWISS                    | A5   | AIRBUS  A319              | Flying    |
| 07:15     | 07:39    | AMSTERDAM        | KL1924  | KLM ROYAL DUTCH AIRLINES | A8   | EMBRAER 190               | Flying    |
| 07:20     | 07:25    | PARIS CDG        | AF1243  | AIR FRANCE               | F61  | AIRBUS  A320              | Flying    |
| 07:25     | 07:34    | ZURICH           | LX2805  | SWISS                    | A6   | AVRO RJ100                | Flying    |
| 07:25     | 07:37    | CATANIA          | EZS1561 | EASYJET                  | A1   | AIRBUS  A320              | Flying    |
| 07:30     | 07:38    | LONDON LHR [P]   | BA723   | BRITISH AIRWAYS          | B32  | AIRBUS  A319              | Flying    |
| 07:30     | 07:41    | LONDON LHR [P]   | LX352   | SWISS                    | B44  | AIRBUS  A320              | Flying    |
| 08:00     | 08:11    | NICE             | LX520   | SWISS                    | F64  | BOMBARDIER Q400           | Flying    |
| 08:10     | 08:17    | BRUSSELS         | SN2712  | BRUSSELS AIRLINES        | A3   | AIRBUS  A319              | Flying    |
| 08:15     | 08:23    | MADRID           | IB3489  | IBERIA                   | A4   | AIRBUS  A321              | Flying    |
| 08:20     | 08:52    | VENICE           | F7190   | ETIHAD REGIONAL (DARWIN) | A7   | SAAB 2000                 | Flying    |
| 08:30     | 08:40    | LUGANO           | F7011   | ETIHAD REGIONAL (DARWIN) | A6   | SAAB 2000                 | Flying    |
| 08:40     | 08:54    | MOSCOW DME [P]   | LX1336  | SWISS                    | B34  | AIRBUS  A319              | Flying    |
| 08:45     | 08:56    | AMSTERDAM        | KL1926  | KLM ROYAL DUTCH AIRLINES | A2   | EMBRAER 175               | Flying    |
| 08:50     | 08:53    | BARCELONA        | EZY1403 | EASYJET                  | D23  | AIRBUS  A320              | Flying    |
| 09:00     | 09:11    | KUWAIT [P]       | KU176   | KUWAIT AIRWAYS           | C55  | AIRBUS A330-200           | Flying    |
| 09:00     | 09:14    | HAMBURG          | EW4745  | EUROWINGS                | D25  | BOMBARDIER CRJ-900        | Flying    |
| 09:10     | 09:34    | PARIS CDG        | AF1543  | AIR FRANCE               | F61  | AIRBUS  A319              | Flying    |
| 09:15     | 09:19    | DUSSELDORF       | EW1743  | EUROWINGS                | D27  | BOMBARDIER CRJ-900        | Flying    |
| 09:20     | 09:29    | NEWARK [P]       | UA957   | UNITED AIRLINES          | C51  | BOEING 767-300            | Flying    |
| 09:25     | 09:28    | ROME FCO         | EZY1343 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 09:30     | 09:36    | NICE             | EZY1389 | EASYJET                  | F60  | AIRBUS A320 (SHARKLETS)   | Flying    |
| 09:30     | 09:39    | BRUSSELS         | EZS1533 | EASYJET                  | D75  | AIRBUS  A319              | Flying    |
| 09:30     | 09:40    | FRANKFURT        | LH1213  | LUFTHANSA                | A8   | AIRBUS  A319              | Flying    |
| 09:35     | 10:04    | BARCELONA        | VY6208  | VUELING                  | A9   | AIRBUS A320 (SHARKLETS)   | Flying    |
| 09:40     | 09:42    | LONDON LGW [P]   | EZS8467 | EASYJET                  | C52  | AIRBUS  A320              | Flying    |
| 09:45     | 09:59    | ANTALYA [P]      | XQ129   | SUN EXPRESS              | B32  | BOEING 737-800 (WINGLETS) | Flying    |
| 09:45     | 10:01    | MUNICH           | LX1122  | SWISS                    | A4   | AIRBUS  A319              | Flying    |
| 09:50     | 13:46    | IBIZA            | F7380   | ETIHAD REGIONAL (DARWIN) | A7   | SAAB 2000                 | Flying    |
| 10:00     | 10:10    | ZURICH           | LX2807  | SWISS                    | A5   | AIRBUS  A320              | Flying    |
| 10:10     | 10:15    | LONDON LHR [P]   | BA725   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 10:10     | 10:19    | FIGARI           | EZS1547 | EASYJET                  | F64  | AIRBUS  A320              | Flying    |
| 10:15     | 10:30    | VIENNA           | OS572   | AUSTRIAN                 | A3   | FOKKER 100                | Flying    |
| 10:15     | 10:42    | PORTO            | EZY1451 | EASYJET                  | D23  | AIRBUS A320 (SHARKLETS)   | Flying    |
| 10:20     | 10:26    | WARSAW           | LO418   | LOT POLISH AIRLINES      | A2   | EMBRAER 175               | Flying    |
| 10:20     | 10:45    | LISBON           | EZY1445 | EASYJET                  | D25  | AIRBUS  A319              | Flying    |
| 10:25     | 10:27    | HERAKLION        | LX2350  | SWISS                    | A1   | AIRBUS  A320              | Flying    |
| 10:30     | 10:44    | MANCHESTER [P]   | EZY1950 | EASYJET                  | B44  | AIRBUS  A319              | Flying    |
| 10:30     | 10:48    | PARIS CDG        | AF1643  | AIR FRANCE               | F61  | AIRBUS  A321              | Flying    |
| 10:40     | 10:46    | LONDON LTN [P]   | EZY2052 | EASYJET                  | B43  | AIRBUS  A319              | Flying    |
| 10:45     | 10:50    | PARIS ORY        | EZY1397 | EASYJET                  | F60  | AIRBUS  A320              | Flying    |
| 10:45     | 11:16    | PORTO            | TP939   | TAP PORTUGAL             | D21  | EMBRAER 190               | Flying    |
| 10:55     | 10:54    | HELSINKI         | AY868   | FINNAIR                  | A9   | EMBRAER 190               | Flying    |
| 11:00     | 10:59    | FRANKFURT        | LH1215  | LUFTHANSA                | A8   | BOEING 737-300            | Flying    |
| 11:00     | 11:08    | SPLIT [P]        | EZS1317 | EASYJET                  | B34  | AIRBUS  A320              | Flying    |
| 11:00     | 11:12    | ZURICH           | LX2809  | SWISS                    | A5   | AIRBUS  A320              | Flying    |
| 11:00     | 11:13    | BORDEAUX         | EZS1371 | EASYJET                  | F63  | AIRBUS  A319              | Flying    |
| 11:20     | 11:25    | ATHENS           | A3821   | AEGEAN AIRLINES          | A4   | AIRBUS  A320              | Flying    |
| 11:20     | 11:29    | BRUSSELS         | SN2714  | BRUSSELS AIRLINES        | A3   | AIRBUS  A320              | Flying    |
| 11:20     | 11:30    | BASTIA           | EZS1301 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 11:20     | 11:44    | BILBAO           | EZS1439 | EASYJET                  | D75  | AIRBUS  A319              | Flying    |
| 11:20     | 11:48    | ISTANBUL IST [P] | TK1918  | TURKISH AIRLINES         | B32  | AIRBUS A321 (SHARKLETS)   | Flying    |
| 11:25     | 11:18    | DJERBA [P]       | TU875   | TUNISAIR                 | B42  | AIRBUS  A319              | Flying    |
| 11:30     | 11:55    | AMSTERDAM        | EZS1355 | EASYJET                  | D27  | AIRBUS  A319              | Flying    |
| 11:40     | 11:57    | CALVI            | LX2324  | SWISS                    | F63  | BOMBARDIER Q400           | Flying    |
| 11:45     | 11:51    | BEIRUT [P]       | ME214   | MEA MIDDLE EAST AIRLINES | B33  | AIRBUS  A320              | Flying    |
| 11:45     | 11:59    | WASHINGTON [P]   | UA975   | UNITED AIRLINES          | C51  | BOEING 767-300 (WINGLETS) | Flying    |
| 11:45     | 12:05    | NEW YORK [P]     | LX022   | SWISS                    | C55  | AIRBUS A330-300           | Flying    |
| 11:50     | 12:02    | LONDON LHR [P]   | BA727   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 11:55     | 12:03    | AMSTERDAM        | KL1928  | KLM ROYAL DUTCH AIRLINES | A2   | BOEING 737-700 (WINGLETS) | Flying    |
| 12:00     | 12:10    | PARIS CDG        | AF1843  | AIR FRANCE               | F61  | AIRBUS  A318              | Flying    |
| 12:00     | 14:22    | PALMA MALLORCA   | EZS1513 | EASYJET                  | D27  | AIRBUS  A320              | Flying    |
| 12:10     | 12:21    | PORTO            | LX2078  | SWISS                    | D25  | AIRBUS  A320              | Flying    |
| 12:15     | 12:26    | MADRID           | IB3483  | IBERIA                   | A9   | AIRBUS  A319              | Flying    |
| 12:20     | 12:22    | ROME FCO         | AZ575   | ALITALIA                 | A8   | AIRBUS  A319              | Flying    |
| 12:20     | 12:29    | ATHENS           | LX1822  | SWISS                    | A1   | AIRBUS  A320              | Flying    |
| 12:25     | 12:56    | TENERIFE         | EZS1541 | EASYJET                  | D21  | AIRBUS  A320              | Flying    |
| 12:35     | 12:36    | DUBROVNIK [P]    | EZS1323 | EASYJET                  | B43  | AIRBUS  A319              | Flying    |
| 12:35     | 12:40    | MOSCOW SVO [P]   | SU2381  | AEROFLOT                 | B34  | AIRBUS  A320              | Flying    |
| 12:40     | 12:46    | LISBON           | TP951   | TAP PORTUGAL             | A3   | AIRBUS  A319              | Flying    |
| 12:40     | 12:47    | AMSTERDAM        | EZY1353 | EASYJET                  | D75  | AIRBUS A320 (SHARKLETS)   | Flying    |
| 12:45     | 12:54    | HURGHADA [P]     | EZS1569 | EASYJET                  | B44  | AIRBUS  A320              | Flying    |
| 12:50     | 13:44    | LONDON LHR [P]   | LX354   | SWISS                    | C52  | AVRO RJ100                | Flying    |
| 12:55     | 13:13    | AJACCIO          | LX2320  | SWISS                    | F60  | AIRBUS  A319              | Flying    |
| 13:00     | 13:08    | TUNIS [P]        | TU701   | TUNISAIR                 | B32  | AIRBUS  A320              | Flying    |
| 13:00     | 13:09    | LISBON           | EZS1443 | EASYJET                  | D27  | AIRBUS  A320              | Flying    |
| 13:00     | 13:17    | TORONTO [P]      | AC835   | AIR CANADA               | C56  | BOEING 767-300            | Flying    |
| 13:10     | 13:19    | PARIS CDG        | AF1743  | AIR FRANCE               | F61  | AIRBUS  A319              | Flying    |
| 13:10     | 19:36    | CAGLIARI         | F71162  | ETIHAD REGIONAL (DARWIN) | A6   | SAAB 2000                 | Flying    |
| 13:25     | 13:41    | EDINBURGH [P]    | EZY6906 | EASYJET                  | B43  | AIRBUS  A319              | Flying    |
| 13:30     | 13:42    | MUNICH           | LX1124  | SWISS                    | A9   | AIRBUS  A319              | Flying    |
| 13:30     | 13:53    | OLBIA            | EZS1503 | EASYJET                  | D25  | AIRBUS  A319              | Flying    |
| 13:35     | 13:34    | LONDON LHR [P]   | BA729   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 13:40     | 13:39    | BERLIN SXF       | EZY1591 | EASYJET                  | D23  | AIRBUS  A319              | Flying    |
| 13:40     | 13:49    | BIARRITZ         | A56513  | HOP                      | F64  | BOMBARDIER CRJ-700        | Flying    |
| 13:40     | 14:39    | PALMA MALLORCA   | LX2160  | SWISS                    | A5   | AIRBUS  A320              | Flying    |
| 13:45     | 13:54    | KIEV [P]         | PS486   | UKRAINE INTERNATIONAL    | B33  | EMBRAER 190               | Flying    |
| 14:00     | 14:03    | FRANKFURT        | LH1217  | LUFTHANSA                | A8   | BOEING 737-300            | Flying    |
| 14:00     | 14:17    | REYKJAVIK        | FI565   | ICELANDAIR               | A7   | BOEING 757-200 (WINGLETS) | Flying    |
| 14:05     | 14:16    | REYKJAVIK        | EZS1521 | EASYJET                  | D71  | AIRBUS  A320              | Flying    |
| 14:10     | 14:26    | AMSTERDAM        | KL1930  | KLM ROYAL DUTCH AIRLINES | A3   | EMBRAER 190               | Flying    |
| 14:20     | 14:41    | PRISTINA [P]     | GM6462  | GERMANIA FLUG            | C54  | AIRBUS A321 (SHARKLETS)   | Flying    |
| 14:30     | 14:31    | NAPLES           | EZY1553 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 14:35     | 15:00    | LONDON LGW [P]   | EZS8475 | EASYJET                  | B34  | AIRBUS  A319              | Flying    |
| 14:45     | 14:48    | ZURICH           | LX2811  | SWISS                    | A9   | AIRBUS  A320              | Flying    |
| 14:50     | 15:14    | PARIS CDG        | AF1443  | AIR FRANCE               | F61  | AIRBUS  A320              | Flying    |
| 14:50     | 15:27    | ISTANBUL IST [P] | TK1330  | TURKISH AIRLINES         | B42  | BOEING 737-800 (WINGLETS) | Flying    |
| 14:50     | 15:58    | ISTANBUL SAW [P] | PC338   | PEGASUS                  | B33  | BOEING 737-800 (WINGLETS) | Flying    |
| 14:55     | 14:58    | FRANKFURT        | LH1219  | LUFTHANSA                | A8   | BOEING 737-300            | Flying    |
| 14:55     | 15:10    | NICE             | EZS1383 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 15:00     | 15:17    | CAIRO [P]        | MS772   | EGYPTAIR                 | B32  | BOEING 737-800 (WINGLETS) | Flying    |
| 15:10     | 15:19    | MYKONOS          | EZS1577 | EASYJET                  | A10  | AIRBUS  A319              | Flying    |
| 15:10     | 15:42    | LONDON LHR [P]   | BA731   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 15:15     | 15:22    | DUBAI [P]        | EK090   | EMIRATES                 | C51  | BOEING 777-300ER          | Flying    |
| 15:20     | 15:25    | MANCHESTER [P]   | EZY1952 | EASYJET                  | B43  | AIRBUS  A320              | Flying    |
| 15:25     | 15:36    | MALTA            | KM483   | AIR MALTA                | A4   | AIRBUS  A320              | Flying    |
| 15:25     | 15:41    | BRISTOL [P]      | EZY6154 | EASYJET                  | C52  | AIRBUS  A320              | Flying    |
| 15:30     | 16:00    | RIYADH [P]       | SV238   | SAUDIA                   | C55  | AIRBUS  A320              | Flying    |
| 15:30     | 16:20    | ALGIERS [P]      | AH2047  | AIR ALGERIE              | B44  | BOEING 737-800 (WINGLETS) | Flying    |
| 15:35     | 15:48    | PORTO            | EZY1457 | EASYJET                  | D27  | AIRBUS  A320              | Flying    |
| 15:35     | 16:25    | TOULOUSE         | EZY1473 | EASYJET                  | F64  | AIRBUS  A319              | Flying    |
| 15:40     | 15:50    | AJACCIO          | EZS1307 | EASYJET                  | F63  | AIRBUS  A320              | Flying    |
| 15:40     | 15:54    | LONDON LHR [P]   | LX348   | SWISS                    | C53  | BOMBARDIER Q400           | Flying    |
| 15:45     | 15:56    | ZURICH           | LX2813  | SWISS                    | A2   | AVRO RJ100                | Flying    |
| 15:50     | 16:14    | HERAKLION        | EZS1559 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 15:55     | 17:22    | MARRAKECH [P]    | EZS1313 | EASYJET                  | C54  | AIRBUS  A320              | Flying    |
| 16:00     | 16:10    | MONASTIR [P]     | TU509   | TUNISAIR                 | B32  | AIRBUS  A320              | Flying    |
| 16:00     | 16:16    | JEDDAH [P]       | SV236   | SAUDIA                   | C56  | AIRBUS  A320              | Flying    |
| 16:00     | 16:18    | PARIS ORY        | EZY1399 | EASYJET                  | F61  | AIRBUS A320 (SHARKLETS)   | Flying    |
| 16:00     | 16:22    | LONDON LGW [P]   | EZY8477 | EASYJET                  | B34  | AIRBUS  A319              | Flying    |
| 16:05     | 17:04    | DUBLIN [P]       | EI685   | AER LINGUS               | B31  | AIRBUS  A320              | Flying    |
| 16:35     | 16:51    | FLORENCE         | F7130   | ETIHAD REGIONAL (DARWIN) | A7   | SAAB 2000                 | Flying    |
| 16:45     | 16:53    | ATHENS           | LX1820  | SWISS                    | A10  | AIRBUS  A319              | Flying    |
| 16:45     | 17:12    | LISBON           | EZY1447 | EASYJET                  | D25  | AIRBUS  A319              | Flying    |
| 17:00     | ON TIME  | ZURICH           | F7024   | ETIHAD REGIONAL (DARWIN) |      | SAAB 2000                 | Cancelled |
| 17:05     | 17:15    | MUNICH           | LX1126  | SWISS                    | A8   | AIRBUS  A319              | Flying    |
| 17:20     | 17:25    | AMSTERDAM        | KL1932  | KLM ROYAL DUTCH AIRLINES | A2   | EMBRAER 190               | Flying    |
| 17:20     | 17:31    | AMMAN [P]        | RJ149   | ROYAL JORDANIAN          | B43  | AIRBUS  A319              | Flying    |
| 17:20     | 17:36    | CASABLANCA [P]   | AT931   | ROYAL AIR MAROC          | B33  | BOEING 737-800 (WINGLETS) | Flying    |
| 17:25     | 17:47    | MALAGA           | EZS1435 | EASYJET                  | D23  | AIRBUS  A319              | Flying    |
| 17:35     | 17:40    | PRISTINA [P]     | EZS1483 | EASYJET                  | C51  | AIRBUS  A319              | Flying    |
| 17:35     | 17:43    | LONDON LHR [P]   | BA733   | BRITISH AIRWAYS          | B32  | AIRBUS  A319              | Flying    |
| 17:40     | 17:50    | NICE             | LX528   | SWISS                    | F64  | AIRBUS  A319              | Flying    |
| 17:45     | 17:45    | VENICE           | EZY3326 | EASYJET                  | D21  | AIRBUS  A319              | Flying    |
| 17:45     | 18:34    | LONDON LHR [P]   | LX356   | SWISS                    | B42  | AVRO RJ100                | Flying    |
| 17:50     | 18:00    | CORFU            | LX2352  | SWISS                    | A9   | AIRBUS  A320              | Flying    |
| 17:50     | 18:04    | ZURICH           | LX2817  | SWISS                    | A4   | AVRO RJ100                | Flying    |
| 17:50     | 18:29    | MALTA            | EZS1495 | EASYJET                  | D71  | AIRBUS  A319              | Flying    |
| 17:55     | 17:58    | FRANKFURT        | LH1223  | LUFTHANSA                | A5   | BOEING 737-300            | Flying    |
| 18:00     | 18:11    | PARIS CDG        | AF1343  | AIR FRANCE               | F61  | AIRBUS  A319              | Flying    |
| 18:00     | 18:38    | DOHA [P]         | QR100   | QATAR AIRWAYS            | C53  | BOEING 787-8 DREAMLINER   | Flying    |
| 18:10     | 18:08    | BRINDISI         | EZS1545 | EASYJET                  | A10  | AIRBUS  A319              | Flying    |
| 18:10     | 18:50    | ALGIERS [P]      | LX2206  | SWISS                    | B34  | AIRBUS  A320              | Flying    |
| 18:20     | 19:44    | OLBIA            | LX2370  | SWISS                    | A1   | AIRBUS  A320              | Flying    |
| 18:25     | 18:40    | LISBON           | TP953   | TAP PORTUGAL             | A3   | AIRBUS A320 (SHARKLETS)   | Flying    |
| 18:25     | 18:46    | ANTALYA [P]      | PC5638  | PEGASUS                  | B33  | BOEING 737-800 (WINGLETS) | Flying    |
| 18:30     | 18:54    | ISTANBUL IST [P] | TK1920  | TURKISH AIRLINES         | B44  | AIRBUS A321 (SHARKLETS)   | Flying    |
| 18:30     | 19:08    | MADRID           | IB3493  | IBERIA                   | A4   | AIRBUS A320 (SHARKLETS)   | Flying    |
| 18:45     | 18:53    | LONDON LHR [P]   | BA735   | BRITISH AIRWAYS          | B31  | AIRBUS  A319              | Flying    |
| 18:50     | 19:02    | IBIZA            | EZS1519 | EASYJET                  | D75  | AIRBUS  A320              | Flying    |
| 18:55     | 19:04    | FRANKFURT        | LH1225  | LUFTHANSA                | A1   | BOEING 737-300            | Flying    |
| 19:00     | 18:58    | ROME FCO         | AZ577   | ALITALIA                 | A2   | EMBRAER 175               | Flying    |
| 19:00     | 19:00    | LUGANO           | F7017   | ETIHAD REGIONAL (DARWIN) | D25  | SAAB 2000                 | Flying    |
| 19:05     | 20:02    | PORTO            | TP943   | TAP PORTUGAL             | D23  | EMBRAER 190               | Departed  |
| 19:05     | 20:07    | PALMA MALLORCA   | EZS1515 | EASYJET                  | A10  | AIRBUS  A320              | Flying    |
| 19:10     | 19:13    | BARCELONA        | EZS1409 | EASYJET                  | D21  | AIRBUS  A320              | Flying    |
| 19:10     | 19:15    | RHODOS           | A3485   | AEGEAN AIRLINES          | A8   | AIRBUS  A320              | Flying    |
| 19:15     | 19:19    | LONDON LTN [P]   | EZY2058 | EASYJET                  | B43  | AIRBUS  A320              | Flying    |
| 19:15     | 19:24    | ZURICH           | LX2815  | SWISS                    | A9   | AIRBUS  A319              | Flying    |
| 19:20     | 19:18    | BARCELONA        | LX1946  | SWISS                    | A5   | AIRBUS  A320              | Flying    |
| 19:25     | 19:35    | WARSAW           | LO416   | LOT POLISH AIRLINES      | A3   | EMBRAER 175               | Flying    |
| 19:30     | ON TIME  | AMSTERDAM        | KL1934  | KLM ROYAL DUTCH AIRLINES |      | EMBRAER 190               | Cancelled |
| 19:35     | 19:41    | FRANKFURT        | LH1227  | LUFTHANSA                | D27  | BOMBARDIER CRJ-900        | Flying    |
| 20:10     | 19:58    | VIENNA           | OS576   | AUSTRIAN                 | A2   | FOKKER 100                | Departed  |
| 20:25     | ON TIME  | BEIJING [P]      | CA862   | AIR CHINA                | C53  | AIRBUS A330-200           | Departed  |
| 20:30     | ON TIME  | PARIS CDG        | AF1043  | AIR FRANCE               | F61  | AIRBUS  A320              | Boarding  |
| 20:50     | ON TIME  | ZURICH           | LX2819  | SWISS                    | A9   | AIRBUS  A319              | Scheduled |
| 21:25     | ON TIME  | ABU DHABI [P]    | EY052   | ETIHAD AIRWAYS           | C55  | AIRBUS A330-300           | Scheduled |
| 21:30     | ON TIME  | PORTO            | EZY1459 | EASYJET                  | D21  | AIRBUS  A320              | Scheduled |
| 21:45     | ON TIME  | DUBAI [P]        | EK084   | EMIRATES                 | C51  | BOEING 777-300ER          | Scheduled |
| 21:45     | ON TIME  | LONDON LGW [P]   | EZY8485 | EASYJET                  |      | AIRBUS A320 (SHARKLETS)   | Scheduled |
| 21:50     | ON TIME  | MOSCOW SVO [P]   | SU2383  | AEROFLOT                 | B33  | AIRBUS  A320              | Scheduled |
+-----------+----------+------------------+---------+--------------------------+------+---------------------------+-----------+
```

If a *[P]* appears next to the name of the destination that means that's a
non-Schengen flight.

I have no affiliation with [Geneva International Airport](http://gva.ch) and
the software is provided without guarantee. Enjoy.

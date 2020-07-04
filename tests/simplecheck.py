#!/usr/bin/env python3

import humanify
import datetime

test_date = datetime.datetime(2018, 9, 4, 0, 40, 20)

if not humanify.datetime(test_date) == "Tuesday, 4th of September 2018 00:40:20":
    raise Exception("Unit test gave incorrect results")

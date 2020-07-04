# Documentation for humanify

## Method Reference

### Time Only

method `humanify.time_only( input_datetime )`

*Argument is required and must be of type `datetime.datetime`.*

Returns a string respresenting the time as given by a datetime.

### Date Only

method `humanify.date( input_datetime )`

*Argument is required and must be of type `datetime.datetime`.*

Returns a string respresenting the date as given by a datetime.

### Full Datetime

method `humanify.datetime( input_datetime )`

*Argument is required and must be of type `datetime.datetime`.*

Returns a combination of date and time as given by a datetime.

## Examples

```python
#!/usr/bin/env python3
import humanify
import datetime

current_date = datetime.datetime.now()

print(humanify.time_only(current_date))
print(humanify.date(current_date))
print(humanify.datetime(current_date))
```

# webcal-prune

Very simple Python web service that loads a specified webcal url and returns a subset of the events - those with names matching the keyword.

## Using with pagerduty

1. Identify the webcal url from your pagerduty profile (User icon, My Profile, User Settings) - copy the link from:
![Pagerduty profile](webcal-link.png?raw=true)

2. Identify the unique string to filter to the schedules you want to include

3. Decide if you want to do any further substitution on the event name (e.g. replace On Call with your name)

3. Build your url as follows (or by using the [form](https://webcal.eu-gb.mybluemix.net/) ):

```https://webcal.eu-gb.mybluemix.net/?webcal=*url*&keyword=Primary&find=On+Call&replacement=Ricky```

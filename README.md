# Days_Until

This file calculates the days until a given date. The date given can be in the form of a string. 

# Installation 
``` bash
git clone https://github.com/pesanteur/Days_Until.git
```

# Usage 
```bash
from days_until import days_until

# Given a spelled out month and day
days_until('November 2') 

# Given a month not spelled out
days_until('Nov 2') 

# Given a complete date, this can be used to get days until years in the future
days_until('November 2, 2016')
```

"""
Podcast RSS Parser

Parse a podcast RSS feed and print statistics on the publishing time.

Arguments:
1: String [required] URL of podcast RSS stream

"""
# Author: Derek Jobst
# Email: derekjobst@gmail.com

import sys
import feedparser
import json

from time import mktime
from datetime import datetime
from collections import defaultdict

if __name__ == '__main__':
    d = feedparser.parse(sys.argv[1])

    days = defaultdict(int)

    # Process entries
    print 'Processing {} entires'.format(len(d.entries))
    for entry in d.entries:
        dt = datetime.fromtimestamp(mktime(entry.published_parsed))
        days[dt.__format__('%A')] += 1

    # Print Results
    popular = [(v, k) for k,v in days.iteritems()]
    for n, d in sorted(popular):
        print ' {}: {}'.format(d, n)

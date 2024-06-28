# Quickselect

Pure python implementation of [quick select](https://en.wikipedia.org/wiki/Quickselect) for finding order statistics.  As a special case, contains functions for finding the median of an array.  Allows for the use of a user-defined size function.  Algorithms are in-place and alter the underlying array.  Namely, the desired order statistic is moved so that all entries smaller than it have lower index.  

Indexing conventions:
- The 0-th order statistic is the minimum.
- For the median of an even list, the smaller index median is returned.  

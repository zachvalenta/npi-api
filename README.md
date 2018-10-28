# ENTITY RESOLVER

🗻 __problem (abstract)__

* take some data from JSON 1
* use it to look up some other data from JSON 2
* insert data from JSON 2 into JSON 1

🚠 __problem (germane)__

* take data from data set
* use it to look up NPI number
* add NPI number back into data set

🐠 what I did

* made POC using small subset of data
* refactored after bringing in the full data set (more error handling, rewrite to maintain association between top level key and NPI across NPI lookup failures) 

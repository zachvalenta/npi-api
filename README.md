# ENTITY RESOLVER

📍 __disclaimer__

I've never heard the phrase 'entity resolver' before. 

I searched 'entity resolver' on Youtube and all the results were Counter Strike or Minecraft. 

Here goes nothing 😄

🗻 __problem (abstract)__

* take some data from JSON 1
* use it to look up some other data from JSON 2
* insert data from JSON 2 into JSON 1

🚠 __problem (germane)__

* take data from Mount Sinai
* use it to look up NPI number
* add NPI number back into Mount Sinai dataset

⏰ __what I did__

I'm not super sure that I actually understand the problem, so I built a basic POC against limited scope i.e. 2 obj from Mount Sinai data vs. the full data set (which busted PyCharm 😮)

<figure>
    <img src="json-breaks-pycharm.png">
    <figcaption></figcaption>
</figure>

Like a real project at work, my general approach is:

* get some ink on the page (concreate > abstract)
* ask a few questions before full implementation (safe > sorry)

📮 __feedback plz__

Figured I'd show you guys what I did Wednesday night after work and make sure I was barking up the right tree before writing unit tests 😓

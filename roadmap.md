# General Notes

So far the idea is that each instance of RGS runs seperately. How exactly this will be done is still a question, though Docker might be a good solution. AWS, Heroku, and a custom solution are also posibilities.

I think this project needs a new name.

A landing page/marketing will need to be done at some point, but now is not the time.


# Wireframe notes:

- [x] Switch "Select" from checkbox to some sort of count so you can check out multiple of one item
- [ ]~ Get all buttons working
- [ ]? Design a "modal" system of some sort
- [x] Eventually connect the wireframe to the backend

I understand the wireframe shouldn't work, but I want to try something new. Design the backend first, then redecorate the front end.

## Getting the wireframe working
07/05: ~~I just realized how hard this is going to be to get working. For example, exporting a sample item to jinja is hard. Multiple stores is really the kicker.~~

07/08: ~~OK. So I can import the data into the page, sort/filter via JS (not yet, but I've done it before). The problem is defining "unique" traits. i.e. should two of the same bikes be considered different items or the same? I think different, and sorted with javascript, and clicking each category brings up a checkbox pop-up that can filter by options~~

07/09: Great so I got sorting working all crispy and neat. Unfortunately, I just remembered how complicated names are. I'll have to add some limiter to say "if more than n options, just make it text based" which will also nix the search bar, which is cool

# General TODO
- [x] inventory searching (Allow for multiple options per column)
- [ ]~ inventory sorting
- [ ] implement actual authentication
- [ ] reservation system
- [ ] inventory editing
- [ ] check out/in system
- [ ] configuration
- [ ] export data to barcode
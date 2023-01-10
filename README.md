# AspectsCLI
A CLI interface to the aspects software installation system.

# The concept of "aspects"

I have a cool concept for making AspectOS completely different from the competition.

But first, a question: Have you ever installed an OS that has everything you need without being extremely bloated? Probably not. Most OS' are only targeted to people with very casual computer usage, like browsing the web, reading their email, and maybe making a document or two.

But in my concept, you have a base OS, called Aspect OS base, which doesn't have a de or anything, but has some basic tools like a (cli) text editor,  image editor, etc. But in the install script, you can choose to add an aspect. An aspect is pre-tailored set of packages along with some commands to install them. There will be repos for this. There will be a core repo, which has some general purpose ones like “casual”, “video editing”, “programming” and more. There will also be a community repo, which has more, more edge case, but still useful to more than a handful of people, aspects. And you will be able to import an aspect from a url (e.g you have a custom aspect specifically made for you). These aspects include the DE, which is good, so an entry-level user could choose an aspect with, say GNOME or Cinnamon, while an expert user, could choose an aspect with something like i3.

There will be lots of apps and DE's which have pre-built install scripts in a repo, but you can also make custom versions of these.

You will also be able to make aspects with a python library. An aspect script might look like this:
```
import aspects as asp
asp.desktop("cinnamon") # You can only have one desktop.
asp.image_editor("gimp")
asp.image_editor("krita") # You can have multiple of the same app
# More code...
asp.custom_app("Image Editor", "https://example.org/exampleimaged.py") # You can also reference custom DE's
```
Taken from [a Scratch forum post](https://scratch.mit.edu/discuss/topic/646359/?page=23#post-6883608). 

# Links
The first party aspects: https://github.com/AspectLinux/FirstPartyAspects/

# English

## Kandinsky and ion modules for python for computer !

Just add the two files in the same directory as your script, and that's all !

### Why ?

- In the website of numworks, it's VERY slow, so you can't test graphical programs !
- You can devellop your Numworks program in your computer, with the IDE you want !

### Know problems

- It's still a little slow, because we use .update() to update the screen ! It use a lot of performances :/ We should use .after() but atm I don't know how to do something like that :\
- Turtle and Kandinsky will not be in the same screen :\
- Because it create objects (tkinter works like that), after a moment the script can use a lot of memory (RAM)

### Questions

- #### If my keys are not detected ?
  - Just run get_key_name.py, click on the touch, copy the name, and then open ion.py, find the touch and change the name !
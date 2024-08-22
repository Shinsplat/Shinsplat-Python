# ComfyUI-Shinsplat
ComfyUI Node alterations that I found useful in my own projects and for friends.


Python node to manipulate input/output anything else possible within a work-flow.

If you wanna hang and make words, or you have a bug report, here's where to find me...
https://shinsplat.com/sd/

# :wrench: ComfyUI Convenience Nodes

## Nodes

Python / Python More

	A very simple node that I was unable to find from day one, so I made it.  It's
	just a way to manipulate data incoming and outgoing.  Just type in your python
	in the text box, manipulating any of the inputs and send the result to the
	outputs or not even that, you can perform any local task even file manipulation,
	loading, saving, etc.  The so called-built in variables are the input and output
	names, this is how you access those ports...

	if "dog" in str_in.lower():
		str_out = str_in + " " + "in a park"
	if "man" in str_in.lower():
		str_out = str_in + " " + "making sandwiches"
	if "woman" in str_in.lower():
		str_out = str_in + " " + "operating a jackhammer"

	The "More" alternative has 2 each of the types, so you can use this as a gate
	as well as combine inputs to outputs.


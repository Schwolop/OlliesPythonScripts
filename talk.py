import sys
import subprocess

if __name__ == "__main__":
	print("Type something to make me talk!\r\n")
	done = False
	while not done:
		args = ["say"]
		phrase = input(">> ")
		if phrase == "exit":
			done = True
			phrase = "Thanks for talking with me. Bye bye!"
		elif phrase == "":
			phrase = "you need to type something first!"
		args.append(phrase)
		subprocess.call(args)
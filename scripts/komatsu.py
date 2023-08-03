import pyperclip
import keyboard
import os
	
os.system("cls")
print(f"czDevelopment | czSKUConverter\n")
print("Пресет komatsu загружен\n")

def noralization(sentence):
	sentence = sentence.replace(" ", "")
	start_part = ""
	start_part_two = ""

	last_four = sentence[-5:]
	slen = len(sentence)
	slen = int(slen) - 5

	if "-" in sentence:
		new_str = sentence.replace("-", "")
		two_str = sentence
	else:
		for i in range(0, slen):
			start_part = start_part + sentence[i]

		new_str = start_part+"-"+last_four
		with_tire = new_str

		# print(with_tire)

		two_step = with_tire[-5:]
		tlen = len(two_step)
		tlen = int(tlen) - 2

		for i in range(0, tlen):
			start_part_two = start_part_two + sentence[i]

		two_str = start_part_two+"-"+with_tire[-8:]

	wo_tire = sentence.replace("-", "")
	done_string = f"{two_str} ; {wo_tire}"
	return done_string

def shiza():
	sentence = pyperclip.paste()
	arr = sentence.split("/")

	final_str = ""

	for sku in arr:
		new_sku = noralization(sku)
		print(new_sku)
		final_str = final_str + new_sku + " / "

	print(f"Финальная строка: {final_str[:-3]}\n")
	sentence = pyperclip.copy(final_str[:-3])

keyboard.add_hotkey("shift", shiza)

keyboard.wait()
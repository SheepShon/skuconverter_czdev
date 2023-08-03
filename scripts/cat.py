import pyperclip
import keyboard
import os

os.system("cls")
print(f"czDevelopment | czSKUConverter\n")
print("Пресет caterpiller загружен\n")
	
def noralization(sentence):
	sentence = sentence.replace(" ", "")
	start_part = ""

	last_four = sentence[-4:]
	slen = len(sentence)
	slen = int(slen) - 4

	if "-" in sentence:
		new_str = sentence.replace("-", "")
		with_tire = sentence
	else:
		for i in range(0, slen):
			start_part = start_part + sentence[i]

		new_str = start_part+"-"+last_four
		with_tire = new_str

	wo_tire = sentence.replace("-", "")
	done_string = f"{with_tire} ; {wo_tire}"
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
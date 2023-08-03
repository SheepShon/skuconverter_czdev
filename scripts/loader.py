import os

version = "0.2"

os.system("cls")
print(f"czDevelopment | czSKUConverter | Version {version}\n")

cwd = os.getcwd() + "/scripts"
cwd = cwd.replace('\\', '/')

presets = []

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.py'):
        	if file == "loader.py": pass
        	else: presets.append(file[:-3])

available_presets = ', '.join(presets)

while True:

	print(f"\nДоступные пресеты: {available_presets}")
	preset = input("Введите пресет обработки: ")

	if os.path.exists(f'scripts/{preset}.py'):
		try:
			os.system('start cmd /k python scripts/'+preset+'.py')
			os.abort()
		except OSError:
			print(f'\nПресет "{preset}"" не найден.')
	else:
		print(f'\nПресет "{preset}"" не найден.')
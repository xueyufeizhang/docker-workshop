from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"File in {current_dir}.")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue
    print(f"   - {filepath.name}")

    if filepath.is_file():
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Fail to read file: {e}")
        if content == "":
            print(f"    Content: <ENMPTY>")
        else:
            print(f"    Content: {content}")
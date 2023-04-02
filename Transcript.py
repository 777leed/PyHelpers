# Open the Markdown file
with open("C:\\Users\\hp\\Documents\\Vault\\Inbox\\spanish_trs.md", "r", encoding="utf-8") as f:
    text = f.read()
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != ""]
    text_without_empty_lines = ''.join(non_empty_lines)
    fnl = text_without_empty_lines.translate({ord(i):None for i in '1234567890:'})
    print(fnl)
with open("C:\\Users\\hp\\Documents\\Vault\\Inbox\\spanish_trs.md", "w", encoding="utf-8") as f:
    f.write(fnl)
    
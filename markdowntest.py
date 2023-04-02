

def getwords():
    with open(r'C:\Users\hp\Documents\Vault\Inbox\Weekly Spanish.md', 'r', encoding="utf-8") as f:
        text = f.read()
        text = text.translate({ord(i):None for i in '#123456789'})
        text = text.replace("day", '')
        lines = text.split('\n')
        non_empty_lines = [line for line in lines if line.strip() != ""]
        textdash = ''.join(non_empty_lines)
        lines = textdash.split('-')
        new_values = [lines[i+1] for i in range(len(lines)-1)]
        return new_values
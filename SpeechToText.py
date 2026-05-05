import whisper
import sys
from tkinter import Tk, filedialog
import msvcrt
import time
import torch
import threading
import os
from pathlib import Path

def transcrever_audio(audio):
    
    result = model.transcribe(
        audio,
        language="pt",
        task="transcribe",
        fp16= (device == "cuda")
    )

    print("\nFinalizado!                                                           ")
    return result

def timer(stop_event):
    start = time.time()
    while not stop_event.is_set():
        elapsed = time.time() - start
        print(f"Tempo: {elapsed:.1f}s", end="\r")
        time.sleep(0.1)


base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) #!IMPORTANTE, ESTE BLOCO DEVE VIR ANTES DE QUALQUER COISA
ffmpeg_path = os.path.join(base_path, "ffmpeg.exe")
os.environ["PATH"] = base_path + os.pathsep + os.environ["PATH"]
os.environ["FFMPEG_BINARY"] = ffmpeg_path

root = Tk()
root.withdraw()

device = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("small").to(device) #* tiny/ base / small / medium / large

while True:
    
    audio = filedialog.askopenfilename(title="Selecione o áudio que deseja transcrever")

    ch = '0'

    if not audio:
        print("Nenhum áudio foi selecionado.")
        print("Você deseja: \n1-Procurar um novo áudio; \n2-Encerrar o programa.")
        ch = msvcrt.getwch()

        while ch != '1' and ch != '2':
            print("Opção invalida!")
            print("Você deseja: \n1-Procurar um novo áudio; \n2-Encerrar o programa.")
            ch = msvcrt.getwch()
        
    if ch == '1':
        continue

    elif ch == '2':
        for i in range(3, 0, -1):
            print(f"Encerrando programa em: {i}s                                                        ", end="\r", flush=True)
            time.sleep(1)
        sys.exit()
        
    nomeSemExtensao= Path(audio).stem

    try: #*parte principal
        print("Iniciando Transcrição")
        
        

        stop_event = threading.Event()
        t = threading.Thread(target=timer, args=(stop_event,))
        t.start()

        result = transcrever_audio(audio)
        print()
        print(f"Transcrição do áudio '{nomeSemExtensao}':\n'{result["text"]}'")
        print()
    
    except Exception as e:
        print(f"Erro ao transcrever áudio: {nomeSemExtensao}")
        print("Erro: ", e)

    stop_event.set()
    t.join()

    print("Deseja Transcrever novo áudio? (S/N)")
    ch = msvcrt.getwch()

    while ch.lower() != 's' and ch.lower() != 'n':
        print("Opção invalida!")
        print("Deseja Transcrever novo áudio? (S/N)")
        ch = msvcrt.getwch()

    if ch.lower() == 's':
        continue

    break

print("Eu te amo, minha princesinha S2")
print("mwac mwac mwac")
for i in range(3, 0, -1):
    print(f"Encerrando programa em: {i}s                                                        ", end="\r", flush=True)
    time.sleep(1)

sys.exit()
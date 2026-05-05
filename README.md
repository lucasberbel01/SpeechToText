# 🎙️ Transcritor de Áudio com Whisper

Ferramenta desktop para transcrição de arquivos de áudio em português, utilizando o modelo [Whisper](https://github.com/openai/whisper) da OpenAI. Com interface gráfica para seleção de arquivos e suporte a GPU para processamento acelerado.

---

## ✨ Funcionalidades

- Transcrição automática de áudio para texto em português
- Seleção de arquivo via janela gráfica (sem linha de comando)
- Suporte a GPU (CUDA) para transcrição mais rápida
- Timer em tempo real durante o processamento
- Loop de uso: transcreva múltiplos arquivos sem reiniciar o programa
- Compatível com os formatos suportados pelo FFmpeg (MP3, WAV, MP4, M4A, FLAC, etc.)

---

## 🧰 Requisitos

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/) (incluso como `ffmpeg.exe` na pasta do projeto)
- GPU com suporte a CUDA (opcional, mas recomendado)

### Dependências Python

```bash
pip install openai-whisper torch tkinter
```

> **Nota:** Para uso com GPU, instale o PyTorch com suporte a CUDA. Veja as instruções em [pytorch.org](https://pytorch.org/get-started/locally/).

---

## 📁 Estrutura esperada do projeto

```
projeto/
├── transcritor.py
└── ffmpeg.exe        # Obrigatório: FFmpeg deve estar na mesma pasta do script
```

---

## ▶️ Como usar

1. Certifique-se de que o `ffmpeg.exe` está na mesma pasta do script.
2. Execute o script:

```bash
python transcritor.py
```

3. Uma janela de seleção de arquivo será aberta — escolha o áudio desejado.
4. Aguarde a transcrição. O tempo decorrido será exibido em tempo real.
5. O texto transcrito será exibido no terminal.
6. Ao final, o programa pergunta se deseja transcrever outro arquivo.

---

## ⚙️ Configuração do modelo

O modelo utilizado pode ser alterado diretamente no código. Modelos maiores oferecem mais precisão, porém são mais lentos e exigem mais memória:

```python
model = whisper.load_model("small").to(device)
#                           ↑
#           Opções: tiny | base | small | medium | large
```

| Modelo  | Tamanho | Velocidade | Precisão |
|---------|---------|------------|----------|
| tiny    | ~39 MB  | ⚡⚡⚡⚡⚡   | ⭐⭐      |
| base    | ~74 MB  | ⚡⚡⚡⚡    | ⭐⭐⭐     |
| small   | ~244 MB | ⚡⚡⚡      | ⭐⭐⭐⭐    |
| medium  | ~769 MB | ⚡⚡        | ⭐⭐⭐⭐⭐  |
| large   | ~1.5 GB | ⚡          | ⭐⭐⭐⭐⭐  |

---

## 🖥️ Compatibilidade

> ⚠️ Este script foi desenvolvido para **Windows**, pois utiliza:
> - `msvcrt.getwch()` — leitura de tecla sem Enter (exclusivo do Windows)
> - `ffmpeg.exe` — binário Windows do FFmpeg
> - `tkinter` com `filedialog` — interface gráfica nativa

---

## 📝 Observações

- O idioma de transcrição está fixado em **português (`pt`)**.
- A precisão do modelo `fp16` é ativada automaticamente quando uma GPU CUDA está disponível.
- O script é compatível com executáveis gerados via **PyInstaller** (`sys._MEIPASS`).

---

## 📄 Licença

Projeto pessoal. Livre para uso e modificação.

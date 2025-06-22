# 📂 Organizador de Arquivos

Um organizador automático de arquivos em Python com interface gráfica para seleção de pasta, visualização prévia e opção de desfazer a organização.

---

## 🚀 Funcionalidades

- Seleção interativa da pasta (interface gráfica)
- Visualização prévia do que será movido
- Organização automática por tipo de arquivo (extensão)
- Criação automática das subpastas (imagens, documentos, vídeos, etc)
- Opção de desfazer a última organização

---

## 📷 Prévia

Ao executar o script:

1. O utilizador escolhe uma pasta.
2. O script mostra um resumo dos arquivos e para onde irão.
3. O utilizador pode confirmar ou cancelar.
4. Após organizar, pode desfazer tudo com um clique.

---

## 📦 Categorias suportadas

Os arquivos são organizados em pastas como:

- `imagens/`: `.jpg`, `.png`, `.gif`, ...
- `documentos/`: `.pdf`, `.docx`, `.txt`, ...
- `videos/`: `.mp4`, `.avi`, ...
- `audios/`: `.mp3`, `.wav`, ...
- `compactados/`: `.zip`, `.rar`, ...
- `executáveis/`: `.exe`, `.msi`, ...
- `scripts/`: `.py`, `.js`, `.html`, ...
- `outros/`: tudo o que não se encaixa nas categorias acima

---

## 🛠️ Requisitos

- Python 3.7 ou superior

Bibliotecas usadas (padrão do Python, não precisa instalar):

- `tkinter`
- `os`
- `shutil`
- `pathlib`

---

## ▶️ Como usar

1. Clone este repositório oiu baixe o arquivo `main.py`.
   ```bash
   git clone https://github.com/a14481-oficina/Organizador-de-Arquivos
   
3. Execute com:

```bash
python main.py
```
3. Escolha a pasta a ser organizada.
4. Confirme a organização ou cancele.
5. Se quiser, desfaz a última ação com um clique.

---

## 🧪 Exemplo
Antes:

```bash
Downloads/
├── foto.jpg
├── música.mp3
├── documento.pdf
```
Depois:

```bash
Downloads/
├── imagens/
│   └── foto.jpg
├── audios/
│   └── música.mp3
├── documentos/
│   └── documento.pdf
```

---

## ❌ Desfazer
Após mover os arquivos, o programa armazena os caminhos antigos em memória. Se clicar em "Desfazer", todos os arquivos voltam para onde estavam originalmente.

---

## 📦 Empacotar como .exe (opcional)
Para transformar o script em executável no Windows:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

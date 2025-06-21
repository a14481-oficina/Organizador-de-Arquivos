import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Mapeamento de extensões
EXTENSOES = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documentos": [".pdf", ".docx", ".txt", ".xls", ".xlsx", ".pptx"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audios": [".mp3", ".wav", ".aac", ".ogg"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "executáveis": [".exe", ".msi", ".apk", ".bat", ".sh"],
    "scripts": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
    "outros": []
}

historico_movimentos = {}  # Para desfazer

def categoria_arquivo(extensao):
    for categoria, lista in EXTENSOES.items():
        if extensao in lista:
            return categoria
    return "outros"

def visualizar_preview(pasta):
    preview = []
    for item in os.listdir(pasta):
        caminho_item = Path(pasta) / item
        if caminho_item.is_file():
            ext = caminho_item.suffix.lower()
            categoria = categoria_arquivo(ext)
            preview.append(f"{item}  ->  {categoria}/")
    return preview

def organizar_pasta(pasta):
    count = 0
    historico_movimentos.clear()
    for item in os.listdir(pasta):
        caminho_item = Path(pasta) / item
        if caminho_item.is_file():
            ext = caminho_item.suffix.lower()
            categoria = categoria_arquivo(ext)
            pasta_destino = Path(pasta) / categoria
            pasta_destino.mkdir(exist_ok=True)
            destino = pasta_destino / caminho_item.name
            shutil.move(str(caminho_item), str(destino))
            historico_movimentos[destino] = caminho_item
            count += 1
            print(f"Movido: {item} -> {categoria}/")
    return count

def desfazer_ultima_organizacao():
    if not historico_movimentos:
        messagebox.showinfo("Nada a desfazer", "Nenhuma organização anterior encontrada.")
        return

    for destino, original in historico_movimentos.items():
        if destino.exists():
            shutil.move(str(destino), str(original))
            print(f"Desfeito: {destino.name} <- {original.parent.name}/")
    messagebox.showinfo("Desfeito", "Todos os arquivos foram restaurados ao local original.")
    historico_movimentos.clear()

def escolher_pasta():
    root = tk.Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title="Escolha a pasta a organizar")
    return pasta

if __name__ == "__main__":
    pasta_escolhida = escolher_pasta()
    
    if not pasta_escolhida:
        messagebox.showinfo("Cancelado", "Nenhuma pasta foi selecionada.")
        exit()

    preview = visualizar_preview(pasta_escolhida)
    if not preview:
        messagebox.showinfo("Vazio", "Nenhum arquivo encontrado na pasta.")
        exit()

    texto_preview = "\n".join(preview[:30])
    if len(preview) > 30:
        texto_preview += f"\n...e mais {len(preview) - 30} arquivos."

    confirmacao = messagebox.askyesno("Visualização Prévia", f"Os seguintes arquivos serão movidos:\n\n{texto_preview}\n\nDeseja continuar?")
    if confirmacao:
        total = organizar_pasta(pasta_escolhida)
        messagebox.showinfo("Concluído", f"Organização concluída!\n{total} arquivos foram movidos.")

        desfazer = messagebox.askyesno("Desfazer?", "Deseja desfazer a organização?")
        if desfazer:
            desfazer_ultima_organizacao()
    else:
        messagebox.showinfo("Cancelado", "A organização foi cancelada.")

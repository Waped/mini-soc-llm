from pathlib import Path

def load_knowledge():
    """
    Charge tous les fichiers de knowledge/
    (RAG simple sans embeddings)
    """

    folder = Path("knowledge")

    context = ""

    for file in folder.glob("*.txt"):
        content = file.read_text()
        context += f"\n--- {file.name} ---\n"
        context += content + "\n"

    return context
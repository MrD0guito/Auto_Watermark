# 🖼️ Watermark Adder

Este projeto em Python adiciona automaticamente uma marca d'água (selo) em todas as imagens de uma pasta. Ele redimensiona e posiciona a marca d'água proporcionalmente no canto inferior direito de cada imagem.

## ⚙️ Como usar

1. Instale a biblioteca Pillow:
   ```bash
   pip install pillow
   ```

2. Coloque as imagens que deseja marcar na pasta `watermark_add/`.

3. Coloque a imagem da marca d'água como (`watermark.png`).

4. Execute o script Python.

5. As imagens com a marca serão salvas automaticamente na pasta `output_watermark/`.

## ✨ Funcionalidades

* Suporte a `.jpeg`, `.jpg`, `.png` e `.webp`
* Redimensionamento proporcional da marca
* Posicionamento automático no canto inferior direito
* Margens ajustáveis e proporção da marca configurável

## 🧠 Requisitos

* Python 3.7 ou superior
* Biblioteca Pillow (instalável via `pip`)

## 📌 Exemplo de uso

```python
nova_largura_marca = int(largura * 0.2)  # Ajuste esse valor para mudar o tamanho da marca
```

---

### Feito com 💻 por Gabriel.

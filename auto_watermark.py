from PIL import Image
import os

caminho_original = "watermark_add/"
caminho_destino = "output_watermark/"
marca_dagua = "watermark.png"

def adicionar_marca_dagua(imagem_original, marca_dagua, caminho_destino):
    try:
        imagem = Image.open(imagem_original)
        marca = Image.open(marca_dagua).convert("RGBA")

        largura, altura = imagem.size
        marca_largura, marca_altura = marca.size

        margem_percentual = 0.05  # 5% da largura e altura da imagem

        nova_largura_marca = int(largura * 0.2)  # 20% da largura da imagem
        proporcao = nova_largura_marca / marca_largura
        nova_altura_marca = int(marca_altura * proporcao)
        marca_redimensionada = marca.resize((nova_largura_marca, nova_altura_marca), resample=Image.Resampling.LANCZOS)

        margem_x = int(largura * 0.05)  # margem horizontal 5%
        margem_y = int(altura * 0.05)   # margem vertical 5%
        posicao = (largura - nova_largura_marca - margem_x, altura - nova_altura_marca - margem_y)


        imagem.paste(marca_redimensionada, posicao, marca_redimensionada)
        imagem.save(caminho_destino + os.path.splitext(os.path.basename(imagem_original))[0] + ".png")
        print(f"Marca d'água adicionada em {imagem_original}")

    except Exception as e:
        print(f"Erro ao processar {imagem_original}: {e}")


# Lista de arquivos na pasta original
arquivos = os.listdir(caminho_original)

# Itera sobre os arquivos e adiciona a marca d'água
for arquivo in arquivos:
    if arquivo.endswith(".jpg") or arquivo.endswith(".webp") or arquivo.endswith(".jpeg") or arquivo.endswith(".png"):
        imagem_original = caminho_original + arquivo
        adicionar_marca_dagua(imagem_original, marca_dagua, caminho_destino)

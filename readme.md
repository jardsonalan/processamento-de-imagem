# Processamento Digital de Imagem

Este repositório é destinado ao armazenamento das atividades práticas realizadas durante as aulas de Processamento Digital de Imagem.

## Sumário:
- [Pré-requisitos](#pré-requisitos)
- [Como rodar os scripts](#como-rodar-os-scripts)

## Pré-requisitos:
- **Python:** `>=3.13`

## Como rodar os scripts:
1. Clone o repositório para sua máquina, utilizando o seguinte comando:
   ```bash
   git clone https://github.com/jardsonalan/processamento-de-imagem.git
   ```
   
2. Entre na pasta do projeto, utilizando:
   ```bash
   cd processamento-de-imagem
   ```

3. Para usuários de sistema **Linux**:

   3.1 Crie uma máquina virtual antes de executar os próximos comandos:
   ```bash
   python -m venv venv
   ```

   3.2 Inicialize a máquina virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instale as bibliotecas necessárias, que se encontram em `requirements.txt`, executando o seguinte comando:
   ```bash
   python -m pip install -r requirements.txt
   ```
   
5. Entre em algum dos exemplos das `aula-*/` e adicione uma imagem na pasta `images/`.
   
   5.1 Ao inserir a imagem, acesse o arquivo `lab*.py` correspondente ao exemplo e altere o nome e a extensão da imagem em `img_path`.
   ```py
   img_path = os.path.join(base_dir, 'images', 'adicione-a-imagem-aqui')
   ```

6. Rode o projeto para seu respectivo exemplo, executando:
   ```bash
   python aula-*/lab*.py
   ```
   
   > **Observação:** Os asteriscos (*) servem para demonstração. No lugar deles, adicione a numeração correspondente ao exemplo e ao arquivo que será executado.
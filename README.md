### Sistema de transcrição de videos
Sistema que transcreve videos utilizando python
Feito inicialmente para linux (Futuramente será portado para windows)

## Pré-requisitos
É necessário ter o ffmpeg instalado. 

Utilize sudo apt install ffmpeg

### Como rodar
Instale os requirements.txt que estão na raiz do projeto com pip install -r requirements.txt

Adicione o video que deseja transcrever na pasta videos do projeto e então digite no terminal ```python main.py nome do arquivo```

Ele irá instalar alguns pré requisitos na primeira vez que rodar e logo depois iniciará o processamento.
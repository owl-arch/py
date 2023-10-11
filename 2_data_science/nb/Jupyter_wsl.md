## Jupyter Notebook no subsistema Windows para Linux (WSL)

### Instalação do Python no WSL

Embora o Python venha pré-instalado com a maioria das distribuições Linux, infelizmente não vem com WSL. Então você tem que instalá-lo manualmente:

```bash
apt update && apt upgrade
apt install python3 python3-dev python3-pip
```

Verifique ae versão do python: `python3 --versão`

### Instalando o Jupyter Notebook no WSL

WSL atuará como um servidor Jupyter acessível em localhost com porta 8888.

```bash
pip3 install jupyter
```

Levará algum tempo e instalará todos os pacotes necessários.

## Mudando para navegadores instalados no Windows

Crie um alias para iniciar o Jupyter sem navegador a partir do WSL

- BASH: Abra sua configuração do bash ~/.bashrc e  adicione ao final do arquivo.
```bash
alias jupyter-notebook="~/.local/bin/jupyter-notebook --no-browser"
```

- ZSH: Abra sua configuração do zsh ~/.zshrc e adicione ao final do arquivo.
```bash
alias jupyter-notebook="/usr/local/bin/jupyter-notebook --no-browser"
```

***Importante:*** Para rodar o Jupyter Notebook logado como usuário root adicione `--allow-root` no alias.

### Gerando a configuração Padrão

Crie o arquivo de configuração `~/.jupyter/jupyter_notebook_config.py` default do Jupyter Notebook usando o seguinte comando:

```bash
jupyter notebook --generate-config
```


### Primeiro acesso ao Jupyter Notebook no WSL

Ao acessar pela primeira vez com `localhost:8888`, você verá a tela:

<div style="display: inline_block">
  <img align="right" alt="event-driven.png" style="border-radius: 10%; width: 99%; height:auto;" src="https://github.com/owl-arch/py/blob/main/2_data_science/nb/jupyter.png">
</div>

<br>

A partir do notebook 5.3, na primeira vez que você fizer login usando um token, o servidor deverá lhe dar a oportunidade de configurar uma senha na interface do usuário.

Será apresentado a você um formulário solicitando o token atual , bem como sua nova senha ; insira ambos e clique em `Login and setup new password`.

Da próxima vez que precisar fazer login, você poderá usar a nova senha em vez do token de login; caso contrário, siga o procedimento para definir uma senha na linha de comando.

<br>

#### Referência 
- https://jupyter-notebook.readthedocs.io/en/5.6.0/public_server.html
- https://harshityadav95.medium.com/jupyter-notebook-in-windows-subsystem-for-linux-wsl-8b46fdf0a536


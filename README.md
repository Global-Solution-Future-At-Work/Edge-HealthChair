# Sistema de Monitoramento para controle de Postura

|RM|Nome|
|---|---|
|563995|Azor Biagioni Tartuce|
|566284|Daniel Oliveira de Souza|
|562757|Lucas de Almeida Pires|

Este projeto foi criado para ajudar o usuário a manter uma postura mais saudável enquanto está sentado, especialmente durante atividades de trabalho ou estudo. Posturas inadequadas podem causar dores e reduzir o bem-estar, e o sistema tem como objetivo avisar quando isso estiver acontecendo, promovendo um ambiente de trabalho mais confortável e seguro.
O dispositivo usa um sensor ultrassônico conectado a um ESP32 para medir a distância das costas do usuário até o encosto da cadeira. Assim, ele identifica quando a postura está correta ou quando o usuário está se inclinando demais. As informações são enviadas automaticamente para a nuvem, sem necessidade de equipamentos complexos ou infraestrutura avançada. Uma aplicação para Windows recebe esses dados e avisa o usuário quando é necessário ajustar a postura. 
Dessa forma, o sistema contribui diretamente para condições de trabalho mais saudáveis e alinhadas com a **ODS 8 da ONU**, que incentiva ambientes de trabalho decentes e que cuidem da saúde do trabalhador.

**Link para o Wokwi:** [https://wokwi.com/projects/447606800978932737](https://wokwi.com/projects/447606800978932737) <br>
**Mídias do Projeto:**
*   **Vídeo Demonstrativo (YouTube):** ADICIONAR DEPOIS
*   **Imagem do Circuito/Protótipo:**
  <img src="https://github.com/Global-Solution-Future-At-Work/Edge-HealthChair/blob/main/embarcado/schema_photo.png?raw=true">

---

## 🎯 Objetivo

O objetivo principal deste sistema é **automatizar a abertura de uma escotilha para facilitar a drenagem de água** quando o nível atinge um ponto crítico, ajudando a prevenir ou minimizar os danos causados por enchentes. Adicionalmente, oferece um modo de controle manual para intervenção direta.


## 🛠 Tecnologias e Componentes Utilizados
*   **Aplicação:** Python
*   **Placa Controladora:** ESP32 Dev  DOIT
*   **Sensor de Medição:** 1x Sensor Ultrassônico HC-SR04
*   **Montagem:** Fios de conexão (Jumpers)


## 📦 Funcionalidades

Este sistema embarcado oferece as seguintes funcionalidades:

### 🧍‍♂️📏 Monitoramento Contínuo da Postura do Usuário

-   Utiliza um **sensor ultrassônico acoplado ao ESP32** para medir constantemente a distância entre as costas do usuário e o encosto da cadeira.
    
-   A partir dessas medições, o sistema identifica se o usuário está **mantendo uma postura adequada** ou se está se afastando demais, inclinando-se ou curvando-se.
    
    

### ☁️📡 Envio Inteligente dos Dados para a Nuvem

-   Todas as leituras do sensor são enviadas automaticamente para uma nuvem programável usando o Wi-Fi do ESP32.
    
-   O sistema foi projetado para operar sem necessidade de infraestrutura robusta: **não requer servidores locais**, gateways dedicados ou equipamentos adicionais. Apenas uma criação de uma VM na nuvem é o suficiente para funcionar.
    
-   O armazenamento e processamento dos dados acontecem remotamente, garantindo acesso simples, seguro e em tempo real.
    

### 🖥️💬 Aplicação Windows com Alertas de Postura

-   O usuário conta com uma **aplicação desktop para Windows** que recebe as informações em tempo real diretamente da nuvem.
    
-   Quando o sistema detecta que a postura está inadequada, a aplicação emite um **pop-up**, orientando o usuário a corrigir sua posição.
    
-   Ideal para uso durante trabalho, estudos ou longas sessões sentado, ajudando a criar hábitos posturais mais saudáveis.
    
## 🔌 Conexão Principal (Pinos do ESP32 Dev DOIT)

Para referência rápida, a principal conexão é:
*   **Sensor Ultrassônico:**
    *   `TRIG`: Pino D26
    *   `ECHO`: Pino D25

As conexões de alimentação (3V e GND) podem ser distribuídas pela protoboard ou direto no ESP32, use o `diagram.json` como referência.


## 🪛 Como Instalar

1.  **Criação de Máquina Virtual:**	
* Crie uma **máquina virtual** (no exemplo estamos usando o Azure), com algumas especificações recomendadas, sendo:
	* CPU com **1 Núcleo** ou **+**
	* **1GB** de memória RAM
	* **32GB** de memória OS + **32GB** extra (para banco de dados)
* Veja um exemplo da azure:<br> ![recomendao_maquina.png](https://github.com/Global-Solution-Future-At-Work/Edge-HealthChair/blob/main/python/recomendao_maquina.png?raw=true)

2.  **Configuração de ambiente da VM:**
*   Libere as seguintes portas da máquina virtual:
	* 1026/TCP -  **Orion Context Broker**
	* 1883/TCP -  **Eclipse-Mosquitto MQTT**
	* 4041/TCP -  **IoT-Agent MQTT**
	* 8666/TCP -  **STH-Comet**
* Conecte-se a máquina virtual por SSH e execute o seguinte comando abaixo. Depois, desconecte-se da máquina e feche a entrada por SSH ao final da operação.
```bash
wget  -qO-  https://raw.githubusercontent.com/Global-Solution-Future-At-Work/Edge-HealthChair/refs/heads/main/install_fiware.sh  |  bash
```

3.  **Configurar Fiware (App em nuvem):**
*   Importe o Json Collection do Postman deste repositório.
*   Os dados já estão mockados em cada requisição, logo é importante que siga o passo-a-passo de:
	* Definir a variável global em "GS2-HealthChair", sendo: 
		* Key = "url" 
		* value = "IP_MAQUINA_NUVEM"
	* Executar, em ordem, os seguintes requests:
		* 2. Provisioning a Service Group for MQTT
		* 3. Provisioning a Device
		* 4. Registering Device Commands
* Após isso, a aplicação na nuvem está configurada com sucesso!

4.  **Acessar código do hardware:**
*   Abra o projeto no Wokwi através do link: [https://wokwi.com/projects/432609669649223681](https://wokwi.com/projects/432609669649223681)
	*   Se estiver montando do zero, carregue o arquivo `diagram.json` (para o circuito) e cole o código fornecido no editor do Arduino Uno.
* Na seguintes linhas, altere o BROKER_MQTT para endereço da máquina virtual criada. (Caso esteja testando de forma física, certifique também de mudar o SSID e o password para uma rede de Wi-Fi disponível):
![codigo](https://github.com/Global-Solution-Future-At-Work/Edge-HealthChair/blob/main/embarcado/codigo_arduino_foto.png?raw=true)
* Após isso, execute o projeto e controle o Sensor Ultrassônico da aplicação para a distância desejada (Simuladores do Wokwi permitem até 4 metros = 400cm). Seus dados já estão sendo transmitidos para a nuvem!

5. **Acessar código da aplicação do OS**
* Clone o repositório e acesse a pasta "python". Edite as seguintes variáveis: ![codigo_python](https://github.com/Global-Solution-Future-At-Work/Edge-HealthChair/blob/main/python/codigo_python_linhas.png?raw=true)
* Após isso, volte para a raiz do diretório clonado e execute o arquivo `start_python_app`

Pronto! Todos os passos já estão cumpridos e projeto já pode ser usado.

## 🪑Como usar

1. **Instale o ESP32 de maneira correta**
* E necessário que o dispositivo se mantenha no topo da cadeira para funcionamento correto. Veja o exemplo:
![exemplo_instalação](https://github.com/Global-Solution-Future-At-Work/Edge-HealthChair/blob/main/embarcado/exemplo_instalacao.png?raw=true)
2. **Conecte ele a uma fonte de energia**
* O ESP32 aceita:
	* Pilhas 9 Volts para funcionamento sem cabos
	* Conexão direta com fonte de celular

---

WorkQueue - 2025
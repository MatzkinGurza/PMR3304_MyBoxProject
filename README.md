# Proposta de Sistema: Plataforma de E-Commerce por Subscrição

_Grupo F:<br>
Mateus Matzkin Gurza 6010281<br>
Gustavo Loiola dos Santos 13681784<br>
Vinicius Barile Lora Franco 13679930<br>
Luís Eduardo Dorneles Fauth 13679436_<br>

## Visão Geral do Sistema

O projeto consiste na elaboração de uma plataforma de e-commerce voltada para a compra e venda de produtos por meio de um sistema de subscrição. A plataforma será dedicada a conectar compradores e vendedores, permitindo que os consumidores adquiram pacotes periódicos de produtos de lojas específicas.<br>
	Assim, este projeto visa criar uma plataforma de e-commerce inovadora que combina a conveniência das compras online com um sistema de subscrição. Ao focar em uma experiência de usuário simplificada e em uma gestão eficiente de subscrições, a plataforma oferece aos consumidores uma nova forma de adquirir produtos de suas lojas preferidas de maneira contínua e personalizada. A atenção à segurança, desempenho, e usabilidade garantirá que a plataforma seja confiável e atraente para todos os usuários.

**Nome adotado para a plataforma:** MyBox <br>
**Figma Link:** https://www.figma.com/proto/K7wcsNdh4D18uQggwRcw3F/MyBox?node-id=0-1&t=erScI8Fkic8k3lhP-1
	
## Atores do Sistema

### 1. Perfil Comprador:
   - Pode navegar pelas lojas disponíveis e selecionar pacotes de subscrição.
   - Gerencia suas subscrições ativas, acompanhando os produtos que irá receber e o valor mensal gasto.
   - Acesso a um carrinho de compras para adicionar ou remover pacotes antes de finalizar a subscrição.
   - Possibilidade de visualizar e editar informações de pagamento e endereço de entrega.
   - Pode enviar feedbacks ao vendedor


### 2. Perfil Vendedor:
   - Cria, gerencia e atualiza pacotes de subscrição, definindo os produtos e preços oferecidos mensalmente.
   - Acompanha as vendas e o status das subscrições dos clientes.
   - Pode visualizar feedbacks dos clientes.

## Requisitos Funcionais

### 1. Carrinho de Compras:
   - O comprador pode adicionar pacotes de subscrição ao carrinho.
   - O comprador pode revisar, editar ou remover itens do carrinho antes de finalizar a compra.
   - O sistema deve calcular automaticamente o valor total da subscrição com base nos pacotes selecionados.

### 2. Gestão de Subscrições:
   - O comprador pode visualizar todas as suas subscrições ativas, com detalhes sobre produtos incluídos, valor mensal e data de renovação.
   - O sistema permite pausar ou cancelar subscrições conforme necessário.

### 3. Pagamentos:
   - O sistema deve processar os pagamentos conectando-se diretamente à forma de pagamento do cliente.
   - O sistema realiza cobranças mensais automáticas com base nas subscrições ativas.

### 4. Gerenciamento de Pacotes:
   - Os vendedores podem criar e gerenciar pacotes de subscrição, definindo os produtos, quantidade e preço em sua descrição.
   - Os vendedores podem visualizar o histórico de vendas e o desempenho de seus pacotes.

### 5. Sistema de cadastro:
   - Sistema de cadastro de lojas como vendedores e clientes como compradores
   - autenticação de perfil para uso da plataforma

## Requisitos Não-Funcionais

### 1. Segurança:
   - Sistema deve ser seguro e garantir que não seja possível roubar informações de outros usuários ou se passar por eles
   - Deve proteger informações de pagamento e dados pessoais dos usuários.
  
### 2. Desempenho:
   - O sistema deve ser capaz de processar múltiplas transações e usuários simultâneos.

### 3. Usabilidade:
   - Interface amigável e intuitiva, com navegação fácil entre diferentes seções da plataforma.
   - Disponibilidade de suporte ao cliente, por exemplo, FAQ.

### 4. Escalabilidade:
   - A arquitetura do sistema deve suportar o crescimento da base de usuários e do volume de transações.
   - Facilidade de integração com novos métodos de pagamento e outros serviços terceirizados.
---

## Casos de uso
A seguir será abordada a questão dos casos de uso do sistema, indicando o fluxo de informações entre telas presentes nele. Note que múltiplos fluxos de navegação serão possíveis.<br>

**Sequência inicial de fluxo de dados e telas:**

- _Telas:_ [1] tela comum de entrada (inicial MyBox) sem usuário logado -> [2] tela de entrada de usuário -> [2.a] tela para login ou [2.b] tela para cadastro -> [3] tela inicial MyBox com usuário logado
	- Opções de sequência:
		- _Pesquisa de Loja_ -> [3.1.a] tela de loja -> [3.2.a] tela de produto (box) -> [3.3.a] tela de confirmação de compra
		- _Pesquisa de produto_ -> [3.1.b] produto aparece na página principal MyBox
		- _Carrinho de compras_ -> [3.1.c] tela de carrinho de compras/subscrições e gerenciamento de subscrições -> [3.2.c] tela de cadastro ou alterações de informações de pagamento e informações de usuário
		-_Exclusivo para **Vendedor**_ -> [3.1.d] página de edição e adição de pacotes e configuração da página da loja
 
- _Fluxo de dados_:
	- Dados Pessoais [obtidos em 2.b ou checados em 2.a] vão da interface para o banco de dados -> tabela "Dados Pessoais":
		- Usuário
		- Agente (tipo de agente, comprador ou vendedor)   
		- Nome
		- Sobrenome
		- E-mail
		- Telefone
		- CPF
		- Idade
		- Gênero
		- Endereço
		- Complemento
		- CEP
	- Subscrições [obtidas em 3.3.a ao confirma-se a compra] dados obtidos são encaminhados para um banco que guarda as subscrições atuais -> tabela "Subscrições":
		- ID de compra
		- ID de pacote
		- Usuário
		- Tempo (tempo de subscrição)
 		- Data de compra
     		- Data de fim
		- Status (subscrição, ativa ou inativa)
	- Dados de pacote [fornecidos a 3.2.a com informações provindas do input ou alteração em 3.1.d] dados obtidos são enviados para uma tabela com as informações relevantes do pacote -> tabela "Dados de pacote":
		- ID de pacote
		- Descrição
		- Preço 
		- Usuário_vendedor    
	- Dados sensíveis [Utilizados em 3.1.c e obtidos em 3.2.c] dados sensíveis protegidos -> tabela "Dados sensíveis":
		- Usuário
		- Senha
		- Forma de pagamento
		- Titular do cartão
		- Número do cartão
		- Pin do cartão       

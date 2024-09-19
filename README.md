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

| **Tabela**         | **Dado Armazenado**     | **Casos de Uso (Dado Obtido)** | **Casos de Uso (Dado Utilizado)** |
|--------------------|-------------------------|--------------------------------|----------------------------------|
| Usuário            | Nome                    | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | Sobrenome                | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | E-mail Usuário           | 1 (Cadastro de Usuário)        | 2 (Login no Sistema), 3 (Recuperação de Senha), 4 (Atualização de Perfil), 20 (Notificações de Subscrição) |
| Usuário            | Telefone                | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | CPF                      | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | Data de nascimento       | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | Sexo                     | 1 (Cadastro de Usuário)        | 4 (Atualização de Perfil de Usuário) |
| Usuário            | Endereço                 | 1 (Cadastro de Usuário)        | 12 (Gerenciar Informações de Pagamento e Endereço) |
| Usuário            | Complemento              | 1 (Cadastro de Usuário)        | 12 (Gerenciar Informações de Pagamento e Endereço) |
| Usuário            | CEP                      | 1 (Cadastro de Usuário)        | 12 (Gerenciar Informações de Pagamento e Endereço) |
| Usuário            | Senha                    | 1 (Cadastro de Usuário)        | 2 (Login no Sistema), 3 (Recuperação de Senha), 4 (Atualização de Perfil de Usuário) |
| Agente             | Tipo de Agente (comprador/vendedor) | 1 (Cadastro de Usuário)  | 2 (Login no Sistema), 13 (Criar e Gerenciar Pacotes), 5 (Navegar em Lojas e Produtos) |
| Loja               | Nome Loja                | 1 (Cadastro de Usuário, se vendedor) | 19 (Gerenciar Configurações da Loja) |
| Loja               | E-mail Loja              | 1 (Cadastro de Usuário, se vendedor) | 14 (Acompanhar Vendas e Subscrições), 19 (Gerenciar Configurações da Loja) |
| Loja               | CNPJ                     | 1 (Cadastro de Usuário, se vendedor) | 4 (Atualização de Perfil) |
| Loja               | Imagem_logo              | 19 (Gerenciar Configurações da Loja) | 19 (Gerenciar Configurações da Loja) |
| Loja               | Imagem de plano de fundo | 19 (Gerenciar Configurações da Loja) | 19 (Gerenciar Configurações da Loja) |
| Pacote             | ID de Pacote             | 7 (Adicionar Pacote ao Carrinho) | 9 (Finalizar Compra), 14 (Acompanhar Vendas e Subscrições) |
| Pacote             | Descrição do pacote      | 13 (Criar e Gerenciar Pacotes)  | 5 (Navegar em Lojas e Produtos), 9 (Finalizar Compra) |
| Pacote             | Preço do pacote          | 13 (Criar e Gerenciar Pacotes)  | 7 (Adicionar Pacote ao Carrinho), 9 (Finalizar Compra) |
| Pacote             | Imagem do pacote         | 13 (Criar e Gerenciar Pacotes)  | 5 (Navegar em Lojas e Produtos) |
| Subscrição         | ID de compra             | 9 (Finalizar Compra)            | 11 (Visualizar Histórico de Compras), 14 (Acompanhar Vendas e Subscrições) |
| Subscrição         | Tempo (duração)          | 7 (Adicionar Pacote ao Carrinho) | 9 (Finalizar Compra), 14 (Acompanhar Vendas e Subscrições) |
| Subscrição         | Data de compra           | 9 (Finalizar Compra)            | 11 (Visualizar Histórico de Compras), 14 (Acompanhar Vendas e Subscrições) |
| Subscrição         | Data de fim              | 7 (Adicionar Pacote ao Carrinho) | 14 (Acompanhar Vendas e Subscrições), 20 (Notificações de Subscrição) |
| Subscrição         | Status                   | 14 (Acompanhar Vendas e Subscrições) | 10 (Gerenciar Subscrições) |
| Pagamento          | Forma de pagamento       | 9 (Finalizar Compra)            | 12 (Gerenciar Informações de Pagamento), 18 (Processar Pagamento de Subscrição) |
| Pagamento          | Titular do cartão        | 9 (Finalizar Compra)            | 12 (Gerenciar Informações de Pagamento) |
| Pagamento          | Número do cartão         | 9 (Finalizar Compra)            | 12 (Gerenciar Informações de Pagamento) |
| Pagamento          | Pin do cartão            | 9 (Finalizar Compra)            | 12 (Gerenciar Informações de Pagamento) |

Tabela 1: Mapeamento de dados coletados e utilizados nos casos de uso do e-commerce por subscrição.

| **Tabela**   | **Dados Presentes**                                                                                      | **Key**            |
|--------------|----------------------------------------------------------------------------------------------------------|--------------------|
| Usuário      | Nome, Sobrenome, E-mail, Telefone, CPF, Data de nascimento, Sexo, Endereço, Complemento, CEP, Senha        | ID_Usuário         |
| Agente       | Tipo de Agente (comprador/vendedor), ID_Usuário                                                           | ID_Agente          |
| Loja         | Nome da loja, E-mail, CNPJ, Imagem_logo, Imagem de plano de fundo                                         | ID_Loja            |
| Pacote       | ID_Pacote, Descrição do Pacote, Preço, Imagem                                                             | ID_Pacote          |
| Subscrição   | ID_Compra, Tempo (duração), Data de compra, Data de fim, Status, ID_Pacote, ID_Usuário                    | ID_Compra          |
| Pagamento    | Forma de pagamento, Titular do cartão, Número do cartão, Pin do cartão, ID_Compra, ID_Usuário             | ID_Pagamento       |

Tabela 2: Estrutura das tabelas, com dados presentes e chaves primárias para relacionamentos.

# Proposta de Sistema: Plataforma de E-Commerce por Subscrição

_Grupo F:
Mateus Matzkin Gurza 6010281<br>
Gustavo Loiola dos Santos 13681784<br>
Vinicius Barile Lora Franco 13679930<br>
Luís Eduardo Dorneles Fauth 13679436_<br>

## Visão Geral do Sistema

O projeto consiste na elaboração de uma plataforma de e-commerce voltada para a compra e venda de produtos por meio de um sistema de subscrição. A plataforma será dedicada a conectar compradores e vendedores, permitindo que os consumidores adquiram pacotes periódicos de produtos de lojas específicas.<br>
	Assim, este projeto visa criar uma plataforma de e-commerce inovadora que combina a conveniência das compras online com um sistema de subscrição. Ao focar em uma experiência de usuário simplificada e em uma gestão eficiente de subscrições, a plataforma oferece aos consumidores uma nova forma de adquirir produtos de suas lojas preferidas de maneira contínua e personalizada. A atenção à segurança, desempenho, e usabilidade garantirá que a plataforma seja confiável e atraente para todos os usuários.

**Nome adotado para a plataforma:** MyBox
	
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


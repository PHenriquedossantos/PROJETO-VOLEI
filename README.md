API de Agenda
Este é um projeto de API em Python usando o Django Rest Framework para armazenar informações de horários para agendar quadras de vôlei em uma arena.

As bibliotecas utilizadas são:

asgiref==3.6.0
Django==4.1.7
djangorestframework==3.14.0
Markdown==3.4.1
pytz==2022.7.1
sqlparse==0.4.3
tzdata==2022.7
A API possui as seguintes rotas:

GET /company/ - retorna todas as empresas cadastradas
POST /company/ - cria uma nova empresa
GET /company/:id - retorna uma empresa específica
PUT /company/:id - atualiza uma empresa específica
DELETE /company/:id - deleta uma empresa específica
GET /customer/ - retorna todos os clientes cadastrados
POST /customer/ - cria um novo cliente
GET /customer/:id - retorna um cliente específico
PUT /customer/:id - atualiza um cliente específico
DELETE /customer/:id - deleta um cliente específico
GET /place/ - retorna todas as quadras/campos disponíveis
POST /place/ - cria uma nova quadra/campo
GET /place/:id - retorna uma quadra/campo específica
PUT /place/:id - atualiza uma quadra/campo específica
DELETE /place/:id - deleta uma quadra/campo específica
GET /payment/ - retorna todos os tipos de pagamento cadastrados
POST /payment/ - cria um novo tipo de pagamento
GET /payment/:id - retorna um tipo de pagamento específico
PUT /payment/:id - atualiza um tipo de pagamento específico
DELETE /payment/:id - deleta um tipo de pagamento específico
GET /scheduling/ - retorna todos os horários agendados
POST /scheduling/ - cria um novo agendamento
GET /scheduling/:id - retorna um agendamento específico
PUT /scheduling/:id - atualiza um agendamento específico
DELETE /scheduling/:id - deleta um agendamento específico
GET /customer/:id/horarios - retorna todos os horários agendados por um cliente específico
Para cada recurso, a API suporta as operações CRUD (Create, Read, Update e Delete). Além disso, há uma rota para listar os horários agendados por um cliente específico.

As models utilizadas são:

Company: representa o local onde estão as quadras/campos
Customer: representa os clientes que agendam horários
Place: representa cada quadra/campo disponível em cada local
Payment: representa as formas de pagamento aceitas para cada agendamento
Scheduling: representa cada agendamento de horário para uma quadra/campo específica por um cliente específico.
Os serializers utilizados são:

CompanySerializer: serializa/desserializa objetos Company
CustomerSerializer: serializa/desserializa objetos Customer
PlaceSerializer: serializa/desserializa objetos Place
PaymentSerializer: serializa/ desserializa objetos Payment
SchedulingSerializer: serializa/desserializa objetos Scheduling
HorariosClientesSerializer: serializa/desserializa



Para executar a API, siga os seguintes passos:

Instale as bibliotecas necessárias:

Copy code
	pip install -r requirements.txt
Execute as migrações do banco de dados:


	python manage.py migrate
Inicie o servidor:

	python manage.py runserver


Informações adicionais:

Versão da API: 1.0.0
Autor: [Henrique Santos]
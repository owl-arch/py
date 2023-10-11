##
# Inspiração: https://www.linkedin.com/feed/update/urn:li:activity:7100045742077005826/?utm_source=share&utm_medium=member_android
##


[1.] Use descriptive and meaningful resource naming -
/users, /products, /orders

[2.] Follow the principles of the HTTP methods -
GET /users, POST /products, PUT /users/{id}, DELETE /orders/{id}

[3.] Utilize HTTP status codes correctly -
200 OK, 201 Created, 400 Bad Request, 404 Not Found etc.

[4.] Provide comprehensive and clear documentation for your API -
Detailed API documentation with usage examples, parameter descriptions, and response formats.

[5.] Use versioning to manage API changes -
/v1/users, /v2/products

[6.] Design your API to be stateless -
Authenticate each request with an access token rather than relying on server-side sessions.

[7.] Implement proper error handling -
{ "error": "Invalid request body" } with an appropriate HTTP status code.

[8.] Use appropriate authentication and authorization mechanisms -
Implement OAuth 2.0 or JWT-based authentication and define roles/permissions for authorized users.

[9.] Implement rate limiting and throttling -
E.g. Allow a maximum of 100 requests per hour for a particular API endpoint per client.

[10.] Utilize caching mechanisms -
Set appropriate Cache-Control and ETag headers for responses that can be cached.

[11.] Follow the principles of HATEOAS -
Include hyperlinks and resource links in API responses for easy traversal and discovery.

[12.] Use pagination techniques -
Implement pagination with query parameters like page and limit to retrieve subsets of data.

[13.] Implement input validation -
Validate request payloads for required fields, data types, and data format.

[14.] Design your API to be idempotent -
Ensure that multiple identical requests have the same effect as a single request.

[15.] Use appropriate content types -
Set Content-Type: application/json for JSON payloads or Content-Type: application/xml for XML payloads.

[16.] Support content negotiation -
Accept and return multiple representation formats based on the Accept header.

[17.] Consider implementing request/response compression -
Compress response payload using gzip encoding when the client supports it.

[18.] Provide filtering, sorting, and searching capabilities -
Allow clients to filter results based on query parameters like filter, sort, or search.

[19.] Implement proper version control for API documentation -
Maintain a separate versioned documentation for each API version.

[20.] Support graceful handling of deprecated API endpoints or features -
Clearly communicate deprecation, provide migration guides, and offer alternative endpoints.

[21.] Implement proper logging and monitoring -
Log API requests, errors, and performance metrics. Set up monitoring tools for proactive detection of issues.

[22.] Follow RESTful URI conventions -
Use hierarchical URIs like /users/{id}/orders to represent resource relationships.

TRADUÇÃO
[1.] Usar nomenclatura de recursos descritiva e significativa - /usuários, /produtos, /pedidos [2.] Siga os princípios dos métodos HTTP - GET /users, POST /products, PUT /users/{id}, DELETE /orders/{id} [3.] Utilize códigos de status HTTP corretamente - 200 OK, 201 Criado, 400 Solicitação Incorreta, 404 Não Encontrado etc. [4.] Fornecer documentação abrangente e clara para sua API - Documentação detalhada da API com exemplos de uso, descrições de parâmetros e formatos de resposta. [5.] Usar o controle de versão para gerenciar alterações na API - /v1/usuários, /v2/produtos [6.] Projete sua API para ser sem monitoração de estado - Autentique cada solicitação com um token de acesso em vez de depender de sessões do lado do servidor. [7.] Implementar o tratamento adequado de erros - { "error": "Corpo de solicitação inválido" } com um código de status HTTP apropriado. [8.] Usar mecanismos apropriados de autenticação e autorização - Implemente a autenticação baseada em OAuth 2.0 ou JWT e defina funções/permissões para usuários autorizados. [9.] Implementar limitação e limitação de taxa - Por exemplo, permitir um máximo de 100 solicitações por hora para um determinado ponto de extremidade de API por cliente. [10.] Utilizar mecanismos de cache - Defina os cabeçalhos Cache-Control e ETag apropriados para respostas que podem ser armazenadas em cache. [11.] Siga os princípios da HATEOAS - Inclua hiperlinks e links de recursos nas respostas da API para facilitar a travessia e a descoberta. [12.] Use técnicas de paginação - Implemente a paginação com parâmetros de consulta como página e limite para recuperar subconjuntos de dados. [13.] Implementar validação de entrada - Valide cargas úteis de solicitação para campos obrigatórios, tipos de dados e formato de dados. [14.] Projete sua API para ser idempotente - Certifique-se de que várias solicitações idênticas tenham o mesmo efeito que uma única solicitação. [15.] Usar tipos de conteúdo apropriados - Defina Content-Type: application/json para cargas JSON ou Content-Type: application/xml para cargas XML. [16.] Suporte à negociação de conteúdo - Aceite e retorne vários formatos de representação com base no cabeçalho Accept. [17.] Considere implementar a compactação de solicitação/resposta - Comprima a carga útil de resposta usando a codificação gzip quando o cliente a suportar. [18.] Fornecer recursos de filtragem, classificação e pesquisa - Permitir que os clientes filtrem resultados com base em parâmetros de consulta, como filtro, classificação ou pesquisa. [19.] Implementar controle de versão adequado para documentação da API - Mantenha uma documentação com versão separada para cada versão da API. [20.] Suporte ao tratamento normal de pontos de extremidade ou recursos de API preteridos - Comunique claramente a depreciação, forneça guias de migração e ofereça pontos de extremidade alternativos. [21.] Implementar registro e monitoramento adequados - Registre solicitações de API, erros e métricas de desempenho. Configure ferramentas de monitoramento para detecção proativa de problemas. [22.] Siga as convenções de URI RESTful - Use URIs hierárquicos como /users/{id}/orders para representar relacionamentos de recursos. 


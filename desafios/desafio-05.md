# Desafio 05 - Executando Tarefas Automatizadas com Lambda Function e S3

## Como automatizar a configuração do S3 Object Lambda com um modelo do CloudFormation

O modelo provisiona os recursos necessários, configura permissões via IAM e implanta uma função AWS Lambda que intercepta e processa solicitações feitas ao S3. Por padrão, a função Lambda retorna os objetos sem alterações, mas pode ser personalizada para aplicar transformações nos dados antes de enviá-los à aplicação cliente.

É possível configurar parâmetros adicionais durante a implantação, ativar o monitoramento com Amazon CloudWatch, definir cargas úteis para a função Lambda e habilitar a simultaneidade provisionada para reduzir latência. Além disso, é possível também modificar cabeçalhos HTTP, retornar códigos de status personalizados e aplicar filtros como intervalos de bytes (Range) e partes de objetos (partNumber), otimizando o desempenho e o uso de memória.

A função Lambda pode ser ajustada para transmitir dados enquanto os transforma, o que é útil para objetos grandes. O modelo também permite desabilitar recursos como suporte a Range e partNumber, caso não sejam necessários. Por fim, o guia oferece exemplos de código e boas práticas para adaptar a função Lambda às necessidades específicas de transformação de dados em tempo real.

--- 
### Referências
[Automatizar a configuração do S3 Object Lambda com um modelo do CloudFormation](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/olap-using-cfn-template.html)
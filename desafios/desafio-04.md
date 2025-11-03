# Desafio 04 - Implementando Infraestrutura Automatizada com AWS CloudFormation

## Automatizando com AWS CloudFormation - Tutorial

O tutorial apresenta um processo automatizado para iniciar um pipeline de previsão com o Amazon Forecast, utilizando um modelo pré-configurado do CloudFormation chamado Improving Forecast Accuracy with Machine Learning Solution. Esse modelo implanta automaticamente os conjuntos de dados de táxis de NYC em um bucket do Amazon S3, inicia o pipeline de previsão e preenche os campos necessários no console com os caminhos corretos dos dados.

Após seguir o tutorial com os dados de demonstração, o usuário pode reutilizar a mesma pilha para gerar previsões com seus próprios conjuntos de dados. Para isso, basta substituir os caminhos dos arquivos no S3 durante a configuração. O processo de implantação envolve etapas simples, como aceitar padrões, fornecer um e-mail para notificações e habilitar permissões para criação de recursos IAM e pilhas aninhadas.

Ao final, o tutorial orienta como limpar os recursos criados e oferece opções para personalizar a implantação com dados próprios ou explorar outras abordagens automatizadas. Mesmo com a descontinuação para novos usuários, o conteúdo continua útil para quem já utiliza o Amazon Forecast e deseja integrar previsões em seus fluxos de trabalho com praticidade e escalabilidade.

---
### Referências
[Tutorial CloudFormation](https://docs.aws.amazon.com/pt_br/forecast/latest/dg/tutorial-cloudformation.html)

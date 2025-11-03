# Desafio 02 - Explorando Workflows Automatizados com AWS Step Functions

## AWS Step Functions
  
O AWS Step Functions é um serviço serverless que permite criar e gerenciar fluxos de trabalho complexos de forma visual e altamente escalável. Ele funciona como uma máquina de estados, onde cada etapa do processo é definida com precisão, facilitando a construção de aplicações distribuídas e resilientes. Com uma interface intuitiva, os desenvolvedores podem visualizar e validar a lógica dos seus workflows, além de integrar facilmente mais de 220 serviços da AWS, como Lambda, DynamoDB, SQS, SNS e muitos outros.

Entre os principais recursos, o Step Functions oferece tratamento automático de erros, tentativas de reexecução, controle de tempo de execução e suporte a execuções paralelas. Isso garante maior confiabilidade e flexibilidade na automação de processos. Além disso, é possível transformar dados diretamente dentro do fluxo usando expressões JSONata, o que reduz a necessidade de código adicional.

### Principais destaques

O serviço também se destaca por sua capacidade de escalar com eficiência, especialmente com os chamados Express Workflows, que suportam milhares de execuções por segundo — ideal para aplicações como ingestão de dados em tempo real ou processamento de eventos IoT. Outro ponto forte é a separação clara entre a lógica de negócio e a implementação técnica, permitindo que equipes mantenham e evoluam seus sistemas com mais agilidade.

Para monitoramento e auditoria, o Step Functions se integra ao CloudWatch e ao CloudTrail, oferecendo visibilidade completa sobre cada execução, entradas, saídas e falhas. Ele opera com alta disponibilidade, distribuído entre múltiplas zonas de disponibilidade, e atende a padrões rigorosos de segurança e conformidade, como HIPAA e SOC. O modelo de cobrança é baseado em transições de estado, o que torna o custo proporcional ao uso real, sem tarifas por tempo ocioso.

--- 
### Referências
[Step Functions](https://aws.amazon.com/pt/step-functions/features/?pg=ln&sec=hs)

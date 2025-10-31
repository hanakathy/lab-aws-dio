# Implementando sua Primeira Stack com AWS CloudFormation

O AWS CloudFormation é uma ferramenta poderosa que permite criar e gerenciar recursos da AWS de forma automatizada e segura, utilizando modelos escritos em YAML ou JSON.

Ao utilizar o CloudFormation, você descreve os recursos desejados — como instâncias EC2, bancos de dados RDS, balanceadores de carga e muito mais — em um modelo que funciona como um roteiro para a infraestrutura. Esses modelos podem ser reaproveitados em diferentes contextos, graças à possibilidade de incluir parâmetros de entrada que tornam a configuração flexível e adaptável. Quando você envia esse modelo para o CloudFormation, ele cria uma “pilha”, que é um conjunto de recursos gerenciados como uma única unidade. Isso significa que você pode criar, atualizar ou excluir toda a infraestrutura apenas manipulando a pilha correspondente.

Durante o processo de criação, o CloudFormation realiza chamadas aos serviços da AWS para provisionar os recursos conforme especificado. Caso algo falhe, ele reverte automaticamente as alterações, garantindo que o ambiente não fique em estado inconsistente. Para atualizações, você pode modificar o modelo original ou os parâmetros e gerar um “conjunto de alterações”, que mostra exatamente o que será alterado antes de aplicar qualquer modificação. Isso é essencial para evitar impactos inesperados, como a substituição de recursos críticos sem planejamento.

Além disso, o CloudFormation oferece integração com o IAM para controle de permissões, e permite armazenar os modelos localmente ou em buckets do Amazon S3. A ferramenta também conta com o Infrastructure Composer, que ajuda a visualizar e validar os modelos antes da implantação. Com esse nível de automação e controle, o CloudFormation se torna uma solução ideal para equipes que buscam consistência, escalabilidade e segurança na gestão de infraestrutura em nuvem.

Fonte: https://docs.aws.amazon.com/pt_br/AWSCloudFormation/latest/UserGuide/cloudformation-overview.html

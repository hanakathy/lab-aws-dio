# Desafio 04: Associando Conceitos de Serviços de Armazenamento e CDN – Ciclo de Vida, Replicação, Cache
# Descrição: Além de armazenar e distribuir arquivos, a AWS permite configurar políticas de ciclo de vida, replicação entre regiões e uso de cache. Associe cada termo à sua definição neste desafio.

entrada = input()

def descrever_politica(servico):
  if servico == "Lifecycle Policy":
    return "Regras para mover ou excluir arquivos"
  elif servico == "Cross-Region Replication":
    return "Replica objetos S3 em outra região"
  elif servico == "Cache Behavior":
    return "Define como o CloudFront armazena conteúdo"
  elif servico == "Storage Class":
    return "Define o tipo de armazenamento no S3"

print(descrever_politica(entrada))

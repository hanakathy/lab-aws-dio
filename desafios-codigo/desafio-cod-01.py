# Desafio 01: Associando Conceitos de Recursos da AWS
# Descrição: A AWS permite a criação de diferentes recursos que suportam aplicações em nuvem. Os serviços Amazon EC2, S3 e Lambda oferecem soluções escaláveis e sob demanda. Neste desafio, associe corretamente cada recurso da AWS à sua principal função.

entrada = input()

def descrever_servico(servico):
  if servico == "Amazon EC2":
    return "Serviço de máquinas virtuais sob demanda"
  elif servico == "Amazon S3":
    return "Armazenamento de objetos na nuvem"
  elif servico == "AWS Lambda":
    return "Executa código sem gerenciar servidores"
  elif servico == "Amazon Machine Image":
    return "Modelo de instância EC2 pré-configurado"
  
print(descrever_servico(entrada))

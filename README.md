Sistema web para organizar a rotina de uma oficina mecânica fictícia: clientes, veículos, peças e ordens de serviço em um só lugar.

O projeto nasceu da ideia de substituir anotações em papel por um fluxo simples, no qual a equipe consiga consultar atendimentos, acompanhar os serviços e manter o estoque sob controle.

> **Status:** em desenvolvimento

## O que o sistema busca resolver


Em uma oficina, informações espalhadas dificultam encontrar o histórico de um veículo, saber quais peças estão disponíveis e entender o que foi feito em cada atendimento. A proposta do TorqueWEB é centralizar esses dados e manter o registro das operações importantes.

## Funcionalidades

### Clientes e veículos
- Cadastro de clientes e seus dados de contato.
- Associação de vários veículos a um mesmo cliente.
- Consulta de veículos por informações como placa, marca e modelo.
- Histórico de ordens de serviço relacionado ao veículo.

### Ordens de serviço
- Registro do problema relatado e dos serviços realizados.
- Controle do custo de mão de obra e das peças utilizadas.
- Cálculo do total da ordem de serviço.
- Acompanhamento do status do atendimento.
- Registro dos funcionários responsáveis pelas operações previstas no fluxo.

### Peças e estoque
- Cadastro de peças com código, preço e quantidade disponível.
- Consulta de disponibilidade antes de utilizar uma peça.
- Atualização do estoque conforme as operações da ordem de serviço.
- Planejamento de histórico de movimentações para facilitar a conferência de entradas e saídas.

### Acesso
- Contas individuais para os funcionários.
- Senhas armazenadas com hash usando Argon2.
- Estrutura de navegação adaptada para desktop e dispositivos móveis.

> O projeto ainda está em construção. Algumas telas usam dados de demonstração e nem todos os fluxos descritos estão integrados à API. A lista acima representa o escopo do sistema, não uma afirmação de que todos os recursos já estejam concluídos.

## Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Frontend | React, TypeScript, Vite |
| Interface | Tailwind CSS, shadcn/ui, Lucide |
| Backend | Python, FastAPI, SQLAlchemy |
| Banco de dados | PostgreSQL |
| Segurança de senhas | Argon2 com `pwdlib` |

## Estrutura do projeto

```text
.
├── backend/
│   └── app/
│       ├── auth.py
│       ├── clients.py
│       ├── database.py
│       ├── main.py
│       ├── models.py
│       ├── parts.py
│       ├── vehicles.py
│       └── work_orders.py
└── frontend/
    └── src/
        ├── components/
        │   ├── pages/
        │   └── ui/
        ├── App.tsx
        └── main.tsx
```

A estrutura pode evoluir conforme os endpoints e as telas forem integrados.

## Executar localmente

### Requisitos

- Python instalado.
- Node.js e npm.
- PostgreSQL em execução.

### 1. Configurar o banco

Crie um banco PostgreSQL para o projeto e configure a variável `DATABASE_URL` no arquivo `.env` do backend. Exemplo de formato:

```env
DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/mecanica
```

Use suas próprias credenciais e não envie o `.env` para o repositório.

### 2. Iniciar o backend

No terminal, entre na pasta `backend`, ative seu ambiente virtual e instale as dependências definidas pelo projeto. Depois, execute:

```bash
uvicorn app.main:app --reload
```

A rota inicial disponível retorna uma mensagem simples para confirmar que a aplicação FastAPI está respondendo.

### 3. Iniciar o frontend

No terminal, entre na pasta `frontend`, instale as dependências do projeto e execute o script de desenvolvimento definido no `package.json`, normalmente:

```bash
npm install
npm run dev
```

> Os comandos de instalação dependem dos arquivos de dependências presentes na sua cópia do projeto. Configure o ambiente antes de iniciar a aplicação.

## Testes do backend

Com o ambiente virtual ativado e as variáveis de ambiente configuradas, execute a partir da pasta `backend`:

```bash
python -m pytest -v
```

Os testes existentes cobrem partes dos modelos e das operações de clientes, veículos, peças e ordens de serviço. A cobertura deve acompanhar a implementação dos próximos fluxos.


---

<img width="1622" height="859" alt="image" src="https://github.com/user-attachments/assets/594da9ae-6ed8-4593-94b8-c0121ee6f7ad" />

<img width="1905" height="670" alt="image" src="https://github.com/user-attachments/assets/b336cc9f-107d-440c-8dfa-8e49b985bb70" />



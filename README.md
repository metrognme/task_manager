# Python Learning Lab: JSON & System Logic

Este repositório armazena um projeto prático desenvolvido como parte da minha trilha de aprendizado em Python e Cibersegurança. O foco deste laboratório foi traduzir lógica de negócio em código funcional, explorando os fundamentos da linguagem e a interação com o sistema de arquivos.

## 🎯 O que este projeto faz

> O programa permite a entrada de dados pelo usuário, processa essas informações seguindo regras condicionais definidas e garante que o estado da aplicação seja mantido entre execuções.

## 📚 Conceitos e Habilidades Trabalhadas

Este código serviu como estudo de caso para consolidar os seguintes conceitos fundamentais da programação:

* **Manipulação de Arquivos (File I/O):** Leitura (`read`) e escrita (`write`) de dados em disco, compreendendo como o Python interage com arquivos externos.
* **Serialização de Dados (JSON):** Tratamento de dados estruturados, convertendo objetos nativos do Python (dicionários e listas) para o formato JSON, padrão de mercado para troca de dados.
* **Estruturas de Dados:** Uso prático de listas e dicionários para organizar a informação em memória antes da persistência.
* **Controle de Fluxo:** Implementação de lógica condicional (`if/else`) e loops para validar entradas e controlar o comportamento do programa.
* **Interação com o SO:** Uso de caminhos absolutos baseados no diretório do usuário (`home`).

## 💾 Persistência e Compatibilidade

A persistência dos dados é realizada através de um arquivo `.json` salvo automaticamente na raiz do usuário.

### Nota sobre o Ambiente (Unix-like)
Devido à estrutura educacional deste projeto, o gerenciamento de caminhos (paths) foi construído seguindo a notação **Unix**.
* **Sistemas Suportados:** Linux, macOS, WSL.
* **Atenção:** Em sistemas Windows nativos, a estrutura de diretórios pode gerar erros. A refatoração para uso da biblioteca `pathlib` (para compatibilidade total) está planejada para versões futuras.

## 🚀 Roadmap de Estudos

Como um projeto vivo de aprendizado, as próximas atualizações visam aplicar conceitos de segurança e qualidade de código:

- [ ] Tratamento de erros (Try/Except) para arquivos corrompidos ou inexistentes.
- [ ] Refatoração para `pathlib` (Cross-platform).
- [ ] Modularização do código em funções distintas (Princípio de Responsabilidade Única).

## 📝 Isenção de Responsabilidade

Este é um software desenvolvido para fins educacionais e de autoestudo.

---
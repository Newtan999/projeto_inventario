# projeto_inventario
Projeto de inventario de equipamentos de TI

Equipamento

Cada item de hardware ou software que você quer registrar.

Campos possíveis: nome, tipo, fabricante, modelo, número de série, data de aquisição, status (em uso, em manutenção, inativo).

Departamento / Setor

Para saber onde cada equipamento está alocado.

Campos: nome do departamento, localização, responsável.

Categoria de Equipamento

Ex: “Desktop”, “Notebook”, “Servidor”, “Monitor”, “Software”.

Fornecedor

Campos: nome, telefone, email, endereço.

Manutenção / Histórico

Para registrar manutenções e alterações de status.

Campos: equipamento (FK), data da manutenção, descrição do problema/solução, técnico responsável.

Relacionamentos:

Um equipamento pertence a um departamento → ForeignKey.

Um equipamento pertence a uma categoria → ForeignKey.

Um equipamento pode ter várias manutenções → OneToMany

Um equipamento pode ter um fornecedor → ForeignKey.
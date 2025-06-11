from typing import Optional
from data.forma_pagamento_model import FormaPagamento
from data.forma_pagamento_sql import *
from data.produto_sql import EXCLUIR_POR_ID
from data.util import get_connection


def criar_tabela() -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA)
        return cursor.rowcount > 0


def inserir(forma_pagamento: FormaPagamento) -> Optional[int]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERIR, (
            forma_pagamento.nome, 
            forma_pagamento.desconto))
        id_inserido = cursor.lastrowid
        return id_inserido


def obter_todas() -> list[FormaPagamento]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS)
        rows = cursor.fetchall()
        return [FormaPagamento(
            id=row["id"], 
            nome=row["nome"], 
            desconto=row["desconto"])
            for row in rows]


def excluir_por_id(id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_POR_ID, (id,))
        return (cursor.rowcount > 0)
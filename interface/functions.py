import sqlite3

def insertCliente(id,nome,ddn,cpf,rg,cep,end,numero,complemento,bairro,cidade,estado,tel1,tel2,saldo):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = """INSERT INTO CLIENTES (ID,NAME,DDN,CPF,RG,CEP,ENDERECO,NUMERO,COMPLEMENTO,BAIRRO,CIDADE,ESTADO,TELEFONE1,TELEFONE2,SALDO) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""
    dataTuple = (id,nome,ddn,cpf,rg,cep,end,numero,complemento,bairro,cidade,estado,tel1,tel2,saldo)
    conn.cursor().execute(insert,dataTuple)
    conn.commit()
    conn.close()

def removeCliente(cpf):
    conn = sqlite3.connect('BancoDeDados.db')
    sql = 'DELETE FROM CLIENTES WHERE CPF=?'
    cur = conn.cursor()
    cur.execute(sql, (cpf,))
    conn.commit()
    conn.close()

def updateCliente(id,nome,ddn,cpf,rg,cep,end,numero,complemento,bairro,cidade,estado,tel1,tel2):
    conn = sqlite3.connect('BancoDeDados.db')
    conn.execute("UPDATE CLIENTES set NAME = ?  where ID = ?", (nome,id))
    conn.execute("UPDATE CLIENTES set DDN = ?  where ID = ?", (ddn,id))
    conn.execute("UPDATE CLIENTES set CPF = ?  where ID = ?", (cpf,id))
    conn.execute("UPDATE CLIENTES set RG = ?  where ID = ?", (rg,id))
    conn.execute("UPDATE CLIENTES set CEP = ?  where ID = ?", (cep,id))
    conn.execute("UPDATE CLIENTES set ENDERECO = ?  where ID = ?", (end,id))
    conn.execute("UPDATE CLIENTES set NUMERO = ?  where ID = ?", (numero,id))
    conn.execute("UPDATE CLIENTES set COMPLEMENTO = ?  where ID = ?", (complemento,id))
    conn.execute("UPDATE CLIENTES set BAIRRO = ?  where ID = ?", (bairro,id))
    conn.execute("UPDATE CLIENTES set CIDADE = ?  where ID = ?", (cidade,id))
    conn.execute("UPDATE CLIENTES set ESTADO = ?  where ID = ?", (estado,id))
    conn.execute("UPDATE CLIENTES set TELEFONE1 = ?  where ID = ?", (tel1,id))
    conn.execute("UPDATE CLIENTES set TELEFONE2 = ?  where ID = ?", (tel2,id))
    conn.commit()
    conn.close()

def getClientes(cpf,nome):
    if(cpf != ''):
        conn = sqlite3.connect('BancoDeDados.db')
        select = 'SELECT * FROM CLIENTES WHERE CPF=?'
        cur = conn.cursor()
        cur.execute(select, (cpf,))
        itens = cur.fetchall()
        cur.close()
        return itens
    elif(nome != ''):
        conn = sqlite3.connect('BancoDeDados.db')
        select = 'SELECT * FROM CLIENTES WHERE NOME=?'
        cur = conn.cursor()
        cur.execute(select, (nome,))
        itens = cur.fetchall()
        cur.close()
        return itens
    else:
        return []


def insertAgendamento(id,cpf,evento,descricao,acessorios,ajustes,valor,cupom,desconto,sinal,dde):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = '''INSERT INTO AGENDAMENTOS (ID,CPF,EVENTO,DESCRICAO,ACESSORIOS,AJUSTES,VALOR,CUPOM,DESCONTO,SINAL,DDE) \
      VALUES (?,?,?,?,?,?,?,?,?,?,?);'''
    dataTuple = (id,cpf,evento,descricao,acessorios,ajustes,valor,cupom,desconto,sinal,dde)
    conn.cursor().execute(insert,dataTuple)
    conn.commit()
    conn.close()


def updateAgendamento(id,cpf,evento,descricao,acessorios,ajustes,valor,cupom,desconto,sinal,dde):
    conn = sqlite3.connect('BancoDeDados.db')
    conn.execute("UPDATE AGENDAMENTOS set CPF = ?  where ID = ?", (cpf,id))
    conn.execute("UPDATE AGENDAMENTOS set EVENTO = ?  where ID = ?", (evento,id))
    conn.execute("UPDATE AGENDAMENTOS set DESCRICAO = ?  where ID = ?", (descricao,id))
    conn.execute("UPDATE AGENDAMENTOS set ACESSORIOS = ?  where ID = ?", (acessorios,id))
    conn.execute("UPDATE AGENDAMENTOS set AJUSTES = ?  where ID = ?", (ajustes,id))
    conn.execute("UPDATE AGENDAMENTOS set VALOR = ?  where ID = ?", (valor,id))
    conn.execute("UPDATE AGENDAMENTOS set CUPOM = ?  where ID = ?", (cupom,id))
    conn.execute("UPDATE AGENDAMENTOS set DESCONTO = ?  where ID = ?", (desconto,id))
    conn.execute("UPDATE AGENDAMENTOS set SINAL = ?  where ID = ?", (sinal,id))
    conn.execute("UPDATE AGENDAMENTOS set DDE = ?  where ID = ?", (dde,id))
    conn.commit()
    conn.close()

def removeAgendamento(descricao,id):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = 'DELETE from AGENDAMENTOS where DESCRICAO=? AND ID=?'
    dataTuple = (descricao,id,)
    conn.execute(insert,dataTuple)
    conn.commit()
    conn.close()

def insertCupons(cupom,valorCupom):
    conn = sqlite3.connect('BancoDeDados.db')
    conn.execute('''INSERT INTO CUPONS (CUPOM,VALOR) \
      VALUES ({},{})'''.format(cupom,valorCupom));
    conn.commit()
    conn.close()

def removeCupons(cupom):
    conn = sqlite3.connect('BancoDeDados.db')
    conn.execute('''DELETE from CUPONS where CUPOM = {};'''.format(cupom))
    conn.commit()
    conn.close()

def insertContrato(id,cpf,idAgendamento,ddd,fantasia,valor):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = '''INSERT INTO CONTRATOS (ID,CPF,IDAGENDAMENTO,DDD,FANTASIA,VALOR) \
       VALUES (?,?,?,?,?,?);'''
    dataTuple = (id,cpf,idAgendamento,ddd,fantasia,valor)
    conn.cursor().execute(insert,dataTuple)
    conn.commit()
    conn.close()

def removeContrato(cpf):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = 'DELETE from CONTRATOS where CPF=?'
    dataTuple = (cpf,)
    conn.execute(insert,dataTuple)
    conn.commit()
    conn.close()

def getAgendamentos(cpf,nome):
    if(cpf != ''):
        conn = sqlite3.connect('BancoDeDados.db')
        select = 'SELECT * FROM AGENDAMENTOS WHERE CPF=?'
        cur = conn.cursor()
        cur.execute(select, (cpf,))
        itens = cur.fetchall()
        cur.close()
        return itens
    else:
        return []

def getAgendamentosID(id):
    conn = sqlite3.connect('BancoDeDados.db')
    select = 'SELECT * FROM AGENDAMENTOS WHERE ID=?'
    cur = conn.cursor()
    cur.execute(select, (id,))
    itens = cur.fetchall()
    cur.close()
    return itens

def getAllAgendamentos():
    conn = sqlite3.connect('BancoDeDados.db')
    select = 'SELECT * FROM AGENDAMENTOS'
    cur = conn.cursor()
    cur.execute(select)
    itens = cur.fetchall()
    cur.close()
    return itens

def getAllContratos():
    conn = sqlite3.connect('BancoDeDados.db')
    select = 'SELECT * FROM CONTRATOS'
    cur = conn.cursor()
    cur.execute(select)
    itens = cur.fetchall()
    cur.close()
    return itens

def getAllEventos():
    conn = sqlite3.connect('BancoDeDados.db')
    select = 'SELECT * FROM EVENTOS'
    cur = conn.cursor()
    cur.execute(select)
    itens = cur.fetchall()
    cur.close()
    return itens

def insertEvento(evento,cliente,fantasia,data):
    conn = sqlite3.connect('BancoDeDados.db')
    insert = '''INSERT INTO EVENTOS (EVENTO,CLIENTE,FANTASIA,DATA) \
       VALUES (?,?,?,?);'''
    dataTuple = (evento,cliente,fantasia,data)
    conn.cursor().execute(insert,dataTuple)
    conn.commit()
    conn.close()

def removeEvento(evento):
    conn = sqlite3.connect('BancoDeDados.db')
    remove = 'DELETE FROM EVENTOS WHERE EVENTO=?'
    dataTuple = (evento,)
    conn.execute(remove,dataTuple)
    conn.commit()
    conn.close()

    
def criarTabelas():

    conn = sqlite3.connect('BancoDeDados.db')
    conn.execute('''CREATE TABLE CLIENTES
            (ID INT PRIMARY KEY     ,
            NAME           TEXT    ,
            DDN           TEXT    ,
            CPF           TEXT    ,
            RG           TEXT    ,
            CEP         TEXT    ,
            ENDERECO           TEXT    ,
            NUMERO           TEXT    ,
            COMPLEMENTO           TEXT    ,
            BAIRRO           TEXT    ,
            CIDADE           TEXT    ,
            ESTADO           TEXT    ,
            TELEFONE1           TEXT    ,
            TELEFONE2           TEXT    ,
            SALDO           TEXT    );''')

    conn.execute('''CREATE TABLE AGENDAMENTOS
            (ID INT PRIMARY KEY     ,
            CPF           TEXT    ,
            EVENTO           TEXT    ,
            DESCRICAO           TEXT    ,
            ACESSORIOS           TEXT    ,
            AJUSTES           TEXT    ,
            VALOR           TEXT    ,
            CUPOM           TEXT    ,
            DESCONTO           TEXT    ,
            SINAL           TEXT    ,
            DDE           TEXT    );''')

    conn.execute('''CREATE TABLE CONTRATOS
            (ID INT PRIMARY KEY     ,
            CPF           TEXT    ,
            IDAGENDAMENTO           TEXT    ,
            DDD           TEXT,
            FANTASIA      TEXT    );''')

    conn.execute('''CREATE TABLE CUPONS
            (CUPOM           TEXT    ,
         VALOR           TEXT    );''')
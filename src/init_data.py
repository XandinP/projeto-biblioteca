
import re
from db.database_manager import DatabaseManager


db = DatabaseManager()
db.createConnection()

def runSql(filePath):
    try: 
        with open(filePath, 'r') as sqlFile:
            sqlCommands = extractSqlCommands(sqlFile.read())
            for sqlCommand in sqlCommands:
                executeSqlCommand(sqlCommand)
        print(f"sql '{filePath}' executado com sucesso")
    except Exception as err:
        print(f"erro ao executar o arquivo '{filePath}': {str(err)}")

def extractSqlCommands(sqlText):
    ## separa comandos por ; e ignora comentarios
    sqlCommands = re.split(r';(?![^\(]*\))', sqlText)
    cleanedCommands = []
    
    for command in sqlCommands:
        cleanedCommand = removeComments(command.strip())
        if cleanedCommand:
            cleanedCommands.append(cleanedCommand)
    
    return cleanedCommands

def removeComments(sqlText):
    ## remove comentarios (single-line e multi-line)
    sqlText = re.sub(r'--.*$', '', sqlText, flags=re.MULTILINE)
    sqlText = re.sub(r'/\*.*?\*/', '', sqlText, flags=re.DOTALL)
    return sqlText


def executeSqlCommand(sqlCommand):
    try:
        if sqlCommand:
            db.execute(sqlCommand)
            print(f"***EXECUTADO COM SUCESSO***\n {sqlCommand}\n********************")
    except Exception as err:
        print(f"***ERRO AO EXECUTAR***\n{sqlCommand}: {str(err)}\n*******************")
        

print("Inicializando dados")
runSql("../data/01_create_tables.sql")
runSql("../data/02_insert_data.sql")
print("Inicializacao de dados concluida")

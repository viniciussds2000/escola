logins = {"Vinicius": '123',"Gabriel":'123',"Beatriz":'123'}

disciplinas = {"Vinicius": [['lpt1',5.6,7.7,8],['Lab prog 1',10,8,9.5]],
               'Gabriel': [['lpt2',7,9.3,8.3],['Lab prog 2', 1,3.6,6.9]],
               'Beatriz': [['Chiclets',4.9,5.6],["Bandidin 2",5.6,8,9.3]]
               }


def get_login(logg,senha):
    return (logg in logins) and (logins[logg] == senha)

def get_disciplinas(login):
    return disciplinas[login]









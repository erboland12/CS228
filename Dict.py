import pickle

database = pickle.load(open('userData/database.p', 'rb'))

userName = raw_input('Please enter your name: ')
if userName in database:
    logs = database[userName]['logins']
    temp = logs + 1
    database[userName]['logins'] = temp

    print 'welcome back ' + userName + '.'
else:
    database[userName] = {}
    database[userName]['logins'] = 1
    print 'welcome ' + userName + '.'

print database

pickle.dump(database, open('userData/database.p', 'wb'))

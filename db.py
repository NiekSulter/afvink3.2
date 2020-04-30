import mysql.connector

def load_messages(username, password, zoekterm):
    conn = mysql.connector.connect(host='hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com',
                                   user=username + '@hannl-hlo-bioinformatica-mysqlsrv',
                                   password= password,
                                   db='bioinfadmin')


    cursor = conn.cursor()
    cursor.execute('select bericht, datum, tijd, voornaam from piep join student s on piep.student_nr = s.student_nr '
                   'where bericht like \'%{}%\''.format(zoekterm))


    messages = []
    dates = []
    time = []
    user = []
    for i in cursor:
        messages.append(i[0])
        dates.append(i[1])
        time.append(i[2])
        user.append(i[3])

    return messages, dates, time, user


if __name__ == '__main__':
    load_messages(
        'ymxub', '616623', 'Piep')
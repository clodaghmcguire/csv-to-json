# https://pypi.org/project/dictor/
from dictor import dictor  # this library supports searching through nested dictionaries/json
from datetime import timezone, datetime
import csv
import json

now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%Z')+'Z'

# all accounts have the default 'competency' as the password for django
password = "pbkdf2_sha256$150000$jxm5cdnhGEBl$9Vziw8JeQPKyr2kU8IihEpn90jnYeYdwMCJeUayURAE="

managers = ['Aytug', 'Nicholas']

data = []
n = 1
staff = {}
staff['model'] = "staffrecord.user"
staff['pk'] = n
staff['fields'] = {}
staff['fields']['password'] = password
staff['fields']['last_login'] = now
staff['fields']['is_superuser'] = True
staff['fields']['username'] = "adminuser"
staff['fields']['first_name'] = "admin"
staff['fields']['last_name'] = "user"
staff['fields']['email'] = "clodagh.mcguire@nhs.net"
staff['fields']['is_staff'] = True
staff['fields']['is_active'] = True
staff['fields']['date_joined'] = now
staff['fields']['laboratory'] = 1
staff['fields']['role'] = 3
staff['fields']['start_date'] = "2020-11-17"
staff['fields']['end_date'] = None
staff['fields']['on_leave'] = False
staff['fields']['groups'] = []
staff['fields']['user_permissions'] = []

data.append(staff)
n = n + 1

reader = csv.DictReader(open('Staff_details.csv', encoding='utf-8-sig'))
for row in reader:

    search = dictor(data, search='fields')
    if row['first_name'] in dictor(search, search='first_name'):
        pass
    else:
        username = row['first_name'].lower() + row['last_name'].lower()
        username = username.replace(" ", "")
        staff = {}
        staff['model'] = "staffrecord.user"
        staff['pk'] = n
        staff['fields'] = {}
        staff['fields']['password'] = password
        staff['fields']['last_login'] = now
        if row['first_name'] in managers:
            staff['fields']['is_superuser'] = True
        else:
            staff['fields']['is_superuser'] = False
        staff['fields']['username'] = username
        staff['fields']['first_name'] = row['first_name']
        staff['fields']['last_name'] = row['last_name']
        staff['fields']['email'] = row['email']
        staff['fields']['is_staff'] = False
        staff['fields']['is_active'] = True
        staff['fields']['date_joined'] = now
        staff['fields']['laboratory'] = 2
        if row['first_name'] in managers:
            staff['fields']['role'] = 2
        else:
            staff['fields']['role'] = 1
        staff['fields']['start_date'] = datetime.strptime(row['start_date'], "%d/%m/%Y").strftime("%Y-%m-%d")
        staff['fields']['end_date'] = None
        staff['fields']['on_leave'] = False
        staff['fields']['groups'] = []
        staff['fields']['user_permissions'] = []

        n = n + 1
        data.append(staff)

organisation = {}
organisation['model'] = "staffrecord.organisation"
organisation['pk'] = 1
organisation['fields'] = {}
organisation['fields']['name'] = "King's College Hospital NHS Foundation Trust"
organisation['fields']['created_at'] = now
organisation['fields']['updated_at'] = now
data.append(organisation)

department = {}
department['model'] = "staffrecord.department"
department['pk'] = 1
department['fields'] = {}
department['fields']['organisation'] = 1
department['fields']['name'] = "Test department"
department['fields']['created_at'] = now
department['fields']['updated_at'] = now
data.append(department)

department = {}
department['model'] = "staffrecord.department"
department['pk'] = 2
department['fields'] = {}
department['fields']['organisation'] = 1
department['fields']['name'] = "Precision Medicine"
department['fields']['created_at'] = now
department['fields']['updated_at'] = now
data.append(department)

laboratory = {}
laboratory['model'] = "staffrecord.laboratory"
laboratory['pk'] = 1
laboratory['fields'] = {}
laboratory['fields']['department'] = 1
laboratory['fields']['name'] = "Test Laboratory"
laboratory['fields']['created_at'] = now
laboratory['fields']['updated_at'] = now
data.append(laboratory)

laboratory = {}
laboratory['model'] = "staffrecord.laboratory"
laboratory['pk'] = 2
laboratory['fields'] = {}
laboratory['fields']['department'] = 2
laboratory['fields']['name'] = "LMH"
laboratory['fields']['created_at'] = now
laboratory['fields']['updated_at'] = now
data.append(laboratory)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))
n = 1
for type in ['Managerial', 'Appraisal', 'Equipment']:
    category = {}
    category['model'] = "staffrecord.category"
    category['pk'] = n
    category['fields'] = {}
    category['fields']['type'] = type
    category['fields']['created_at'] = now
    category['fields']['updated_at'] = now

    n = n + 1
    data.append(category)

for row in reader:
    search = dictor(data, search='fields')
    if row['Category'] in dictor(search, search='type'):
        pass
    else:
        category = {}
        category['model'] = "staffrecord.category"
        category['pk'] = n
        category['fields'] = {}
        category['fields']['type'] = row['Category']
        category['fields']['created_at'] = now
        category['fields']['updated_at'] = now

        n = n + 1
        data.append(category)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))
n = 1
for row in reader:
    if row['SOP No'] == "N/A":
        pass
    else:
        sop_list = row['SOP No'].split(" & ")
        for sop_id in sop_list:
            if n == 1:
                sop = {}
                sop['model'] = "staffrecord.sop"
                sop['pk'] = n
                sop['fields'] = {}
                sop['fields']['name'] = sop_id
                sop['fields']['created_at'] = now
                sop['fields']['updated_at'] = now
                n = n + 1
                data.append(sop)
            else:
                search = dictor(data, search='fields')
                if sop_id in dictor(search, search='name'):
                    pass
                else:
                    sop = {}
                    sop['model'] = "staffrecord.sop"
                    sop['pk'] = n
                    sop['fields'] = {}
                    sop['fields']['name'] = sop_id
                    sop['fields']['created_at'] = now
                    sop['fields']['updated_at'] = now

                    n = n + 1
                    data.append(sop)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))
n = 1
for row in reader:
    if n == 1:
        frequency = {}
        frequency['model'] = "staffrecord.frequency"
        frequency['pk'] = n
        frequency['fields'] = {}
        frequency['fields']['time'] = row['Freq']
        frequency['fields']['created_at'] = now
        frequency['fields']['updated_at'] = now

        n = n + 1
        data.append(frequency)
    else:
        search = dictor(data, search='fields')
        if row['Freq'] in dictor(search, search='time'):
            pass
        else:
            frequency = {}
            frequency['model'] = "staffrecord.frequency"
            frequency['pk'] = n
            frequency['fields'] = {}
            frequency['fields']['time'] = row['Freq']
            frequency['fields']['created_at'] = now
            frequency['fields']['updated_at'] = now

            n = n + 1
            data.append(frequency)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))
n = 1
for row in reader:
    if n == 1:
        competency = {}
        competency['model'] = "staffrecord.competency"
        competency['pk'] = n
        competency['fields'] = {}
        competency['fields']['title'] = row['Test']
        competency['fields']['laboratory'] = 2  # sets laboratory to LMH for all competencies
        for item in data:
            try:
                if row['Category'] in dictor(item, 'fields.type'):
                    competency['fields']['category'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        for item in data:
            try:
                if row['Freq'] in dictor(item, 'fields.time'):
                    competency['fields']['frequency'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        competency['fields']['created_at'] = now
        competency['fields']['updated_at'] = now
        competency['fields']['created_by'] = None
        competency['fields']['updated_by'] = None
        sop_list = row['SOP No'].split(" & ")
        sop_id_list = []
        for sop_name in sop_list:
            for item in data:
                try:
                    if sop_name in dictor(item, 'fields.name'):
                        sop_id_list.append(
                            item['pk'])  # searches dictionary for matching category and add the pk as foreignkey
                except TypeError:
                    pass
        competency['fields']['sop'] = sop_id_list

        n = n + 1
        data.append(competency)
    else:
        search = dictor(data, search='fields')
        if row['Test'] in dictor(search, search='title'):
            pass  # skips any tests that have already been added to the dictionary so that each test object is unique
        else:
            competency = {}
            competency['model'] = "staffrecord.competency"
            competency['pk'] = n
            competency['fields'] = {}
            competency['fields']['title'] = row['Test']
            competency['fields']['laboratory'] = 2  # sets laboratory to LMH for all competencies
            for item in data:
                try:
                    if row['Category'] in dictor(item, 'fields.type'):
                        competency['fields']['category'] = item[
                            'pk']  # searches dictionary for matching category and add the pk as foreignkey
                except TypeError:
                    pass
            for item in data:
                try:
                    if row['Freq'] in dictor(item, 'fields.time'):
                        competency['fields']['frequency'] = item[
                            'pk']  # searches dictionary for matching category and add the pk as foreignkey
                except TypeError:
                    pass
            competency['fields']['created_at'] = now
            competency['fields']['updated_at'] = now
            competency['fields']['created_by'] = 1
            competency['fields']['updated_by'] = 1
            sop_list = row['SOP No'].split(" & ")
            sop_id_list = []
            for sop_name in sop_list:
                for item in data:
                    try:
                        if sop_name in dictor(item, 'fields.name'):
                            sop_id_list.append(
                                item['pk'])  # searches dictionary for matching category and add the pk as foreignkey
                    except TypeError:
                        pass
            competency['fields']['sop'] = sop_id_list

            n = n + 1
            data.append(competency)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))

n = 1
for row in reader:
    if n == 1:
        assignment = {}
        assignment['model'] = "staffrecord.competency_assignment"
        assignment['pk'] = n
        assignment['fields'] = {}
        for item in data:
            try:
                if row['Trainee'] in dictor(item, 'fields.first_name'):
                    assignment['fields']['staff_name'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        for item in data:
            try:
                if row['Test'] in dictor(item, 'fields.title'):
                    assignment['fields']['competency'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        if row['Eligible'] == "N":
            assignment['fields']['eligible'] = False
        else:
            assignment['fields']['eligible'] = True
        assignment['fields']['due_now'] = None
        assignment['fields']['created_at'] = now
        assignment['fields']['updated_at'] = now
        assignment['fields']['created_by'] = 1
        assignment['fields']['updated_by'] = 1

        n = n + 1
        data.append(assignment)
    else:
        assignment = {}
        assignment['model'] = "staffrecord.competency_assignment"
        assignment['pk'] = n
        assignment['fields'] = {}
        for item in data:
            try:
                if row['Trainee'] in dictor(item, 'fields.first_name'):
                    assignment['fields']['staff_name'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        for item in data:
            try:
                if row['Test'] in dictor(item, 'fields.title'):
                    assignment['fields']['competency'] = item[
                        'pk']  # searches dictionary for matching category and add the pk as foreignkey
            except TypeError:
                pass
        if row['Eligible'] == "N":
            assignment['fields']['eligible'] = False
        else:
            assignment['fields']['eligible'] = True
        assignment['fields']['due_now'] = None
        assignment['fields']['created_at'] = now
        assignment['fields']['updated_at'] = now
        assignment['fields']['created_by'] = 1
        assignment['fields']['updated_by'] = 1

        n = n + 1
        data.append(assignment)

reader = csv.DictReader(open('LMH assessments.csv', encoding='utf-8-sig'))
pk = 1
n = 1
years = ['2016', '2017', '2018', '2019', '2020']
for row in reader:
    for year in years:
        if row[year]:
            assessment = {}
            assessment['model'] = "staffrecord.competency_assessment"
            assessment['pk'] = n
            assessment['fields'] = {}
            assessment['fields']['competency'] = pk
            assessment['fields']['level'] = 1
            assessment['fields']['authoriser'] = None
            assessment['fields']['authorised_date'] = datetime.strptime(row[year], "%d/%m/%Y").strftime("%Y-%m-%d")
            assessment['fields']['authorised'] = True
            assessment['fields']['trainee_agreement'] = True
            assessment['fields']['trainee_agreement_date'] = datetime.strptime(row[year], "%d/%m/%Y").strftime(
                "%Y-%m-%d")
            assessment['fields']['created_at'] = now
            assessment['fields']['updated_at'] = now
            assessment['fields']['created_by'] = 1
            assessment['fields']['updated_by'] = 1
            n = n + 1
            data.append(assessment)

    pk = pk + 1

reader = csv.DictReader(open('Assessment_questions.csv'))
n = 1
for row in reader:
    question = {}
    question['model'] = "staffrecord.question"
    question['pk'] = n
    question['fields'] = {}
    question['fields']['question'] = row['question']
    question['fields']['created_at'] = now
    question['fields']['updated_at'] = now
    n = n + 1
    data.append(question)

n = 1
for item in data:
    try:
        if "staffrecord.competency_assessment" in dictor(item, 'model'):
            answer = {}
            answer['model'] = "staffrecord.answer"
            answer['pk'] = n
            answer['fields'] = {}
            answer['fields']['question'] = 1
            answer['fields']['answer'] = "See printed record on shelf"
            answer['fields']['assessed_by'] = None
            answer['fields']['assessed_date'] = None
            answer['fields']['related_assessment'] = item['pk']
            answer['fields']['created_at'] = now
            answer['fields']['updated_at'] = now
            answer['fields']['created_by'] = 1
            answer['fields']['updated_by'] = 1
            n = n + 1
            data.append(answer)

    except TypeError:
        pass

with open('lmh_data.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))

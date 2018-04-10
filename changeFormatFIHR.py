import json

data = {}

data['patient'] = []
data['patient'].append({
	'identifier':identifier,
	'active':active,
	'name':name,
	'telecom':telecom,
	'gender':gender,
	'birthdate':birthdate,
	'deceased':[
		'status':status,
		'datetime':datatime],
	'address':address,
	'maritalstatus':maritalstatus,
	'multiplebirth':[
		'mbbool':mbbool,
		'mbint':mbint],
	'photo':photo,
	'contact':[
		'relation':relation,
		'name':telecom,
		'address':caddress,
		'gender':gender,
		'organization':org,
		'period':period],
	'animal':[
		'species':species,
		'breed':breed,
		'genderstatus':genderstatus],
	'communication':[
		'language':language,
		'preferred':preferred],
	'generalpractitioner':gpract,
	'managingorganization':morg,
	'link':[
		'other':other,
		'type':ltype]})


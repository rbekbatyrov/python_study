def greet_user():
	print("Hello!!!")

greet_user()
print("---")

def greet_user_with_parameter(username):
	print(f"Hello, {username.title()}!!!")

greet_user_with_parameter('jimi')
print("---")

def descibe_pet(animal_type, pet_name):
	print(animal_type.title())
	print(pet_name.title())

descibe_pet(animal_type='hamster', pet_name='harry')
print("---")

def descibe_pet_2(animal_type, pet_name='harry'):
	print(animal_type.title())
	print(pet_name.title())

descibe_pet_2(animal_type='hamster')
print("---")

def get_formatted_name(f_name, l_name):
	full_name = f"{f_name} {l_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("---")

def get_formatted_name_1(f_name, l_name, m_name=''):
	if m_name:
		full_name = f"{f_name} {l_name} {m_name}"
	else:
		full_name = f"{f_name} {l_name}"
	return full_name.title()

musician = get_formatted_name_1('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_1('jimi', 'hendrix', 'lee')
print(musician)
print("---")

def build_person(f_name, l_name, age=None):
	person = {'first':f_name, 'last':l_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=23)
print(musician)
print("---")

def make_pizza(*toppings):
	print(toppings)
make_pizza('pepperoni')

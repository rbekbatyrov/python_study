#echo string
print('Helloworld!!!')
print('---')

#create variable and print it
hello_message='Helloworld!!!'
print(hello_message)
print('---')

#work with hello_message string
hello_message='HELLO WORLD!!!'
print(hello_message.lower())
hello_message='hello world!!!'
print(hello_message.upper())
print(hello_message.title())
print('---')

#work with printing messages
print('Hey,' , '\n\thello', '\n\tworld')
print('---')

#work with format string variables
variable_1='hello'
variable_2='world'
new_hellow_world=f'{variable_1} {variable_2}'
print(new_hellow_world)
print('---')

#work with strip
strip_variable_1=' hello '
strip_variable_2=' world '
strip_hellow_world=f'{strip_variable_1} {strip_variable_2} {strip_variable_1} test'
print(strip_hellow_world)
strip_hellow_world=f'{strip_variable_1.lstrip()} {strip_variable_2.rstrip()}, {strip_variable_1.strip()} test'
print(strip_hellow_world)

#Functions with outputs

"""def format_name(f_name,l_name):
  formatted_f_name=f_name.title() 
  formatter_l_name=l_name.title()
  return f"{formatted_f_name} {formatted_l_name}" """

#OR

def format_name(f_name,l_name):
  name= f_name+" "+l_name
  name=name.title()
  return name

formatted_string=format_name("hAZal","senTURK")
print(formatted_string)
#OR
print(format_name("hAZal","senTURK"))



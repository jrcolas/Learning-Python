### Functions with outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("FRANCK", "colas")
print(formatted_string)

### Multiple Return Values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("FRANCK", "colas")
print(format_name(input("What is your first name? "), input("What is your last name? ")))


### Docstrings

def someFunction(something):
    """Takes something and does something else with it."""
    something += something
    return something

someFunction("stuff")
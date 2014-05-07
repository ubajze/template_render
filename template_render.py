from jinja2 import Template
import argparse
import re


def get_text_file(template,variables):

    """
    Function takes template string and variable values as input and generates string in which variables are replaced with values.
    
    Temlate must be in jinja2 format where variable is marked as {{ variable }}.
    Variables must be in dictionary format where dictionary keys are the same as variables in template.
    """

    template_class = Template(template)
    return template_class.render(variables)



def get_variables_from_template(template):

    """
    The function is used to extract variables from template string. It takes template string as input and return sorted list of variables.
    """

    template_variables = []
    for i in re.findall('{{\s[a-z0-9A-Z_-]*\s}}', template):
        template_variables.append(i[2:-2].lstrip().rstrip())
    return sorted(list(set(template_variables)))



def get_input_from_command_line(template_variables):

    """
    The function is used to get values for variables from the user. It takes list of variables and return dictionary where keys are the same as variables in input list. 
    """

    variable_values = {}
    for i in template_variables:
        raw_input_empty = True
        while raw_input_empty:        
            input = raw_input('Enter value for variable ' + i + ': ')
            if input != '':
                raw_input_empty = False
        variable_values[i] = input
    return variable_values



def parse_command_line_arguments():

    """
    The function is used to provide argument parsing when function is called from the command line.
    """

    parser = argparse.ArgumentParser(description='Generate text file from template', epilog='all variables in template file must be in the form {{ variable }}')
    parser.add_argument('-t', '--temp', help='path to the template file', required=True, type=file, metavar='FILE')
    parser.add_argument('-v', '--version', help='display version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()
    return vars(args)['temp'].read()


if __name__ == "__main__":

    try:
        template_file = parse_command_line_arguments()
        template_variables = get_variables_from_template(template_file)
        variable_values = get_input_from_command_line(template_variables)
        print get_text_file(template_file,variable_values)
       
    except KeyboardInterrupt:
        print "\nProgram was interrupted by user"
    except:
        raise



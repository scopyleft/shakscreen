def fields_label(fields, dict):
    """
    Translates form field labels
    fields: form fields list
    dict: dict of key: value where key if the form field name and value
        is the translated string
    """
    for key in dict:
        try:
            fields[key].label = dict[key]
        except KeyError:
            raise KeyError('Form field transctription error : no field "%s" exists.' % key)


def fields_help(fields, dict):
    """
    Inserts form field help texts
    fields: form fields list
    dict: dict of key: value where key if the form field name and value
        is the translated string
    """
    for key in dict:
        try:
            fields[key].help_text = dict[key]
        except KeyError:
            raise KeyError('Form field transctription error : no field "%s" exists.' % key)

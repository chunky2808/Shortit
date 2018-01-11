from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	reg_val =value
	if "http" in reg_val:
		new_value = reg_val
	else:
		new_value = 'http://' + value
	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalide URL for the field")
	return new_value

	# except:
	# 	value_1_invalid = True

	# value_2_invalid = "http://" + value

	# try:
	# 	url_validator(value_2_invalid)
	# except:
	# 	value_2_invalid = True
	#if value_1_invalid == False and value_2_invalid == False:

def validate_dot_com(value):
	if not "com" in value:
		raise ValidationError("This is not valid because of no .com")
	return value

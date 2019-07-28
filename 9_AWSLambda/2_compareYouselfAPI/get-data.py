import json

def lambda_handler(event, context):
  re = event.type
  if re == 'all':
    return 'All the data'
  elif re == 'single':
    return 'Just my data'
  else:
    return 'type request not found'
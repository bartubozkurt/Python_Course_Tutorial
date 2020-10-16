def full_emails(people):
  result = []
  for  name, email in people:
    result.append(("{} <{}>".format(name,email))
   return result

print(full_emails(["bartubozkurt35@gmail.com", "Bartu Bozkurt",
      ("altaybzkrt@hotmail.com", "Altay Bozkurt")]))
                  

## ['Bartu Bozkurt <bartubozkurt35@gmail.com>','Altay Bozkurt <altaybzkrt@hotmail.com>']

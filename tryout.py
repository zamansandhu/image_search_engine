#here is the function - call this function separately, replace retrun with print, and you will see it works fine

#this function needs to process the file that is being uploaded, NOT the wording inside
def run_processing(text):
   wording = text#'The Consultant is very lolo lolo nunu blable'
   d = {'print this': ['John', 'Consultant', 'Consultant'], 'another one': ['blable', 'lolo', 'nunu']}
   for key,value in d.items():
       for item in value:
           if item in wording:
               yield (key)
               break

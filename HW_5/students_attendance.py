students = {
    'Stan Marsh': ['Python', 'FrontEnd'],
    'Kyle Broflovski': ['FullStack', 'Java'],
    'Eric Cartman': ['Python', 'Java', 'FullStack'],
    'Kenny McCormick': ['FrontEnd'],
    'Leopold Stotch': ['FullStack'],
    'Wendy Testaburger': ['FullStack', 'Java'],
}

print('Students that attend two or more groups:')
for k, v in students.items():
   if len(v) > 1:
      print(k)

print('-----------------------------------------')

print('Students that do not attend FrontEnd course:')
for k, v in students.items():
   if 'FrontEnd' not in v:
      print(k)

print('-----------------------------------------')

print('Students that study Python or Java:')
for k,v in students.items():
   if 'Python' in v or 'Java' in v or 'FrontEnd' in v:
      print(k)

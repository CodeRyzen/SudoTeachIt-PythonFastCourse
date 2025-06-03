string = "I just recently started learning programming, however, I'm doing well, " \
         "and I'm already going through the topic of cycles! " \
         "Thanks to the YouTube channel sudo teach thanks to which I learn."
         
counter = 1
for i in string:
    if i == ' ':
        counter += 1  

print(counter)

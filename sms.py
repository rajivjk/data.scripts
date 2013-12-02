
import names
import random

names_list = []

#generate a list of random names

print "sender, receiver, num_texts_sent"
for i in range(1,31):
    names_list.append(names.get_full_name())

#remove duplicates
unique_names = set(names_list)

senders_names = []
for name in unique_names:
    senders_names.append(name)
    receivers = unique_names - set(senders_names)
    for name2 in receivers:
        #print name + "," + name2 + "," + random.randint(0,1000)
        print "{name}, {name2}, {numtexts}".format(name=name,name2=name2,
                                            numtexts=random.randint(0,1000))


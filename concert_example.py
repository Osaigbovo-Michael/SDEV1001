concert_name = input('WHat is the name of the concert tonight?')
has_ticket = input('Do you have a ticket? (yes/no)')

if concert_name == 'Coldplay' and has_ticket.lower() == 'yes':
    print('Come on in, the show is about to start!')

elif concert_name == 'Coldplay' and has_ticket.lower() == 'no':
    print('You need a ticket to get in')    

elif concert_name == 'Metallica':
    print('Thats next door')    

else:
    print('Sorry, this is not the venue')    
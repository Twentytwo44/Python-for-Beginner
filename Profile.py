class profile:
    '''
     my = profile('twentytwo')
    my.company = 'starttech'
    my.hobby = ["Coding",'Play Game','Play Sport']
    print(my.name)
    my.show_email()
    my.show_hobby()
    my.show_art()

    
    
    '''
    def __init__(self,name):
        self.name = name
        self.company = ''
        self.hobby = ''
        self.art = '''
╔════╗╔╗╔╗╔╗╔═══╗╔═╗ ╔╗╔════╗╔╗  ╔╗╔════╗╔╗╔╗╔╗╔═══╗
║╔╗╔╗║║║║║║║║╔══╝║║╚╗║║║╔╗╔╗║║╚╗╔╝║║╔╗╔╗║║║║║║║║╔═╗║
╚╝║║╚╝║║║║║║║╚══╗║╔╗╚╝║╚╝║║╚╝╚╗╚╝╔╝╚╝║║╚╝║║║║║║║║ ║║
  ║║  ║╚╝╚╝║║╔══╝║║╚╗║║  ║║   ╚╗╔╝   ║║  ║╚╝╚╝║║║ ║║
 ╔╝╚╗ ╚╗╔╗╔╝║╚══╗║║ ║║║ ╔╝╚╗   ║║   ╔╝╚╗ ╚╗╔╗╔╝║╚═╝║
 ╚══╝  ╚╝╚╝ ╚═══╝╚╝ ╚═╝ ╚══╝   ╚╝   ╚══╝  ╚╝╚╝ ╚═══╝ 
        '''
    def show_email(self):
        if self.company != '':
            print('{}@{}.com'.format(self.name.lower(),self.company))
        else:
            print('{}@gmail.com'.format(self.name.lower()))


    def show_art(self):
        print(self.art)

    def show_hobby(self):
        if len(self.hobby) != 0:
            print('----My Hobby----')
            for i,e in enumerate(self.hobby,start=1):
                print(str(i) + "." + str(e))
                print('------------')
        else:
            print('----No Hobby----')
    
if __name__ == "__main__":
    my = profile('twentytwo')
    my.company = 'starttech'
    my.hobby = ["Coding",'Play Game','Play Sport']
    print(my.name)
    my.show_email()
    my.show_hobby()
    my.show_art()

    #help(my)
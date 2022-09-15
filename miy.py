
class CLI :

    def __init__( self ) :
        pass

    def run ( self ) :
        while True :
            sInput = input('>>> ')
            if sInput == 'exit' :
                break
            print(sInput)

if __name__ == '__main__' :
    CLI().run()

def make_gereting(language):
    def greet(name):
        
        if language =="hindi":
            print("sukriya, ", name)
            
        return greet
    hindi_greeting = make_gereting("hindi")
    
    hindi_greeting("rahul")
    
         
        
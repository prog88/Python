# definition
def Get_Description_From(language):
    match language:
        case "javascript":  
            print("your are Web developer")
        case "python":      
            print("you are an AI developer")
        case "java":        
            print("you are a Software developer")
        case "reactjs":     
            print("you are an Mobile developer")

# execute
Get_Description_From("reactjs")
Get_Description_From("java")
Get_Description_From("python")
Get_Description_From("javascript")
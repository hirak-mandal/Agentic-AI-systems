import os
def document_loader():
        documents=[]
        base_path="knowledge_base"
        #subfolder loop
        for folder in os.listdir(base_path):
                folder_path=os.path.join(base_path,folder)
        
        #file loop
        for file in os.listdir(folder_path):
                #only .txt files
                if file.endswith(".txt"):
                        file_path=os.path.join(folder_path,file)
                
                with open(file_path,"r") as f:
                        documents.append(f.read())
        return documents

file = open("terraformModel", "w")

def createProvider(file,provider,region,access_key,secret_key):
    file.write("provider "+'"'+provider+'"'+"{\n")
    file.write("  region = "+'"'+region+'"\n')
    file.write("  access_key = "+'"'+access_key+'"\n')
    file.write("  secret_key = "+'"'+secret_key+'"\n')
    file.write("}\n"),

createProvider(file,"aws","us-east-1","21212121","121213")
file.close()


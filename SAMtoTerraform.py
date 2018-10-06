def createProvider(file,provider,region,access_key,secret_key):
    file.write("provider "+'"'+provider+'"'+"{\n"
            "  region = "+'"'+region+'"\n'
            "  access_key = "+'"'+access_key+'"\n'
            "  secret_key = "+'"'+secret_key+'"\n'
            "}\n")




def function_resource(file):
    file.write("resource  "+ "aws_lambda_function " +'"example"' + " {\n"
          " function_name = "+'"'+"ServerlessExample"+'"\n'
            "\n"
      
          " s3_bucket = "+'"'+"terraform-serverless-example"+'"\n'
          " s3_key    = "+'"'+"v1.0.0/example.zip"+'"\n'

     
          " handler = "+'"'+"main.handler"+'"\n'
          " runtime = "+'"'+"nodejs6.10"+'"\n'

          " role = "+"${aws_iam_role.lambda_exec.arn}\n"
        "}"
        )

file = open("terraformModel", "w")

createProvider(file,"aws","us-east-1","21212121","121213")
function_resource(file)
file.close()


fh = open("hello_world.yaml.", "r")

arr = []
parmeters = {}
for line in fh:
    if(line!='\n'):
        item = line.strip().split(":")
        arr.append(item)
        parmeters[item[0]] = [item[1]]
        print (line)
    
    

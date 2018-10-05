
file = open("terraformModel", "w")

def createProvider(file,provider,region,access_key,secret_key):
    file.write("provider "+'"'+provider+'"'+"{\n")
    file.write("  region = "+'"'+region+'"\n')
    file.write("  access_key = "+'"'+access_key+'"\n')
    file.write("  secret_key = "+'"'+secret_key+'"\n')
    file.write("}\n"),




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


createProvider(file,"aws","us-east-1","21212121","121213")
function_resource(file)
file.close()

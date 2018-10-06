# aws-sam-mapping-terraform
This is a model that can map AWS SAM to the terraform module

<p align="center"><img src="https://github.com/chashikajw/smart-worker-images/blob/master/terraformmap.jpg" /></p>

What is Terraform?
===================

Terraform is an open source tool created by HashiCorp and written in the Go programming language.
The Go code compiles down into a single binary called, terraform.
You can use this binary to deploy infrastructure from your laptop or a build server or just about any other computer, and you don’t need to run any extra infrastructure to make that happen.
That’s because under the hood, the terraform binary makes API calls on your behalf to one or more providers, such as Amazon Web Services (AWS), Azure, Google Cloud, DigitalOcean, OpenStack, etc.
That means Terraform gets to leverage the infrastructure those providers are already running for their API servers, as well as the authentication mechanisms you’re already using with those providers (e.g., the API keys you already have for AWS).


What is AWS Serverless Application Model (AWS SAM)?
===================

What is a serverless architecture?
A serverless architecture is a way to build and run applications and services without having to manage infrastructure.
Your application still runs on servers, but all the server management is done by AWS.
You no longer have to provision, scale, and maintain servers to run your applications, databases, and storage systems.

AWS Serverless Application Model (AWS SAM)
The AWS Serverless Application Model (AWS SAM) is a model to define serverless applications.
AWS SAM is natively supported by AWS CloudFormation and defines simplified syntax for expressing serverless resources.
The specification currently covers APIs, Lambda functions and Amazon DynamoDB tables.
SAM is available under Apache 2.0 for AWS partners and customers to adopt and extend within their own toolsets.

What is Mapping module?
===================

Mapping module can map SAM to terraform model.


**References**</br>
[AWS Serverless Application Module(AWS)](https://github.com/awslabs/serverless-application-model)</br>
[Terraform](https://www.terraform.io/)</br>


**Licence**</br>
[MIT licence](https://github.com/codezilla2018/aws-sam-mapping-terraform/blob/master/LICENSE)
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

sudo apt-get update
sudo apt-get upgrade
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install unzip
unzip awscliv2.zip
sudo ./aws/install
aws --version
aws s3 ls

$ aws configure
  AWS Access Key ID [None]:
  AWS Secret Access Key [None]: 
  Default region name [None]:
  Default output format [None]:

https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html

aws sts get-caller-identity

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-services.html

aws ec2 describe-instances

make bucket
aws s3 mb s3://cli-demo-cohort-08

make ec2
aws ec2 run-instances --cli-input-json file://demo.json

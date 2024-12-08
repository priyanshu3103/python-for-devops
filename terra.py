import subprocess

def terraform_run(command):
    subprocess.run(command, shell= True, check=True)


dir="/mnt/c/Users/priya/Desktop/python_zero_to_hero/Wanderlust-Mega-Project-for-devops-practice/terraform"
# command= f"terraform -chdir={dir} init"
command= f"terraform -chdir={dir} plan"
# command= f"terraform -chdir={dir} apply -auto-approve"

terraform_run(command)
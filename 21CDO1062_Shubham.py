import boto3
ec2 = boto3.client('ec2')
instance_id = "i-08d957049c6e2fe94"
response = ec2.terminate_instances(InstanceIds=[instance_id])
print(f"Termination initiated for instance: {instance_id}")
print("Response:", response)

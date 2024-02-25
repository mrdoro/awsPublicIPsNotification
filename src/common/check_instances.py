import boto3

def check_public_ip(instance_ids):
    ec2 = boto3.client('ec2')

    # Describe instances
    response = ec2.describe_instances(InstanceIds=instance_ids)

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Check if the instance has a public IP address
            if 'PublicIpAddress' in instance:
                print(f"Instance {instance['InstanceId']} has a public IP address: {instance['PublicIpAddress']}")
                publicIP = instance['PublicIpAddress']
            else:
                print(f"Instance {instance['InstanceId']} does not have a public IP address.")
                publicIP = None

    return publicIP

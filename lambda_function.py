import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = ec2.describe_instances()

    instance_ids = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if instance['State']['Name'] == 'running':
                instance_ids.append(instance['InstanceId'])

    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)

    return {
        'statusCode': 200,
        'body': f'Stopped {len(instance_ids)} instances'
    }
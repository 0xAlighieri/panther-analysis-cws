from panther_base_helpers import deep_get

ALLOWED_REGIONS = ['us-west-1', 'us-west-2', 'us-east-2', 'us-east-1']


def policy(resource):
    ec2_instance_az = deep_get(
        resource, 'Placement', 'AvailabilityZone', default='')

    if not any(region in ec2_instance_az for region in ALLOWED_REGIONS):
        return False
    return True


def title(resource):
    ec2_instance_id = resource['InstanceId']
    ec2_instance_az = deep_get(
        resource, 'Placement', 'AvailabilityZone', default='')
    return f'EC2 instance {ec2_instance_id} found in unauthorized AZ:  \
    {ec2_instance_az}'


    



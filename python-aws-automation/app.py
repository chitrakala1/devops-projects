import boto3

def list_ec2_instances(region="ap-south-1"):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"], instance["State"]["Name"])

if __name__ == "__main__":
    list_ec2_instances()
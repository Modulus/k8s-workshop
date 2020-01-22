import boto3
import botocore
import argparse
import logging
from helpers import group_exists, user_exists,policy_exists

# Initializing loggers and requisites
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("Main")

logger.info("Starting creating of eks user")

parser = argparse.ArgumentParser(description="Create iam user for eks clusters on aws")
parser.add_argument("--profile", type=str,  dest="profile", help="name of the aws profile in ~/.aws/credentials",
                    required=True)
parser.add_argument("--user", type=str, dest="user_name", help="Username to create in aws iam", default="eks-admin")
parser.add_argument("--group", type=str, dest="group_name", help="Name of group connected to policies on aws iam", default="eks-admin")

args = parser.parse_args()

logger.info(f"Using profile {args.profile}")
logger.info(f"User will have the name: {args.user_name}")
logger.info(f"Group will have the name: {args.group_name}")

# Create iam group and policies
boto3.setup_default_session(profile_name=args.profile)


logging.info("Creating autoscaling iam group")

iam = boto3.client("iam")





group_name = args.group_name
user_name = args.user_name
eks_policy_name = "eksPolicy"


def create_group_and_policies():

    if group_exists(group_name=group_name, client=iam):
        logger.warning(f"Group {group_name} already exists, skipping creation")
    else:
        iam.create_group(GroupName=group_name, Path="/")
    logging.info("Attaching policies for eks to work")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AutoScalingFullAccess")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/IAMFullAccess")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonS3FullAccess")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonEC2FullAccess")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonEKSServicePolicy")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy")
    iam.attach_group_policy(GroupName=group_name, PolicyArn="arn:aws:iam::aws:policy/AmazonVPCFullAccess")


def get_expected_eks_policy_arn():
    account_id = get_account_id()
    if account_id and len(account_id) <= 0:
        raise ValueError("Could not extract account id, cannot continue")
    else:
        eks_policy_arn = f"arn:aws:iam::{account_id}:policy/eksPolicy"
        logger.info(f"Expected arn: {eks_policy_arn}")
        return eks_policy_arn


# Gets the account id of the user running this script
def get_account_id():
    return boto3.client('sts').get_caller_identity().get('Account')


def create_eks_policy():
    eks_policy_arn = get_expected_eks_policy_arn()
    if policy_exists(policy_arn=eks_policy_arn, policy_name=eks_policy_name, client=iam):
        logger.warning("Policy already exists, will not create again")
    else:
        try:
            result = iam.create_policy(
                PolicyName="eksPolicy",
                Path="/",
                PolicyDocument="""{
                               "Version": "2012-10-17",
                               "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "eks:*",
                    "Resource": "*"
                },
                {
                    "Effect": "Allow",
                    "Action": "cloudformation:*",
                    "Resource" : "*"
                }
            ]
            }""")

            return result
        except iam.exceptions.NoSuchEntityException:
            logger.warning(f"Group eksPolicy already created")
            return None
        except iam.exceptions.MalformedPolicyDocument:
            logger.error(f"Group eksPolicty failed to be created")
            return None


def attach_user_to_eks_policy():
    arn = get_expected_eks_policy_arn()
    logger.info(f"Attaching policy {arn} to user {user_name}")
    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn=arn
    )


def create_user_and_attach_to_group():
    logger.info(f"Creating user {user_name} if needed")
    if user_exists(user_name=user_name, client=iam):
        logger.warning(f"User {user_name} already exists, skipping creation")
    else:
        logging.info(f"Creating eks user")
        iam.create_user(
            Path="/",
            UserName=user_name,
            Tags=[
                {
                    "Key": "Automation",
                    "Value": "Boto3"
                },
                {
                    "Key": "Purpose",
                    "Value": "Terraform"
                }
            ]
        )
    logging.info(f"User {user_name} created, attaching it to the group {group_name}")
    iam.add_user_to_group(UserName=user_name, GroupName=group_name)


# Run the stuff
create_group_and_policies()
create_eks_policy()
create_user_and_attach_to_group()
attach_user_to_eks_policy()

logger.info("Finished!")


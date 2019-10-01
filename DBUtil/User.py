import json
import boto3,os,glob
import base64, json, logging


def cognito_connection(region):
    cognito_output = boto3.client("cognito-idp", region_name=region, aws_access_key_id='AKIA5GSJESCY2JNKKHO4',
                               aws_secret_access_key='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')
    return cognito_output

class UserDAO():
    userpoolid = 'ap-south-1_2uFgtTYi7'
    clientid = '36od52nqa7hk29eav48q24n7t7'
    region = 'ap-south-1'

    def user_AWSLogin(self,userData):
        try:
            cognito_idp = cognito_connection(self.region)
            response = cognito_idp.admin_initiate_auth(
                UserPoolId=self.userpoolid,
                ClientId=self.clientid,
                AuthFlow='ADMIN_NO_SRP_AUTH',
                AuthParameters={
                    'USERNAME': userData["username"],
                    'PASSWORD': userData["password"]
                }
            )
        except Exception as exception:
            return exception
        else:
           return response

    def update_aws_first_time_password(self,updateData):
        try:
            cognito_idp = cognito_connection(self.region)
            response = cognito_idp.respond_to_auth_challenge(
                ClientId=self.clientid,
                ChallengeName=updateData['ChallengeName'],
                Session=updateData['Session'],
                ChallengeResponses={
                    'NEW_PASSWORD': updateData['new_password'],
                    'USERNAME': updateData['username']
                }
            )
        except Exception as e:
            return e
        else:
            return response

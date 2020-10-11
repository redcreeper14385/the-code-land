import boto3
import sys
from botocore.exceptions import ClientError


def sendEmail(SENDER, RECIPIENT, SUBJECT, BODY_TEXT):

    AWS_REGION = "us-west-2" #YOUR AWS REGION
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                        ],
                    },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                            },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                            },
                        },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                        },
                    },
                Source=SENDER)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

if __name__ == "__main__":

   sender=sys.argv[1]
   receiver=sys.argv[2]
   subject=sys.argv[3]
   body=sys.argv[4]
   sendEmail(sender, receiver, subject, body)

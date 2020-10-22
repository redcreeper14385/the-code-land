""" This example script uses aws recognition service to compare face from 2 image """
import boto3
import base64
import argparse
import sys

parser = argparse.ArgumentParser(description='Face compare/Text extraction using AWS rekognition')
parser.add_argument('--a', type=str, help='aws access_key', required=True)
parser.add_argument('--s', type=str, help='aws secret_key', required=True)
parser.add_argument('--f1', type=str, help='first/source image', required=True)
parser.add_argument('--f2', type=str, help='second/target image', required=True)
args = parser.parse_args()

#user inputs
aws_access_key = args.a
aws_secret_key = args.s
source_image = args.f1
target_image = args.f2

def convertImagetoB64(image):
    with open(image, 'rb') as file:
        encode_image = base64.encodebytes(file.read())
    return encode_image

def compare_faces_aws(source_file, target_file, access_key, secret_key, similarity_threshold):
    """ compare two faces to find similarity 
        useful for user kyc/authentication
    """
    score = None
    match_flag = 0
    client = boto3.client('rekognition', region_name='us-west-2', aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key)
    source_file = convertImagetoB64(source_file)
    target_file = convertImagetoB64(target_file)

    imageSource = base64.b64decode(source_file)
    imageTarget = base64.b64decode(target_file)

    response = client.compare_faces(SimilarityThreshold=similarity_threshold,
                                    SourceImage={'Bytes': imageSource},
                                    TargetImage={'Bytes': imageTarget})

    similarity = 0
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = faceMatch['Similarity']
        print(faceMatch)

    if similarity > similarity_threshold:
        match_flag = 1
        score = round(similarity, 2)
        return {'message': 'MATCH - confidence factor ' + str(round(similarity, 2)) + '%', 'score': score, 'match_flag': match_flag}
    else:
        match_flag = 0
        score = round(similarity, 2)

        return {'message': 'NOT MATCH - confidence factor ' + str(round(similarity, 2)) + '%', 'score': score, 'match_flag': match_flag}


def main():
    """ main method """
    response = compare_faces_aws(source_image, target_image, aws_access_key, aws_secret_key, 80)
    print(response)

if __name__ == "__main__":
    main()

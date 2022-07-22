import json

def get_success_response(status_code=200, message='Success', data=None):
    return {
        'statusCode': status_code,
        'headers': {"Access-Control-Allow-Origin":"*"},
        'body': json.dumps({
            'responseCode': status_code,
            'message': message,
            'response': data
        })
    }


def get_custom_error(status_code=400, message='Error', data=None):
    return {
        'statusCode': status_code,
        'headers': {"Access-Control-Allow-Origin":"*"},
        'body': json.dumps({
            'responseCode': status_code,
            'message': message,
            'response': data
        })
    }



class CustomValidationErrors:

    def __init__(self, data) -> None:
        self.data = data

    def extract_value(self):
        for value in self.data.values():
            return value

    def get_error(self):
        self.data = self.data.normalized_messages()
        while isinstance(self.data, dict):
            self.data = self.extract_value()
        return get_custom_error(status_code=400, message='Validation Error',
                                data={"message": self.data[0]})


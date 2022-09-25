'use strict';

//A simple Lambda function
exports.handler = (event, context, callback) => {
    console.log('This is our local lambda function');
    console.log('Creating a PetStore service');
    callback(null, "Hello " + event.Records[0].dynamodb.NewImage.Message.S + "!What kind of pet are you interested in?");
}
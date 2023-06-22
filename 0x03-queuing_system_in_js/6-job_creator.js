const kue = require('kue');
const queue = kue.createQueue();

const jobs = {
    phoneNumber: 1234567890,
    message: "This is you"
}

var job = queue.create('push_notification_code', jobs)
  .save((error) => {
    if (!error) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', function(result){
  console.log('Notification job completed');
}).on('failed', function(errorMessage){
  console.log('Notification job failed');
})

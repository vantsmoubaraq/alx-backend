const kue = require('kue');
const queue = kue.createQueue();
const black_listed = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    const total = 100;
    job.progress(0, total);
  
    if (black_listed.includes(phoneNumber)) {
      return done(Error(`Phone number ${phoneNumber} is blacklisted`));
    }
  
    job.progress(50, total);
    console.log( `Sending notification to ${phoneNumber}, with message: ${message}`);
    return done();
}



queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});


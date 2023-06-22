function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs))
        throw Error('Jobs is not an array');
    jobs.forEach((job_to) => {
        var job = queue.createJob('push_notification_code', job_to)
        .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`);
        });
        job.on('complete', function(result){
            console.log('Notification job completed');
        }).on('failed', function(errorMessage){
            console.log('Notification job failed');
        }).on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    })
}

module.exports = createPushNotificationsJobs;